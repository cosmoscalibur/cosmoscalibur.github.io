"""Cosmoscalibur Sphinx theme - minimal, fast, WCAG 2.1 AA accessible.

Self-contained theme package. Registers the theme and connects all
custom extension hooks (context injection, sitemap, performance optimizer)
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
from .extensions import _setup_ablog_suppress
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
    # ABlog
    app.config.post_show_prev_next = False

    # Sitemap (only user-configurable value)
    app.add_config_value("sitemap_excludes", default=[], rebuild="")

    with contextlib.suppress(BaseException):
        app.add_config_value("html_baseurl", default=None, rebuild="")

    # Event hooks
    app.connect("builder-inited", _sync_config)
    app.connect("builder-inited", init_sitemap)
    app.connect("html-page-context", page_context)
    app.connect("build-finished", post_build)

    # Suppress ABlog's auto-generated category pages
    _setup_ablog_suppress(app)

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
    - ``blog_authors`` ← ``{author.split()[0]: (author, None)}``
    - ``blog_default_author`` ← first key in ``blog_authors``
    - ``blog_default_language`` ← ``language``
    - ``copyright`` ← first post year + current year + ``author``

    URL / sitemap / OGP:
    - ``blog_baseurl`` ← ``html_baseurl``
    - ``ogp_site_url`` ← ``html_baseurl.rstrip("/")``
    - ``ogp_custom_meta_tags`` ← ``x_url`` + ``mastodon_url``

    Opinionated ABlog/MyST defaults:
    - ``post_date_format`` = ``"%Y-%m-%d"``
    - ``post_date_format_short`` = ``"%Y-%m-%d"``
    - ``post_auto_excerpt`` = ``1``
    - ``post_auto_image`` = ``1``
    - ``myst_heading_anchors`` = ``3``
    - ``nb_execution_mode`` = ``"off"``
    - ``nb_render_markdown_format`` = ``"myst"``

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

    # blog_title = project (override ABlog's default "Blog")
    if cfg.project:
        cfg.blog_title = cfg.project

    # blog_authors from author (single-author shortcut)
    if not getattr(cfg, "blog_authors", None) and cfg.author:
        name = cfg.author
        short = name.split()[0] if name else "Author"
        cfg.blog_authors = {short: (name, None)}
        if not getattr(cfg, "blog_default_author", None):
            cfg.blog_default_author = short
    elif getattr(cfg, "blog_authors", None) and not getattr(
        cfg, "blog_default_author", None
    ):
        cfg.blog_default_author = next(iter(cfg.blog_authors))

    # blog_default_language = language
    if not getattr(cfg, "blog_default_language", None) and cfg.language:
        cfg.blog_default_language = cfg.language

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

    # blog_baseurl = html_baseurl
    if not getattr(cfg, "blog_baseurl", None) and cfg.html_baseurl:
        cfg.blog_baseurl = cfg.html_baseurl

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

    # ── Opinionated ABlog defaults ────────────────────────────────

    cfg.post_date_format = "%Y-%m-%d"
    cfg.post_date_format_short = "%Y-%m-%d"
    cfg.post_auto_excerpt = 1
    cfg.post_auto_image = 1



    # ── Project paths ─────────────────────────────────────────────

    if not getattr(cfg, "html_theme_path", None):
        cfg.html_theme_path = ["themes"]
    if not getattr(cfg, "html_static_path", None):
        cfg.html_static_path = ["static"]
    if not getattr(cfg, "html_extra_path", None):
        cfg.html_extra_path = ["files"]
