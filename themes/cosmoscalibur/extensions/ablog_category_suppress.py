"""Allowlist filter for ABlog auto-generated pages.

ABlog's ``generate_archive_pages`` handler produces listing pages for
every catalog (tags, categories, authors, languages, yearly archives,
drafts) plus a global "All Posts" index. This site uses manual,
language-prefixed alternatives for most of them, so only a small subset
is allowed through:

- **Tag pages** (``blog/tag/*``): Per-tag listing pages used for
  cross-language tag navigation.
- **Post redirects**: Legacy URL redirects emitted before catalog pages
  (these don't start with ``blog/``).

Everything else under ``blog/`` is suppressed:

- ``blog/`` (all posts index)
- ``blog/archive/YYYY/`` (yearly archives)
- ``blog/category/*``
- ``blog/author/*``
- ``blog/language/*``
- ``blog/drafts/``

The suppression works by disconnecting ABlog's ``html-collect-pages``
handler and replacing it with a filtered version that only yields
pages matching the allowlist.
"""

from collections.abc import Generator
from typing import Any

from sphinx.application import Sphinx

# Only pages starting with these prefixes pass through the filter.
# Everything else produced by ABlog's generate_archive_pages is dropped.
_ALLOWED_PREFIXES = (
    "blog/tag/",
)


def _filtered_archive_pages(
    app: Sphinx,
) -> Generator[tuple[str, dict[str, Any], str], None, None]:
    """Yield only allowed ABlog pages, suppressing all others.

    Imports ABlog's original generator lazily to avoid import-order issues.
    Post redirects (which don't start with ``blog/``) are always allowed.
    """
    from ablog.post import generate_archive_pages  # noqa: PLC0415

    blog_path = getattr(app, "_ablog_blog_path", None)
    if blog_path is None:
        from ablog.blog import Blog  # noqa: PLC0415
        blog_path = Blog(app).blog_path
        app._ablog_blog_path = blog_path

    for page_data in generate_archive_pages(app):
        docname = page_data[0]

        # Always allow pages outside blog/ (e.g. post redirects)
        if not docname.startswith(blog_path):
            yield page_data
            continue

        # Inside blog/: only allow explicitly listed prefixes
        if any(docname.startswith(p) for p in _ALLOWED_PREFIXES):
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
