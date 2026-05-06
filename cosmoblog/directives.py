"""Blog directives — ``{postlist}`` and ``{update}``.

``{postlist}`` renders a list of posts filtered by options.
``{update}`` renders an admonition and sets post modified timestamp.
"""

from __future__ import annotations

from string import Formatter
from typing import TYPE_CHECKING, Any

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.util.nodes import set_source_info

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def _split(a: str | None) -> list[str]:
    """Split a comma-separated option string."""
    return [s.strip() for s in (a or "").split(",") if s.strip()]


# ---------------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------------


class PostListNode(nodes.General, nodes.Element):
    """Placeholder node for ``{postlist}`` — resolved in doctree-resolved."""


class UpdateNode(nodes.admonition):
    """Admonition node for ``{update}`` directive."""


# ---------------------------------------------------------------------------
# Directives
# ---------------------------------------------------------------------------


class PostListDirective(Directive):
    """Handle ``{postlist}`` directives.

    Renders a list of blog posts, optionally filtered by ``:category:``,
    ``:language:``, ``:tags:``, etc.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {
        "tags": _split,
        "category": _split,
        "language": _split,
        "format": lambda a: a.strip(),
        "date": lambda a: a.strip(),
        "sort": directives.flag,
        "excerpts": directives.flag,
        "list-style": lambda a: a.strip(),
        "expand": directives.unchanged,
    }

    def run(self) -> list[nodes.Node]:
        node = PostListNode()
        node.document = self.state.document
        set_source_info(self, node)
        node["length"] = int(self.arguments[0]) if self.arguments else None
        node["tags"] = self.options.get("tags", [])
        node["category"] = self.options.get("category", [])
        node["language"] = self.options.get("language", [])
        node["format"] = self.options.get("format", "{date} - {title}")
        node["date"] = self.options.get("date", None)
        node["sort"] = "sort" in self.options
        node["excerpts"] = "excerpts" in self.options
        node["list-style"] = self.options.get("list-style", "none")
        node["expand"] = self.options.get("expand", None)
        return [node]


class UpdateDirective(BaseAdmonition):
    """Handle ``{update}`` directives.

    Renders an admonition and stores the update date for post metadata.
    The date is extracted during ``doctree-read`` to set
    ``PostInfo.update``.
    """

    required_arguments = 1
    node_class = UpdateNode

    def run(self) -> list[nodes.Node]:
        ad = super().run()
        ad[0]["date"] = self.arguments[0] if self.arguments else ""
        return ad


# ---------------------------------------------------------------------------
# Postlist resolution (called from doctree-resolved)
# ---------------------------------------------------------------------------


def resolve_postlists(app: Sphinx, doctree: Any, docname: str) -> None:
    """Replace ``PostListNode`` placeholders with rendered post lists."""
    from .engine import BlogEngine

    engine: BlogEngine = getattr(app.env, "cosmoblog", None)
    if engine is None:
        return

    for node in doctree.findall(PostListNode):
        posts = _filter_posts(engine, node, docname)
        bl = _render_post_list(app, posts, node, docname, engine)
        node.replace_self(bl)


def _filter_posts(
    engine: Any, node: PostListNode, docname: str
) -> list[Any]:
    """Filter posts based on postlist node options."""
    from .engine import PostInfo

    # Start with all published posts
    posts = [p for p in engine.posts.values() if p.published]

    # Filter by tags
    if node["tags"]:
        tag_set = set(node["tags"])
        posts = [p for p in posts if tag_set & set(p.tags)]

    # Filter by category
    if node["category"]:
        cat_set = set(node["category"])
        posts = [p for p in posts if cat_set & set(p.category)]

    # Filter by language
    if node["language"]:
        lang_set = set(node["language"])
        posts = [p for p in posts if p.language in lang_set]

    # Sort by date (newest first by default)
    posts.sort(reverse=True)

    if node["sort"]:
        # Alphabetical sort (oldest first)
        posts.sort()

    # Limit
    length = node.get("length")
    if length is not None:
        posts = posts[:length]

    return posts


def _render_post_list(
    app: Sphinx,
    posts: list[Any],
    node: PostListNode,
    docname: str,
    engine: Any,
) -> nodes.bullet_list:
    """Render a list of posts as a docutils bullet_list."""
    date_format = node["date"] or engine.date_format_short
    fmts = list(Formatter().parse(node["format"]))
    excerpts = node["excerpts"]
    expand = node["expand"]

    bl = nodes.bullet_list()
    bl.attributes["classes"].append("postlist-style-" + node["list-style"])
    bl.attributes["classes"].append("postlist")

    for post in posts:
        bli = nodes.list_item()
        bli.attributes["classes"].append("ablog-post")
        bl.append(bli)

        par = nodes.paragraph()
        bli.append(par)

        for text, key, _spec, _conv in fmts:
            if text:
                par.append(nodes.Text(text))
            if key is None:
                continue
            if key == "date":
                if post.date:
                    par.append(nodes.Text(post.date.strftime(date_format)))
            elif key == "title":
                ref = nodes.reference()
                ref["refuri"] = app.builder.get_relative_uri(
                    docname, post.docname
                )
                ref["internal"] = True
                ref["ids"] = []
                ref["backrefs"] = []
                ref["dupnames"] = []
                ref["classes"] = []
                ref["names"] = []
                ref.append(nodes.Text(post.title))
                par.attributes["classes"].append("ablog-post-title")
                par.append(ref)
            elif key == "category":
                for i, cat in enumerate(post.category, start=1):
                    par.append(nodes.Text(cat))
                    if i < len(post.category):
                        par.append(nodes.Text(", "))
            elif key == "tags":
                for i, tag in enumerate(post.tags, start=1):
                    par.append(nodes.Text(tag))
                    if i < len(post.tags):
                        par.append(nodes.Text(", "))

        if excerpts and post.excerpt:
            epar = nodes.paragraph()
            epar.attributes["classes"].append("ablog-post-excerpt")
            epar.append(nodes.Text(post.excerpt))
            bli.append(epar)

            # Render first image from post (if any)
            if post.image:
                img_ref_uri = app.builder.get_relative_uri(
                    docname, post.docname
                )
                img_ref = nodes.reference()
                img_ref["refuri"] = img_ref_uri
                img_ref["internal"] = True
                img_ref["ids"] = []
                img_ref["backrefs"] = []
                img_ref["dupnames"] = []
                img_ref["classes"] = [
                    "ablog-post-excerpt",
                    "reference",
                    "internal",
                    "image-reference",
                ]
                img_ref["names"] = []
                img_node = nodes.image()
                img_node["uri"] = post.image
                img_node["alt"] = post.image_alt or post.title
                img_node["classes"] = ["ablog-post-excerpt"]
                img_node["candidates"] = {"?": post.image}
                img_ref.append(img_node)
                bli.append(img_ref)

            if expand:
                ref_uri = app.builder.get_relative_uri(
                    docname, post.docname
                )
                expand_par = nodes.paragraph()
                expand_par.attributes["classes"].append("ablog-post-expand")
                refnode = nodes.reference(
                    "", "", internal=True, refuri=ref_uri
                )
                innernode = nodes.emphasis(text=expand)
                refnode.append(innernode)
                expand_par.append(refnode)
                bli.append(expand_par)

    return bl
