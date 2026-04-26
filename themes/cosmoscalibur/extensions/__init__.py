"""Cosmoscalibur theme extensions — unified event hooks.

Exports the three Sphinx event handlers that ``__init__.py`` connects:

* ``init_sitemap``  — ``builder-inited`` (one-time setup)
* ``page_context``  — ``html-page-context`` (per-page context injection)
* ``post_build``    — ``build-finished`` (all post-processing)
"""

from typing import Any

from sphinx.application import Sphinx

from .ablog_category_suppress import setup as _setup_ablog_suppress
from .context import (
    generate_pygments_css,
    inject_page_context,
)
from .optimizer import (
    post_process_html,
)
from .sitemap import (
    add_html_link,
    create_sitemap,
    init_sitemap,
)

__all__ = [
    "_setup_ablog_suppress",
    "init_sitemap",
    "page_context",
    "post_build",
]


def page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: object,
) -> None:
    """Unified ``html-page-context`` handler.

    Merges three per-page hooks into a single call:
    1. Page language, icon links, analytics injection.
    2. Hreflang alternate URL computation.
    3. Sitemap URL collection.
    """
    inject_page_context(app, pagename, templatename, context, doctree)
    add_html_link(app, pagename, templatename, context, doctree)


def post_build(app: Sphinx, exception: Exception | None) -> None:
    """Unified ``build-finished`` handler.

    Executes all post-processing in optimal order:
    1. Generate Pygments CSS (must precede minification).
    2. Generate sitemap.xml.
    3. Convert images to WebP + update HTML references.
    4. Post-process HTML (lazy, defer, dimensions, prune, minify).
    5. Minify standalone CSS/JS files.
    """
    if exception:
        return

    generate_pygments_css(app)
    create_sitemap(app, exception)
    post_process_html(app, exception)
