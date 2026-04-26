"""Per-page context injection and Pygments CSS generation.

Merges logic from ``theme_context.py`` (page_lang, icon_links, analytics,
Pygments dark-only CSS) and ``lang_switcher.py`` (hreflang alternate URLs)
into a single module.
"""

import json
import re
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

# Pattern to match manual category pages: {lang}/blog/category/{slug}
_CATEGORY_RE = re.compile(r"^(es|en)/blog/category/[^/]+$")

# Regex to extract :category: value from postlist directives in .md files
_CATEGORY_DIRECTIVE_RE = re.compile(r":category:\s*(.+)")

# Build-time cache for category name → manual page docname mapping
# Keyed by (lang, docname) → ablog_category_name
_category_map_cache: dict[str, dict[str, str]] | None = None


def _build_category_page_map(app: Sphinx) -> dict[str, dict[str, str]]:
    """Build a mapping of {lang: {ablog_category_name: docname}}.

    Reads source files of manual category pages to extract the ``:category:``
    value from ``postlist`` directives. Cached for the entire build.
    """
    global _category_map_cache
    if _category_map_cache is not None:
        return _category_map_cache

    result: dict[str, dict[str, str]] = {}
    srcdir = Path(app.srcdir)

    for docname in app.env.all_docs:
        if not _CATEGORY_RE.match(docname):
            continue
        lang = docname.split("/", maxsplit=1)[0]
        # Try to read the source file (.md or .rst)
        for ext in (".md", ".rst"):
            src_file = srcdir / (docname + ext)
            if src_file.exists():
                try:
                    content = src_file.read_text(encoding="utf-8")
                except OSError:
                    continue
                match = _CATEGORY_DIRECTIVE_RE.search(content)
                if match:
                    cat_name = match.group(1).strip()
                    result.setdefault(lang, {})[cat_name] = docname
                break

    _category_map_cache = result
    return result


def inject_page_context(
    app: Sphinx,
    pagename: str,
    _templatename: str,
    context: dict[str, Any],
    _doctree: object,
) -> None:
    """Inject theme options, hreflang, and category links into each page.

    Handles four concerns in a single per-page call:

    1. **Theme options**: ``icon_links``, ``analytics_id``, ``page_lang``
       derived from the page path prefix.
    2. **Hreflang**: Computes alternate-language URLs for the language
       switcher component and ``<link rel="alternate">`` tags.
    3. **Category links**: Scans ``all_docs`` for manual category pages
       matching the current language and reads their titles from
       ``env.titles`` for the navbar navigation.
    4. **Category page map**: Maps ABlog category names to manual category
       page URLs for the related posts sidebar links.
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
    page_lang = (
        first_segment if first_segment in _KNOWN_LANGS else default_lang
    )
    context["page_lang"] = page_lang

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

    # --- Category navigation links ---
    prefix = f"{page_lang}/blog/category/"
    cat_links = []
    for docname in app.env.all_docs:
        if not _CATEGORY_RE.match(docname):
            continue
        if not docname.startswith(prefix):
            continue
        title_node = app.env.titles.get(docname)
        if title_node is None:
            continue
        label = title_node.astext()
        # Strip common prefixes/suffixes to show short category names
        # e.g. "Artículos sobre ciencia" → "Ciencia", "Linux articles" → "Linux"
        if label.startswith("Artículos sobre "):
            label = label[len("Artículos sobre "):]
        elif label.endswith(" articles"):
            label = label[: -len(" articles")]
        label = label[0].upper() + label[1:] if label else label
        cat_links.append({
            "url": context["pathto"](docname),
            "label": label,
        })
    cat_links.sort(key=lambda c: c["label"])
    context["category_links"] = cat_links

    # --- Category page map (ABlog category name → URL) ---
    cat_map = _build_category_page_map(app)
    lang_map = cat_map.get(page_lang, {})
    context["category_page_map"] = {
        name: context["pathto"](docname)
        for name, docname in lang_map.items()
    }


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
