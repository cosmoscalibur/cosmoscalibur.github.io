"""Cosmoscalibur Sphinx theme - minimal, fast, WCAG 2.1 AA accessible.

Self-contained theme package. Registers the theme and connects all
custom extension hooks (context injection, sitemap, performance optimizer)
from a single ``setup()`` entry point.
"""

import contextlib
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx

from .extensions import init_sitemap, page_context, post_build
from .extensions import _setup_blog_customization


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the theme and connect all event hooks."""
    app.add_html_theme(
        "cosmoscalibur",
        str(Path(__file__).parent),
    )

    # Theme-opinionated defaults: SVG sprites, no source links, no prev/next
    app.config.fontawesome_included = False
    app.config.post_show_prev_next = False
    app.config.html_show_sourcelink = False
    app.config.html_copy_source = False

    # Sitemap config values
    app.add_config_value("site_url", default=None, rebuild="")
    app.add_config_value(
        "sitemap_url_scheme",
        default="{lang}{version}{link}",
        rebuild="",
    )
    app.add_config_value("sitemap_locales", default=None, rebuild="")
    app.add_config_value("sitemap_filename", default="sitemap.xml", rebuild="")
    app.add_config_value("sitemap_excludes", default=[], rebuild="")

    with contextlib.suppress(BaseException):
        app.add_config_value("html_baseurl", default=None, rebuild="")

    # 3 hooks - one per event type
    app.connect("builder-inited", init_sitemap)
    app.connect("html-page-context", page_context)
    app.connect("build-finished", post_build)

    # Suppress ABlog's auto-generated category pages
    _setup_blog_customization(app)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
