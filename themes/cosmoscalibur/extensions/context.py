"""Per-page context injection and Pygments CSS generation.

Merges logic from ``theme_context.py`` (page_lang, icon_links, analytics,
Pygments dark-only CSS) and ``lang_switcher.py`` (hreflang alternate URLs)
into a single module.
"""

import functools
import json
from pathlib import Path
import re
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


# ---------------------------------------------------------------------------
# Helpers — each handles a single concern for inject_page_context
# ---------------------------------------------------------------------------


def _resolve_archive_url(
    page_lang: str,
    app: Sphinx,
    context: dict[str, Any],
) -> None:
    """Set ``archive_url`` to the language-specific archive page."""
    archive_docname = f"{page_lang}/blog/archive"
    if archive_docname in app.env.all_docs:
        context["archive_url"] = context["pathto"](archive_docname)
    else:
        context["archive_url"] = context["pathto"]("blog")


def _resolve_home_url(
    page_lang: str,
    default_lang: str,
    context: dict[str, Any],
) -> None:
    """Set ``home_url`` to the root-relative language-specific index."""
    if page_lang == default_lang:
        context["home_url"] = "/"
    else:
        context["home_url"] = f"/{page_lang}/"


def _resolve_hreflang(
    pagename: str,
    default_lang: str,
    app: Sphinx,
    context: dict[str, Any],
) -> None:
    """Set ``lang_alt_*`` and ``lang_current_*`` context variables.

    Handles three cases:
    - Pages under a language prefix (``es/…``, ``en/…``).
    - Non-default language index → links to root index.
    - Root index → links to non-default language index.
    """

    def _set(
        alt_docname: str, current_lang: str, alt_lang: str, alt_label: str,
    ) -> None:
        context["lang_alt_url"] = context["pathto"](alt_docname)
        context["lang_alt_label"] = alt_label
        context["lang_alt_code"] = alt_lang
        context["lang_current_code"] = current_lang

        base_url = (app.config.html_baseurl or "").rstrip("/")
        alt_uri = app.builder.get_target_uri(alt_docname)
        cur_uri = app.builder.get_target_uri(pagename)
        context["lang_alt_abs_url"] = f"{base_url}/{alt_uri}"
        context["lang_current_abs_url"] = f"{base_url}/{cur_uri}"

    parts = pagename.split("/")

    if len(parts) > 1 and parts[0] in _LANG_MAP:
        current_lang = parts[0]
        rest = "/".join(parts[1:])

        # Non-default lang index → alternate is root index
        if rest == "index" and current_lang != default_lang:
            alt_docname = "index"
            alt_lang = default_lang
            alt_label = _LANG_MAP[current_lang][1]
        else:
            alt_lang, alt_label = _LANG_MAP[current_lang]
            alt_docname = alt_lang + "/" + rest

        if alt_docname in app.env.all_docs:
            _set(alt_docname, current_lang, alt_lang, alt_label)

    elif pagename == "index":
        # Root index → alternate is each non-default language index
        blog_languages = app.config.blog_languages or {}
        for lang_code in _KNOWN_LANGS:
            if lang_code == default_lang:
                continue
            alt_docname = f"{lang_code}/index"
            if alt_docname in app.env.all_docs:
                lang_name = blog_languages.get(
                    lang_code, (lang_code, None),
                )[0]
                _set(alt_docname, default_lang, lang_code, lang_name)
                break  # only one alternate for now


def _resolve_category_links(
    page_lang: str,
    app: Sphinx,
    context: dict[str, Any],
) -> None:
    """Set ``category_links`` (navbar) and ``category_page_map`` (sidebar)."""
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
        cat_links.append({
            "url": context["pathto"](docname),
            "label": label,
        })
    cat_links.sort(key=lambda c: c["label"])
    context["category_links"] = cat_links

    # Category page map (ABlog category name → URL)
    cat_map = _build_category_page_map(app)
    lang_map = cat_map.get(page_lang, {})
    context["category_page_map"] = {
        name: context["pathto"](docname)
        for name, docname in lang_map.items()
    }


@functools.lru_cache(maxsize=1)
def _build_category_page_map(app: Sphinx) -> dict[str, dict[str, str]]:
    """Build a mapping of {lang: {ablog_category_name: docname}}.

    Reads source files of manual category pages to extract the ``:category:``
    value from ``postlist`` directives. Cached for the entire build via
    ``lru_cache`` (the ``app`` reference is stable within a single build).
    """
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

    return result


# ---------------------------------------------------------------------------
# Main entry points
# ---------------------------------------------------------------------------


def _resolve_json_ld(
    pagename: str,
    page_lang: str,
    app: Sphinx,
    context: dict[str, Any],
) -> None:
    """Inject JSON-LD structured data into the page context."""
    base_url = (app.config.html_baseurl or "").rstrip("/")
    if not base_url:
        return

    page_url = f"{base_url}/{app.builder.get_target_uri(pagename)}"
    schemas = []

    # 1. BreadcrumbList
    crumbs = []
    # Home
    home_label = "Inicio" if page_lang == "es" else "Home"
    home_url = f"{base_url}/" if page_lang == "es" else f"{base_url}/en/"
    crumbs.append({"name": home_label, "item": home_url})

    # Middle crumbs (Category)
    post = None
    if hasattr(app.env, "ablog_posts") and pagename in app.env.ablog_posts:
        posts = app.env.ablog_posts[pagename]
        if posts:
            post = posts[0]
            categories = post.get("category", [])
            if categories:
                # Use first category for breadcrumb
                cat = categories[0]
                cat_doc = f"{page_lang}/blog/category/{cat}"
                if cat_doc in app.env.all_docs:
                    cat_name = app.env.titles[cat_doc].astext()
                    cat_url = f"{base_url}/{app.builder.get_target_uri(cat_doc)}"
                    crumbs.append({"name": cat_name, "item": cat_url})

    # Current page
    crumbs.append({"name": context.get("title", ""), "item": page_url})

    schemas.append({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": c["name"],
                "item": c["item"]
            } for i, c in enumerate(crumbs)
        ]
    })

    # 2. Article (only for blog posts)
    if post:
        # Get dates
        pub_date = post.get("date")
        # ABlog's 'update' is the max of pub and all update directives
        mod_date = post.get("update") or pub_date
        
        # Site-wide defaults (no hardcoded fallbacks per user request)
        site_author = app.config.author
        site_project = app.config.project
        
        # Resolve specific author (falls back to site author)
        author_name = site_author
        if author := post.get("author"):
            if isinstance(author, list) and author:
                author_name = author[0]
            elif isinstance(author, str):
                author_name = author

        # Logo resolution from configuration
        logo_rel_path = app.config.html_logo
        if not logo_rel_path:
            # Skip logo if not configured, or let the rest of the logic handle it
            logo_url = None
        else:
            logo_filename = Path(logo_rel_path).name
            logo_url = f"{base_url}/_static/{logo_filename}"

        publisher = {
            # Preferring Organization for the publisher establishes the 
            # blog as a formal entity/brand, improving E-E-A-T signals.
            "@type": "Organization",
            "name": site_project,
        }
        if logo_url:
            publisher["logo"] = {
                "@type": "ImageObject",
                "url": logo_url
            }

        article = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": context.get("title", ""),
            "datePublished": pub_date.isoformat() if pub_date else None,
            "dateModified": mod_date.isoformat() if mod_date else None,
            "author": {
                "@type": "Person",
                "name": author_name,
                "url": f"{base_url}/me/" if page_lang == "es" else f"{base_url}/en/me/"
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": page_url
            },
            "publisher": publisher
        }
        
        # Add description if available
        if desc := context.get("description"):
            article["description"] = desc
            
        # Add image if available (OpenGraph image is a good candidate)
        if og_image := context.get("og_image"):
            article["image"] = og_image

        schemas.append(article)

    context["json_ld"] = json.dumps(schemas, ensure_ascii=False)


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
    5. **JSON-LD**: Injects structured data for SEO (Articles, Breadcrumbs).
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

    # --- Delegate to helpers ---
    _resolve_archive_url(page_lang, app, context)
    _resolve_home_url(page_lang, default_lang, context)
    _resolve_hreflang(pagename, default_lang, app, context)
    _resolve_category_links(page_lang, app, context)
    _resolve_json_ld(pagename, page_lang, app, context)

    # --- Copyright split for linked author name ---

    # --- Copyright split for linked author name ---
    copyright_str = app.config.copyright or ""
    if ", " in copyright_str:
        year_part, author_part = copyright_str.split(", ", maxsplit=1)
    else:
        year_part, author_part = copyright_str, ""
    context["copyright_year"] = year_part
    context["copyright_author"] = author_part


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
