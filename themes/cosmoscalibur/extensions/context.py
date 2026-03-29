"""Per-page context injection and Pygments CSS generation.

Merges logic from ``theme_context.py`` (page_lang, icon_links, analytics,
Pygments dark-only CSS) and ``lang_switcher.py`` (hreflang alternate URLs)
into a single module.
"""

import json
from pathlib import Path
from typing import Any

from pygments.formatters import HtmlFormatter
from sphinx.application import Sphinx

# Pygments style — a11y-dark for accessible dark background syntax highlighting
_PYGMENTS_DARK = "a11y-dark"

# Supported site languages for path-prefix detection
_KNOWN_LANGS = {"es", "en"}

# Language mapping for hreflang alternate computation
_LANG_MAP = {"es": ("en", "English"), "en": ("es", "Español")}


def inject_page_context(
    app: Sphinx,
    pagename: str,
    _templatename: str,
    context: dict[str, Any],
    _doctree: object,
) -> None:
    """Inject theme options and hreflang context into each page.

    Handles three concerns in a single per-page call:

    1. **Theme options**: ``icon_links``, ``analytics_id``, ``page_lang``
       derived from the page path prefix.
    2. **Hreflang**: Computes alternate-language URLs for the language
       switcher component and ``<link rel="alternate">`` tags.
    """
    opts = app.config.html_theme_options

    # --- Icon links (JSON string or list) ---
    icon_links = opts.get("icon_links", [])
    if isinstance(icon_links, str):
        icon_links = json.loads(icon_links) if icon_links else []
    context["icon_links"] = icon_links

    # --- Analytics ID ---
    context["analytics_id"] = opts.get("analytics_id", "")

    # --- Per-page language from path prefix ---
    first_segment = pagename.split("/", maxsplit=1)[0]
    default_lang = app.config.language or "es"
    context["page_lang"] = (
        first_segment if first_segment in _KNOWN_LANGS else default_lang
    )

    # --- Hreflang alternate URLs ---
    parts = pagename.split("/")
    if len(parts) > 1 and parts[0] in _LANG_MAP:
        current_lang = parts[0]
        alt_lang, alt_label = _LANG_MAP[current_lang]
        alt_docname = alt_lang + "/" + "/".join(parts[1:])

        if alt_docname in app.env.all_docs:
            context["lang_alt_url"] = context["pathto"](alt_docname)
            context["lang_alt_label"] = alt_label
            context["lang_alt_code"] = alt_lang
            context["lang_current_code"] = current_lang

            base_url = (app.config.html_baseurl or "").rstrip("/")
            alt_uri = app.builder.get_target_uri(alt_docname)
            cur_uri = app.builder.get_target_uri(pagename)
            context["lang_alt_abs_url"] = f"{base_url}/{alt_uri}"
            context["lang_current_abs_url"] = f"{base_url}/{cur_uri}"


def generate_pygments_css(app: Sphinx) -> None:
    """Overwrite pygments.css with dark-only Pygments styles.

    Since the theme only supports dark mode, styles are generated
    without any data-theme or media-query scoping.
    Must run before minification in the ``build-finished`` pipeline.
    """
    if not hasattr(app, "builder") or app.builder is None:
        return

    dark_fmt = HtmlFormatter(style=_PYGMENTS_DARK)

    lines: list[str] = []
    prefix = ".highlight"
    lines.extend(
        f"{prefix} {line}" for line in dark_fmt.get_linenos_style_defs()
    )
    lines.extend(dark_fmt.get_background_style_defs(prefix))
    lines.extend(dark_fmt.get_token_style_defs(prefix))

    out = Path(app.builder.outdir) / "_static" / "pygments.css"
    out.write_text("\n".join(lines), encoding="utf-8")
