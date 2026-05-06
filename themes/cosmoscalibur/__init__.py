"""Cosmoscalibur Sphinx theme - minimal, fast, WCAG 2.1 AA accessible.

Self-contained theme package. Registers the theme and connects all
custom extension hooks (context injection, sitemap, build pipeline)
from a single ``setup()`` entry point.
"""

import contextlib
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from sphinx.application import Sphinx

from .extensions import init_sitemap, page_context, post_build
from .extensions.youtube import setup as _setup_youtube


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the theme and connect all event hooks."""
    app.add_html_theme(
        "cosmoscalibur",
        str(Path(__file__).parent),
    )

    # --- Theme-opinionated defaults (not user-configurable) ---
    # Sphinx
    app.config.fontawesome_included = False
    app.config.html_show_sourcelink = False
    app.config.html_copy_source = False

    # Sitemap (only user-configurable value)
    app.add_config_value("sitemap_excludes", default=[], rebuild="")

    with contextlib.suppress(BaseException):
        app.add_config_value("html_baseurl", default=None, rebuild="")

    # Event hooks
    app.connect("builder-inited", _sync_config)
    app.connect("builder-inited", init_sitemap)
    app.connect("html-page-context", page_context)
    app.connect("build-finished", post_build)

    # Built-in YouTube directive (replaces sphinxcontrib-youtube)
    _setup_youtube(app)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def _sync_config(app: Sphinx) -> None:
    """Auto-derive config values from existing settings.

    Runs on ``builder-inited`` (after ``conf.py`` is fully loaded) to
    reduce redundant configuration in the user's ``conf.py``.

    Identity (single-author focus):
    - ``html_title`` ← ``project``
    - ``blog_title`` ← ``html_title``
    - ``blog_default_language`` ← ``language``
    - ``copyright`` ← first post year + current year + ``author``

    URL / sitemap / OGP:
    - ``ogp_site_url`` ← ``html_baseurl.rstrip("/")``
    - ``ogp_custom_meta_tags`` ← ``x_url`` + ``mastodon_url``

    Project paths:
    - ``html_theme_path`` = ``["themes"]``
    - ``html_static_path`` = ``["static"]``
    - ``html_extra_path`` = ``["files"]``
    """
    cfg = app.config

    # ── Identity ──────────────────────────────────────────────────

    # html_title = project (Sphinx adds 'X documentation' suffix by default)
    if cfg.project:
        cfg.html_title = cfg.project

    # blog_default_language = language (original, before we force English)
    original_lang = cfg.language or "es"
    if not getattr(cfg, "blog_default_language", None):
        cfg.blog_default_language = original_lang

    # Force Sphinx to build with English internally so admonitions
    # come out in English (standard i18n base).  The theme fixes
    # <html lang> per-page and handles all translations via t()
    # and admonition post-processing.
    cfg.language = "en"

    # copyright = "{first_post_year}-{current_year}, {author}"
    if not cfg.copyright and cfg.author:
        confdir = Path(app.confdir)
        years = {
            int(d.name)
            for d in confdir.glob("*/blog/*/")
            if d.is_dir() and re.match(r"^\d{4}$", d.name)
        }
        if years:
            start = min(years)
            now = datetime.now(tz=UTC).year
            cfg.copyright = f"{start}-{now}, {cfg.author}"

    # ── URL / sitemap / OGP ───────────────────────────────────────

    # ogp_site_url = html_baseurl (without trailing slash)
    if not getattr(cfg, "ogp_site_url", None) and cfg.html_baseurl:
        cfg.ogp_site_url = cfg.html_baseurl.rstrip("/")

    # ogp_custom_meta_tags from social URLs in theme options
    if not getattr(cfg, "ogp_custom_meta_tags", None):
        theme_opts = cfg.html_theme_options or {}
        tags = []
        x_url = theme_opts.get("x_url", "")
        if x_url:
            handle = "@" + x_url.rstrip("/").split("/")[-1]
            tags.append(f'<meta name="twitter:creator" content="{handle}" />')
        mastodon_url = theme_opts.get("mastodon_url", "")
        if mastodon_url:
            parsed = urlparse(mastodon_url)
            user = parsed.path.lstrip("/@")
            fedi = f"@{user}@{parsed.hostname}"
            tags.append(
                f'<meta name="fediverse:creator" content="{fedi}" />'
            )
        if tags:
            cfg.ogp_custom_meta_tags = tags

    # ── Project paths ─────────────────────────────────────────────

    if not getattr(cfg, "html_theme_path", None):
        cfg.html_theme_path = ["themes"]
    if not getattr(cfg, "html_static_path", None):
        cfg.html_static_path = ["static"]
    if not getattr(cfg, "html_extra_path", None):
        cfg.html_extra_path = ["files"]
