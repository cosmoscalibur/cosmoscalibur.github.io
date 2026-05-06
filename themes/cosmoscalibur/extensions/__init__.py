"""Cosmoscalibur theme extensions — unified event hooks.

Exports the three Sphinx event handlers that ``__init__.py`` connects:

* ``init_sitemap``  — ``builder-inited`` (one-time setup)
* ``page_context``  — ``html-page-context`` (per-page context injection)
* ``post_build``    — ``build-finished`` (all post-build operations)
"""

from pathlib import Path
import shutil
from typing import Any

from sphinx.application import Sphinx
from sphinx.util.logging import getLogger

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

logger = getLogger(__name__)

__all__ = [
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

    Executes all post-build operations in optimal order:
    1. Generate Pygments CSS (must precede minification).
    2. Generate sitemap.xml.
    3. Optimize HTML (WebP, defer, prune, i18n, minify).
    4. Copy 404 page for GitHub Pages deployment.
    5. Remove unused Sphinx search files.
    """
    if exception:
        return

    generate_pygments_css(app)
    create_sitemap(app, exception)
    post_process_html(app, exception)

    outdir = Path(app.outdir)

    # --- 404 page: GitHub Pages requires 404.html at site root ---
    _move_404_page(outdir)

    # --- Remove Sphinx search files (search uses Google redirect) ---
    for search_file in ("searchindex.js",
                        "_static/searchtools.js",
                        "_static/language_data.js"):
        path = outdir / search_file
        if path.exists():
            path.unlink()


def _move_404_page(outdir: Path) -> None:
    """Move ``404/index.html`` to ``404.html`` at the output root.

    The ``dirhtml`` builder generates ``404/index.html``, but GitHub Pages
    requires ``404.html`` at the site root to serve custom error pages.
    The directory version is useless (404 is a server response, not a
    navigable URL), so we move instead of copy.
    """
    src = outdir / "404" / "index.html"
    dst = outdir / "404.html"
    if src.is_file():
        shutil.move(src, dst)
        src.parent.rmdir()
        logger.info(
            "post_build: moved 404/index.html -> 404.html",
            type="post_build",
            subtype="information",
        )
