"""Multilingual sitemap generator for Sphinx.

Based on sphinx-sitemap. Collects page URLs during the ``html-page-context``
event and writes ``sitemap.xml`` at ``build-finished``.

Copyright (c) 2013 Michael Dowling <mtdowling@gmail.com>
Copyright (c) 2017 Jared Dillard <jared.dillard@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
"""

import queue
from collections import defaultdict
from multiprocessing import Manager
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

from sphinx.application import Sphinx
from sphinx.util.logging import getLogger

__version__ = "2.6.0"

logger = getLogger(__name__)


def init_sitemap(app: Sphinx) -> None:
    """Record builder type and initialize the sitemap URL queue.

    Connected to ``builder-inited`` by the theme's ``setup()``.
    """
    builder = getattr(app, "builder", None)
    if builder is None:
        return
    builder.env.is_directory_builder = (
        type(builder).__name__ == "DirectoryHTMLBuilder"
    )
    builder.env.app.sitemap_links = Manager().Queue()


def get_locales(app: Sphinx) -> list[str]:
    """Get configured or autodetected locales for sitemap alternate links."""
    sitemap_locales: list[str] | None = app.builder.config.sitemap_locales
    if sitemap_locales:
        if sitemap_locales == [None]:
            return []
        return list(sitemap_locales)

    locales = []
    for locale_dir_name in app.builder.config.locale_dirs:
        locale_path = Path(app.confdir) / locale_dir_name
        if locale_path.is_dir():
            locales.extend(
                entry.name
                for entry in locale_path.iterdir()
                if entry.is_dir()
            )
    return locales


def hreflang_formatter(lang: str) -> str:
    """Format locale code for hreflang attribute (``_`` to ``-``)."""
    return lang.replace("_", "-") if "_" in lang else lang


def add_html_link(
    app: Sphinx,
    pagename: str,
    _templatename: str,
    _context: dict[str, Any],
    _doctree: object,
) -> None:
    """Collect page URL for sitemap during ``html-page-context``.

    Called by the unified ``page_context`` handler in ``__init__.py``.
    """
    env = app.builder.env
    file_suffix = app.builder.config.html_file_suffix or ".html"

    if env.is_directory_builder:  # type: ignore[attr-defined]
        if pagename == "index":
            sitemap_link = ""
        elif pagename.endswith("/index"):
            sitemap_link = pagename[:-6] + "/"
        else:
            sitemap_link = pagename + "/"
    else:
        sitemap_link = pagename + file_suffix

    if sitemap_link not in app.builder.config.sitemap_excludes and (
        sitemap_link.startswith(("es/", "en/", "blog/category/"))
    ):
        env.app.sitemap_links.put(sitemap_link)  # type: ignore[attr-defined]


def create_sitemap(app: Sphinx, exception: Exception | None) -> None:
    """Generate ``sitemap.xml`` from collected HTML page links.

    Called by the unified ``post_build`` handler in ``__init__.py``.
    """
    if exception:
        return

    site_url = app.builder.config.site_url or app.builder.config.html_baseurl
    if site_url:
        site_url = site_url.rstrip("/") + "/"
    else:
        logger.warning(
            "sitemap: html_baseurl is required in conf.py. "
            "Sitemap not built.",
            type="sitemap",
            subtype="configuration",
        )
        return

    if app.env.app.sitemap_links.empty():  # type: ignore[attr-defined]
        logger.info(
            "sitemap: No pages generated for %s",
            app.config.sitemap_filename,
            type="sitemap",
            subtype="information",
        )
        return

    ElementTree.register_namespace("xhtml", "http://www.w3.org/1999/xhtml")

    root = ElementTree.Element(
        "urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    locales = get_locales(app)
    language = app.builder.config.language or ""

    pages: dict[str, dict[str, str]] = defaultdict(dict)

    while True:
        try:
            link = app.env.app.sitemap_links.get_nowait()  # type: ignore[attr-defined]
        except queue.Empty:
            break

        lang_page = link.removesuffix("/").split("/")
        if (lang := lang_page[0]) in locales:
            pages["/".join(lang_page[1:])].update({lang: link})
        else:
            pages[link].update({language: link})

    for lang_page in pages.values():
        url = ElementTree.SubElement(root, "url")
        ElementTree.SubElement(url, "loc").text = site_url + (
            lang_page[language]
            if language in lang_page
            else next(iter(lang_page.keys()))
        )
        for lang, link in lang_page.items():
            ElementTree.SubElement(
                url,
                "{http://www.w3.org/1999/xhtml}link",
                rel="alternate",
                hreflang=hreflang_formatter(lang),
                href=site_url + link,
            )

    filename = Path(app.outdir) / app.config.sitemap_filename
    ElementTree.ElementTree(root).write(
        filename, xml_declaration=True, encoding="utf-8", method="xml"
    )

    logger.info(
        "sitemap: %s generated for %s in %s",
        app.config.sitemap_filename,
        site_url,
        filename,
        type="sitemap",
        subtype="information",
    )
