"""Blog engine core — PostInfo dataclass and BlogEngine state manager.

Stores post metadata on ``env.cosmoblog`` as a flat dict. No singleton
pattern, no catalog hierarchy. Only tags are indexed for auto-generation;
categories, archive, and language filtering are handled by user-written
pages with ``{postlist}`` directives.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from datetime import date as date_cls, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any
from unicodedata import normalize

import base64
import hashlib

from docutils import nodes
from sphinx.util.logging import getLogger

if TYPE_CHECKING:
    from sphinx.application import Sphinx

logger = getLogger(__name__)

# Date format used for parsing frontmatter dates
_DATE_FORMAT = "%Y-%m-%d"


def _is_notebook_equation_render(img_node: nodes.image) -> bool:
    """Detect if a notebook image is a rendered equation (SymPy/LaTeX).

    Walks up the doctree to the myst-nb ``mime_bundle`` container and
    checks if a sibling container has ``mime_type: 'text/latex'``.
    Equation renders always have a ``text/latex`` MIME alternative
    alongside the ``image/png``; plot outputs (matplotlib, etc.) do not.
    """
    # Walk up to find the mime_bundle container
    node = img_node
    mime_bundle = None
    for _ in range(4):  # image → container → container → mime_bundle
        node = node.parent
        if node is None:
            return False
        if hasattr(node, "get") and node.get("nb_element") == "mime_bundle":
            mime_bundle = node
            break

    if mime_bundle is None:
        return False

    # Check siblings for a text/latex MIME container
    for child in mime_bundle.children:
        if hasattr(child, "get") and child.get("mime_type") == "text/latex":
            return True

    return False


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = normalize("NFKD", str(text))
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


@dataclass(slots=True)
class PostInfo:
    """Metadata for a single blog post."""

    docname: str
    date: date_cls | None
    update: date_cls | None
    title: str
    tags: list[str]
    category: list[str]
    language: str
    excerpt: str  # Plain text excerpt (first paragraph)
    published: bool
    image: str = ""  # URI of the first image in the post (if any)
    image_alt: str = ""  # Alt text for the first image
    image_width: str = ""  # Width of the first image
    image_height: str = ""  # Height of the first image
    section: str = ""

    def __lt__(self, other: PostInfo) -> bool:
        """Sort by date descending (newest first), then title."""
        sd = self.date or date_cls.max
        od = other.date or date_cls.max
        return (sd, self.title) < (od, other.title)

    def __str__(self) -> str:
        return self.title


class BlogEngine:
    """Blog state stored on ``env``.

    Only tags are indexed for auto-generation. Categories, archive,
    and language filtering are handled by user-written pages with
    ``{postlist}`` directives.
    """

    def __init__(
        self,
        languages: set[str] | None = None,
        matched_patterns: set[str] | None = None,
    ) -> None:
        self.posts: dict[str, PostInfo] = {}
        self.tags: dict[str, list[str]] = {}  # tag → [docnames]
        self.languages: set[str] = languages or set()
        self.matched_patterns: set[str] = matched_patterns or set()
        self.date_format: str = _DATE_FORMAT
        self.date_format_short: str = _DATE_FORMAT

    def register(self, post: PostInfo) -> None:
        """Register a post and index its tags."""
        self.posts[post.docname] = post
        for tag in post.tags:
            self.tags.setdefault(tag, []).append(post.docname)

    def purge(self, docname: str) -> None:
        """Remove a post from the engine."""
        post = self.posts.pop(docname, None)
        if post is None:
            return
        for tag in post.tags:
            docs = self.tags.get(tag, [])
            if docname in docs:
                docs.remove(docname)
            if not docs:
                self.tags.pop(tag, None)

    def recent(
        self,
        n: int | None = None,
        exclude: str | None = None,
        lang: str | None = None,
    ) -> list[PostInfo]:
        """Return recent published posts, newest first.

        Parameters
        ----------
        n : int or None
            Maximum number of posts to return. ``None`` returns all.
        exclude : str or None
            Docname to exclude (current page).
        lang : str or None
            Filter by language.
        """
        posts = [
            p for p in self.posts.values()
            if p.published and p.docname != exclude
        ]
        if lang:
            posts = [p for p in posts if p.language == lang]
        posts.sort(reverse=True)
        if n is not None:
            posts = posts[:n]
        return posts

    def by_tag(self, tag: str) -> list[PostInfo]:
        """Return all published posts with a given tag, newest first."""
        docnames = self.tags.get(tag, [])
        posts = [
            self.posts[d] for d in docnames
            if d in self.posts and self.posts[d].published
        ]
        posts.sort(reverse=True)
        return posts

    def by_category(
        self, category: str, lang: str | None = None
    ) -> list[PostInfo]:
        """Return published posts in a category, newest first."""
        posts = [
            p for p in self.posts.values()
            if p.published and category in p.category
        ]
        if lang:
            posts = [p for p in posts if p.language == lang]
        posts.sort(reverse=True)
        return posts

    def by_language(self, lang: str) -> list[PostInfo]:
        """Return all published posts for a language, newest first."""
        posts = [
            p for p in self.posts.values()
            if p.published and p.language == lang
        ]
        posts.sort(reverse=True)
        return posts

    def by_date_desc(self, lang: str | None = None) -> list[PostInfo]:
        """Return all published posts sorted newest first."""
        posts = [p for p in self.posts.values() if p.published]
        if lang:
            posts = [p for p in posts if p.language == lang]
        posts.sort(reverse=True)
        return posts


# ---------------------------------------------------------------------------
# Post registration (called from doctree-read handler)
# ---------------------------------------------------------------------------


def _split_csv(value: str | list | None) -> list[str]:
    """Split a comma-separated string into a list of stripped values."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [v.strip() for v in str(value).split(",") if v.strip()]


def _parse_date(value: str | date_cls | datetime | None) -> date_cls | None:
    """Parse a date value from frontmatter metadata.

    YAML auto-parses ``2024-05-14`` as :class:`datetime.date` and
    ``2024-05-14 10:30:00`` as :class:`datetime.datetime`.  Handle
    both native types and string fallback.  Always returns a
    :class:`date` (no time component).
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date_cls):
        return value
    try:
        return datetime.strptime(str(value).strip(), _DATE_FORMAT).date()
    except ValueError:
        return None


def _infer_language(
    docname: str, languages: set[str], default_lang: str
) -> str:
    """Infer post language from path prefix.

    ``en/blog/2025/some-post`` → ``en``
    ``es/blog/2024/otro-post`` → ``es``

    Falls back to ``default_lang`` for root-level documents.
    """
    prefix = docname.split("/", maxsplit=1)[0]
    if prefix in languages:
        return prefix
    return default_lang


def _get_update_dates(
    section: nodes.Node, docname: str
) -> list[date_cls]:
    """Extract dates from {update} directives and set their titles."""
    from .directives import UpdateNode

    update_dates: list[date_cls] = []
    for node in section.findall(UpdateNode):
        date_str = node.get("date", "")
        dt = _parse_date(date_str)
        if dt is None:
            logger.warning("Invalid update date '%s' in %s", date_str, docname)
            continue
        # Insert a title node for the admonition rendering
        title_text = f"Updated on {dt.strftime(_DATE_FORMAT)}"
        title_node = nodes.title("", title_text)
        node.insert(0, title_node)
        node["classes"] = ["note", "update"]
        update_dates.append(dt)
    return update_dates


def register_post(app: Sphinx, doctree: Any) -> None:
    """Register post metadata from doctree frontmatter.

    Called from the ``doctree-read`` event handler.

    MyST extracts frontmatter into ``env.metadata[docname]`` before
    ``doctree-read`` fires, so we read from there instead of parsing
    docinfo nodes.
    """
    env = app.env
    engine: BlogEngine = getattr(env, "cosmoblog", None)
    if engine is None:
        return

    docname = env.docname

    # Early rejection: only process matched blog posts
    if docname not in engine.matched_patterns:
        return

    # Read metadata from env (MyST extracts frontmatter here)
    metadata = env.metadata.get(docname, {})
    if not metadata:
        # Fallback: check docinfo nodes for non-MyST sources
        docinfo_nodes = list(doctree.findall(nodes.docinfo))
        if docinfo_nodes:
            docinfo = docinfo_nodes[0]
            metadata = {}
            for field_node in docinfo.findall(nodes.field):
                children = list(field_node.children)
                if len(children) >= 2:
                    name = children[0].astext().lower()
                    value = children[1].astext()
                    metadata[name] = value
            for date_node in docinfo.findall(nodes.date):
                metadata["date"] = date_node.astext()
        if not metadata:
            return

    # Must have a date to be a blog post (or be in matched patterns)
    date = _parse_date(metadata.get("date"))

    # Parse tags — handle MyST list format ["a", "b"] or CSV
    tags_raw = metadata.get("tags", "")
    if isinstance(tags_raw, str):
        # MyST may store as ["a", "b", "c"] string
        tags_raw = tags_raw.strip().lstrip("[").rstrip("]")
        tags_raw = ",".join(
            t.strip().strip("'\"") for t in tags_raw.split(",")
        )
    tags = _split_csv(tags_raw)

    category = _split_csv(metadata.get("category"))

    # Language: always inferred from path
    default_lang = getattr(app.config, "language", "en") or "en"
    # Use the original default language, not the forced "en"
    blog_default_lang = getattr(app.config, "blog_default_language", None)
    if blog_default_lang:
        default_lang = blog_default_lang
    language = _infer_language(docname, engine.languages, default_lang)

    # Title
    title = ""
    sections = list(doctree.findall(nodes.section))
    if sections:
        for title_node in sections[0].findall(nodes.title):
            title = title_node.astext()
            break

    # Update dates from {update} directives
    section = doctree if not sections else sections[0]
    update_dates = _get_update_dates(section, docname)
    all_dates = [d for d in update_dates + ([date] if date else []) if d]
    update = max(all_dates) if all_dates else None

    # Excerpt (first paragraph, as plain text)
    excerpt = ""
    for para in section.findall(nodes.paragraph):
        excerpt = para.astext()
        break

    # First image in post (URI + alt text, for postlist cards).
    # For notebook posts, skip equation renders (SymPy/LaTeX) and prefer
    # the first actual plot output (matplotlib, etc.).
    image_uri = ""
    image_alt = ""
    image_width = ""
    image_height = ""
    first_img_node = None  # Fallback if all images are equations
    for img_node in section.findall(nodes.image):
        uri = img_node.get("uri", "")

        # For notebook images, skip equation renders.
        # Equations are identified by a text/latex sibling in the
        # myst-nb mime_bundle container (doctree structure).
        if "jupyter_execute" in uri and _is_notebook_equation_render(img_node):
            if first_img_node is None:
                first_img_node = img_node
            continue

        # Normalize URI to be source-absolute (leading /)
        if uri.startswith("data:"):
            # Predict the URI that Base64ImageTransform will produce.
            # Avoid full extraction here; the post-transform handles disk I/O.
            try:
                _header, encoded = uri.split(",", 1)
                data = base64.b64decode(encoded)
                sha = hashlib.sha256(data).hexdigest()[:12]
                image_uri = f"/_images/nb_inline/{sha}.webp"
            except Exception:
                image_uri = uri
        elif not uri.startswith(("/", "http://", "https://", "//")):
            srcdir = Path(app.srcdir)
            doc_dir = str(Path(docname).parent)
            
            # Try to find where the file actually is in the source tree
            potential_paths = [
                srcdir / doc_dir / uri,
                srcdir / uri.lstrip("/"),
            ]
            found = False
            for p in potential_paths:
                if p.is_file():
                    # Convert to root-relative path with leading slash
                    rel_p = p.relative_to(srcdir)
                    image_uri = "/" + str(rel_p)
                    found = True
                    break
            if not found:
                # Fallback to original URI
                image_uri = uri
        else:
            image_uri = uri

        image_alt = img_node.get("alt", "")
        
        # Extract dimensions directly for PostInfo
        image_width = img_node.get("width", "")
        image_height = img_node.get("height", "")
        if not (image_width and image_height) and not uri.startswith("data:"):
            # Try finding the file to get dimensions
            from .transforms import _get_image_size
            srcdir = Path(app.srcdir)
            doc_dir = str(Path(docname).parent)
            # Try several paths (absolute, relative, root-relative)
            paths_to_try = [
                srcdir / uri.lstrip("/"),
                srcdir / doc_dir / uri,
            ]
            if "images/" in uri:
                paths_to_try.append(srcdir / "images" / uri.split("images/")[-1])
            
            for p in paths_to_try:
                if p.is_file():
                    try:
                        w, h = _get_image_size(p)
                        if w and h:
                            image_width = str(w)
                            image_height = str(h)
                            break
                    except Exception:
                        pass
        break

    # Fallback: if all notebook images were equations, use the first one
    if not image_uri and first_img_node is not None:
        uri = first_img_node.get("uri", "")
        image_uri = uri if uri.startswith("/") else "/" + uri
        image_alt = first_img_node.get("alt", "")

    # Published if has a date and date is not in the future
    published = date is not None and date <= date_cls.today()

    # Make orphan to suppress toctree warnings
    env.metadata.setdefault(docname, {})["orphan"] = True

    # Create and register the post
    post = PostInfo(
        docname=docname,
        date=date,
        update=update,
        title=title,
        tags=tags,
        category=category,
        language=language,
        excerpt=excerpt,
        published=published,
        image=image_uri,
        image_alt=image_alt,
        image_width=image_width,
        image_height=image_height,
    )
    engine.register(post)


# ---------------------------------------------------------------------------
# Tag page generation
# ---------------------------------------------------------------------------


def generate_tag_pages(app: Sphinx) -> Any:
    """Generate tag index and per-tag pages.

    Only generates pages for tags that don't already have a manual page.
    """
    engine: BlogEngine = getattr(app.env, "cosmoblog", None)
    if engine is None:
        return

    blog_path = app.config.blog_path or "blog"
    found_docs = app.env.found_docs
    tag_base = f"{blog_path}/tag"

    # Tag index page
    tag_index_docname = tag_base
    if tag_index_docname not in found_docs:
        context = {
            "parents": [],
            "title": "Tags",
            "tags": engine.tags,
            "engine": engine,
            "summary": True,
        }
        yield (tag_index_docname, context, "cosmoscalibur/tag_index.html")

    # Per-tag pages
    for tag_name, docnames in engine.tags.items():
        tag_slug = slugify(tag_name)
        tag_docname = f"{tag_base}/{tag_slug}"
        if tag_docname not in found_docs:
            posts = engine.by_tag(tag_name)
            context = {
                "parents": [],
                "title": f"Posts tagged {tag_name}",
                "header": "Posts tagged",
                "tag_name": tag_name,
                "collection_posts": posts,
                "engine": engine,
                "summary": True,
            }
            yield (tag_docname, context, "cosmoscalibur/tag_detail.html")
