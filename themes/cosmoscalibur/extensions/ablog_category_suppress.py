"""Customizations for ABlog blog generation.

ABlog auto-generates category listing pages at ``blog/category/{slug}/``.
These pages are suppressed because the site maintains manual category pages
with curated descriptions under ``es/blog/category/`` and
``en/blog/category/``, which provide better SEO and Ads performance than
ABlog's bare post listings.

The suppression works by disconnecting ABlog's ``html-collect-pages``
handler for ``generate_archive_pages`` and replacing it with a filtered
version that skips category-related pages.
"""

from sphinx.application import Sphinx


def _filtered_archive_pages(app):
    """Generate archive pages, skipping category pages.

    Imports ABlog's original generator lazily to avoid import-order issues.
    """
    from ablog.post import generate_archive_pages

    for page_data in generate_archive_pages(app):
        docname = page_data[0]
        if "/category/" in docname or docname.endswith("/category"):
            continue
        yield page_data


def setup(app: Sphinx):
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
