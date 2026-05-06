"""Cosmoblog — lightweight Sphinx blog engine.

Single-author, multilingual blog engine optimized for fast compilation
and correct-by-default output. Languages are inferred from directory
structure; post metadata from YAML frontmatter.

Registers itself as a Sphinx extension via ``setup()``.
"""

from __future__ import annotations

import os
import re
from glob import glob
from pathlib import Path, PurePath
from typing import Any

from sphinx.application import Sphinx

from .directives import PostListDirective, UpdateDirective, UpdateNode
from .engine import BlogEngine

__version__ = "0.1.0"


def setup(app: Sphinx) -> dict[str, Any]:
    """Register cosmoblog as a Sphinx extension."""
    app.require_sphinx("6.2")

    # --- Config values (all optional) ---
    app.add_config_value("blog_path", "blog", "env")
    app.add_config_value("blog_post_pattern", "*/blog/*/*", "env")
    app.add_config_value("blog_feed_fulltext", True, "env")

    # --- Directives ---
    app.add_directive("postlist", PostListDirective)
    app.add_directive("update", UpdateDirective)
    app.add_node(
        UpdateNode,
        html=(
            lambda s, n: s.visit_admonition(n),
            lambda s, n: s.depart_admonition(n),
        ),
        latex=(
            lambda s, n: s.visit_admonition(n),
            lambda s, n: s.depart_admonition(n),
        ),
    )

    # --- Event hooks ---
    app.connect("config-inited", _config_inited)
    app.connect("builder-inited", _builder_inited)
    app.connect("env-before-read-docs", _env_before_read)
    app.connect("doctree-read", _doctree_read)
    app.connect("env-purge-doc", _env_purge_doc)
    app.connect("env-merge-info", _env_merge_info)
    app.connect("doctree-resolved", _doctree_resolved)
    app.connect("html-collect-pages", _html_collect_pages)
    app.connect("html-page-context", _html_page_context)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


# ---------------------------------------------------------------------------
# Event handlers
# ---------------------------------------------------------------------------


def _config_inited(app: Sphinx, config: Any) -> None:
    """Glob post patterns and discover languages from directories."""
    pattern = config.blog_post_pattern
    if isinstance(pattern, str):
        pattern = [pattern]

    matched: set[str] = set()
    for pat in pattern:
        full = os.path.join(app.srcdir, pat)
        matched.update(
            PurePath(p).relative_to(app.srcdir).with_suffix("").as_posix()
            for p in glob(full, recursive=True)
        )
    config.cosmoblog_matched_posts = matched

    # Discover languages from directory structure
    languages = _discover_languages(Path(app.srcdir))
    config.cosmoblog_languages = languages


def _builder_inited(app: Sphinx) -> None:
    """Initialize the BlogEngine and force dirhtml builder for pretty URLs."""
    # Opinionated: always use dirhtml for pretty URLs (page/ not page.html).
    if app.builder.name == "html":
        app.builder = app.create_builder("dirhtml")
        app.builder.init()

    if not hasattr(app.env, "cosmoblog"):
        app.env.cosmoblog = BlogEngine(
            languages=app.config.cosmoblog_languages,
            matched_patterns=app.config.cosmoblog_matched_posts,
        )
    else:
        # Update with potentially new matched patterns
        app.env.cosmoblog.matched_patterns = app.config.cosmoblog_matched_posts
        app.env.cosmoblog.languages = app.config.cosmoblog_languages


def _env_before_read(app: Sphinx, env: Any, docnames: list[str]) -> None:
    """Ensure engine exists and has current config before reading docs."""
    if not hasattr(env, "cosmoblog"):
        env.cosmoblog = BlogEngine(
            languages=app.config.cosmoblog_languages,
            matched_patterns=app.config.cosmoblog_matched_posts,
        )
    else:
        # Update config-derived fields
        env.cosmoblog.matched_patterns = app.config.cosmoblog_matched_posts
        env.cosmoblog.languages = app.config.cosmoblog_languages


def _doctree_read(app: Sphinx, doctree: Any) -> None:
    """Register post metadata from frontmatter on doctree-read."""
    from .engine import register_post
    register_post(app, doctree)


def _env_purge_doc(app: Sphinx, env: Any, docname: str) -> None:
    """Remove a document from the blog engine on env-purge-doc."""
    if hasattr(env, "cosmoblog"):
        env.cosmoblog.purge(docname)


def _env_merge_info(
    app: Sphinx, env: Any, docnames: list[str], other: Any
) -> None:
    """Merge blog engine state from parallel reads."""
    if not hasattr(other, "cosmoblog"):
        return
    if not hasattr(env, "cosmoblog"):
        env.cosmoblog = other.cosmoblog
        return
    for docname, post in other.cosmoblog.posts.items():
        env.cosmoblog.register(post)


def _doctree_resolved(app: Sphinx, doctree: Any, docname: str) -> None:
    """Resolve {postlist} directive nodes into rendered content."""
    from .directives import resolve_postlists
    resolve_postlists(app, doctree, docname)


def _html_collect_pages(app: Sphinx) -> Any:
    """Generate tag pages and Atom feeds."""
    from .engine import generate_tag_pages
    from .feeds import generate_atom_feeds

    yield from generate_tag_pages(app)
    yield from generate_atom_feeds(app)


def _html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> None:
    """Inject cosmoblog data into template context."""
    engine: BlogEngine = getattr(app.env, "cosmoblog", None)
    if engine is None:
        return

    # Make the engine available to templates
    context["cosmoblog"] = engine

    # Provide current post info if this page is a post
    post = engine.posts.get(pagename)
    context["cosmoblog_post"] = post

    # Anchor helper for template compatibility
    context["anchor"] = lambda p: f"#{p.section}" if getattr(p, "section", None) else ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _discover_languages(srcdir: Path) -> set[str]:
    """Scan for ``{lang}/blog/`` directories where *lang* is a 2-letter code.

    Supports any number of languages — add ``fr/blog/``, ``pt/blog/``, etc.
    """
    return {
        d.name
        for d in srcdir.iterdir()
        if d.is_dir() and len(d.name) == 2 and (d / "blog").is_dir()
    }
