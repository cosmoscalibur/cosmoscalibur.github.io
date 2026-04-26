"""Customizations for ABlog blog generation.

ABlog auto-generates several types of listing pages that are suppressed
because the site uses manual, language-specific alternatives:

- **Category pages** (``blog/category/{slug}/``): Suppressed in favor of
  manual category pages with curated descriptions under
  ``es/blog/category/`` and ``en/blog/category/``.
- **"All Posts" page** (``blog/``): Suppressed in favor of
  language-specific archive pages at ``es/blog/archive/`` and
  ``en/blog/archive/``.
- **Archive pages** (``blog/archive/``): Same reason as above.
- **Author pages** (``blog/author/``): Suppressed because the blog has a
  single author configured via ``blog_default_author`` and these pages
  add no navigational or SEO value.

The suppression works by disconnecting ABlog's ``html-collect-pages``
handler for ``generate_archive_pages`` and replacing it with a filtered
version that skips the unwanted pages.
"""

from collections.abc import Generator
from typing import Any

from sphinx.application import Sphinx

# Prefixes and docname patterns to suppress from ABlog's auto-generated
# archive pages.
_SUPPRESSED_PREFIXES = (
    "blog/category/",
    "blog/category",
    "blog/archive/",
    "blog/archive",
    "blog/author/",
    "blog/author",
)


def _filtered_archive_pages(
    app: Sphinx,
) -> Generator[tuple[str, dict[str, Any], str], None, None]:
    """Generate archive pages, skipping suppressed pages.

    Imports ABlog's original generator lazily to avoid import-order issues.
    """
    from ablog.post import generate_archive_pages  # noqa: PLC0415

    blog_docname = getattr(app, "_ablog_blog_docname", None)
    if blog_docname is None:
        from ablog.blog import Blog  # noqa: PLC0415
        blog_docname = Blog(app).posts.docname
        app._ablog_blog_docname = blog_docname

    for page_data in generate_archive_pages(app):
        docname = page_data[0]
        # Suppress the "All Posts" page (blog/ or blog/blog/)
        if docname == blog_docname:
            continue
        # Suppress category, archive, and author pages
        if any(
            docname.startswith(p) or docname == p.rstrip("/")
            for p in _SUPPRESSED_PREFIXES
        ):
            continue
        yield page_data


def setup(app: Sphinx) -> None:
    """Replace ABlog's archive page generator during Sphinx setup.

    Called from the theme's ``setup()`` which runs after ABlog's own
    ``setup()`` has registered its event handlers.
    """
    listeners = app.events.listeners.get("html-collect-pages", [])

    # Find and remove ABlog's generate_archive_pages listener
    to_remove = []
    for listener in listeners:
        handler = listener.handler
        qualname = getattr(handler, "__qualname__", "")
        module = getattr(handler, "__module__", "")
        if "generate_archive_pages" in qualname and "ablog" in module:
            to_remove.append(listener)

    for listener in to_remove:
        listeners.remove(listener)

    # Connect our filtered version
    app.connect("html-collect-pages", _filtered_archive_pages)
