# Cosmoscalibur — Custom Sphinx Theme

Minimal, fast, dark-only Sphinx theme with WCAG 2.1/2.2 AA compliance.
Built for [cosmoscalibur.com](https://www.cosmoscalibur.com), designed to
replace `pydata-sphinx-theme` with zero Bootstrap dependency and full control
over performance and accessibility.

## Theme Options (`html_theme_options`)

All options are optional. Set them in `conf.py`:

```python
html_theme = "cosmoscalibur"
html_theme_path = ["themes"]
html_theme_options = {
    # Layout
    "show_toc_level": 2,          # Heading depth shown in right TOC sidebar

    # Social links (auto-generate icon links in navbar)
    "github_url": "https://github.com/user/",
    "mastodon_url": "https://instance/@user",
    "x_url": "https://x.com/user",
    "facebook_url": "https://facebook.com/user",
    "youtube_url": "https://youtube.com/c/user",
    "linkedin_url": "https://linkedin.com/in/user",

    # Fallback: manual icon links (used if no *_url options are set)
    "icon_links": [
        {"name": "Mastodon", "url": "...", "icon": "mastodon", "rel": "me"},
    ],

    # Google Analytics (gtag.js)
    "analytics_id": "G-XXXXXXXXXX",

    # Google AdSense
    "google_adsense_id": "ca-pub-XXXXXXXXXXXXXXXX",

    # Plausible Analytics
    "plausible_domain": "example.com",
    "plausible_src": "https://plausible.io/js/script.js",  # optional custom

    # PostHog
    "posthog_api_key": "phc_...",
    "posthog_host": "https://us.i.posthog.com",            # optional custom
    "posthog_src": "https://us.i.posthog.com/static/array.js",  # optional
}
```

Setting any analytics/ads option to an empty string (default) disables that
provider — no tracking scripts are rendered during local development.

### Theme defaults set by `setup()`

The theme enforces these Sphinx options regardless of `conf.py` values:

| Option | Value | Rationale |
|---|---|---|
| `fontawesome_included` | `False` | SVG sprite used instead of FA JS |
| `post_show_prev_next` | `False` | Cleaner post layout |
| `html_show_sourcelink` | `False` | Disabled for public sites |
| `html_copy_source` | `False` | No source files in output |

## Bundled Extensions

Three Sphinx event hooks are registered by the theme's `setup()` function.
No separate `extensions` entry is needed in `conf.py`.

### Context Injection (`html-page-context`)

**Module:** `extensions/context.py`

- **Per-page language detection**: Extracts language from the first path
  segment (`es/`, `en/`) and injects `page_lang` into the template context.
- **Icon links**: Parses `icon_links` from theme options (JSON string or
  list) and injects them as a template variable.
- **Analytics ID**: Exposes `analytics_id` for conditional rendering.
- **Hreflang alternates**: Computes alternate-language URLs for
  `<link rel="alternate">` tags and the language switcher component.
- **Pygments CSS**: Generates dark-only `pygments.css` using the `a11y-dark`
  style (overwriting the default dual-mode output).

### Multilingual Sitemap (`builder-inited` + `build-finished`)

**Module:** `extensions/sitemap.py`

Based on `sphinx-sitemap`. Collects page URLs during build and generates
`sitemap.xml` with `<xhtml:link rel="alternate">` entries for each language.

Configured via standard Sphinx config values:

- `html_baseurl` — Required. Base URL for sitemap entries.
- `sitemap_locales` — List of locale codes (e.g., `["es", "en"]`).
- `sitemap_excludes` — URL patterns to exclude.
- `sitemap_filename` — Output filename (default: `sitemap.xml`).

### Performance Optimizer (`build-finished`)

**Module:** `extensions/optimizer.py`

Post-processes the built HTML to improve Core Web Vitals:

| Optimization | Description |
|---|---|
| **WebP conversion** | Converts PNG/JPEG images to WebP (Pillow). Lossless for PNG, quality 85 for JPEG. |
| **Lazy loading** | Adds `loading="lazy"` and `decoding="async"` to below-the-fold images (skips logo and first image). |
| **Script deferral** | Adds `defer` to synchronous Sphinx scripts (`doctools.js`, `sphinx_highlight.js`, etc.). |
| **Image dimensions** | Injects `width`/`height` attributes from file headers (PNG, JPEG, WebP) to prevent layout shifts. |
| **Asset pruning** | Removes `<link>`/`<script>` for CSS/JS not used by the page (e.g., `pygments.css` on pages without code blocks). |
| **HTML/CSS/JS minification** | Minifies all output files using `minify-html`. |

## CSS Architecture

Four stylesheets, loaded in order:

| File | Scope |
|---|---|
| `css/main.css` | CSS custom properties, reset, typography, utilities, reduced-motion |
| `css/content.css` | Sphinx/MyST content (admonitions, code blocks, tables, Cosmoblog cards, sphinx-design, search results) |
| `css/components.css` | Navbar, sidebar, TOC, footer, back-to-top, CSS Grid layout, responsive breakpoints |
| `css/print.css` | Print stylesheet (`@media print`) — hides chrome, black-on-white |

### Dark Theme

The theme is **dark-only**. All color tokens are defined as CSS custom
properties in `:root` (in `main.css`). There is no light mode toggle.
Contrast ratios meet WCAG 2.1 AA:

- Body text: 10.5:1 on background
- Secondary text: 5.3:1
- Accent (links): 6.0:1

### Responsive Design

CSS Grid layout with three responsive breakpoints (in `components.css`):

| Viewport | Columns | Behavior |
|---|---|---|
| `> 1200px` | sidebar + content + TOC | Full 3-column layout |
| `993px – 1200px` | sidebar + content | Right TOC hidden |
| `≤ 992px` | content only | Single column, sidebar/TOC hidden, hamburger menu |

Breakpoints align with Bootstrap `lg` (992px) / `xl` (1200px), matching
`pydata-sphinx-theme` defaults.

Key responsive properties:

- `min-width: 0` on `.content` prevents grid overflow from wide code blocks.
- `overflow-wrap: break-word` handles long URLs and unbreakable strings.
- Tables use `overflow-x: auto` for independent horizontal scrolling.
- `@media (prefers-reduced-motion: reduce)` disables all animations.

### Accessibility (WCAG 2.1/2.2 AA)

- **Skip link** (WCAG 2.4.1): `<a class="skip-link">` before navbar.
- **Focus indicators** (WCAG 2.4.7): 2px accent-colored outline on all
  interactive elements.
- **Semantic HTML5**: `<header>`, `<main>`, `<aside>`, `<nav>`, `<footer>`
  with ARIA roles and labels.
- **Color contrast**: All text ≥ 4.5:1, large text ≥ 3:1.
- **Reduced motion**: Respects `prefers-reduced-motion`.
- **Keyboard navigation**: Hamburger menu toggle with `aria-expanded`.

## JavaScript

Single file: `js/main.js` (~3 KB, vanilla JS, no dependencies).

| Feature | Description |
|---|---|
| Mobile nav toggle | `aria-expanded` hamburger menu |
| Back-to-top button | Shows after 300px scroll, uses `hidden` attribute |
| TOC scroll-spy | Highlights the current section in the right TOC with anchor-lock support |
| Sphinx search init | Calls `Search.init()` if the search results container exists |

## Jinja2 Templates

### Layout

`layout.html` extends `basic/layout.html` and overrides:

- `{% block css %}` — Loads the four theme stylesheets.
- `{% block scripts %}` — Loads `main.js` with `defer`.
- `{% block extrahead %}` — Analytics, AdSense, hreflang tags.
- `{% block content %}` — CSS Grid container with sidebar, main content,
  and TOC sidebar.
- `{% block footer %}` — Footer, back-to-top button, SVG sprite.

### Sphinx Overrides

| Template | Description |
| --- | --- |
| `search.html` | Extends `basic/search.html`, empties `{% block searchbox %}` to remove the redundant inline search form (navbar search is always available) |

### Components (`components/`)

| Template | Description |
|---|---|
| `navbar.html` | Sticky glassmorphism navbar with logo, lang badge, search, hamburger toggle |
| `icon-links.html` | Social icon links (auto-generated from `*_url` options, rendered in footer) |
| `lang-switcher.html` | Language toggle badge (2-letter code: ES/EN, derived from `lang_alt_code`) |
| `search-form.html` | Sphinx search input + button |
| `toc-sidebar.html` | Right-side table of contents |
| `post-byline.html` | Date-only byline (single-author: no author display) |
| `post-discovery.html` | Unified discovery zone: tags + related posts (sidebar on desktop, inline on mobile) |
| `footer.html` | Copyright + social links + "Built with Sphinx and Cosmoblog" |
| `analytics.html` | Conditional GA / Plausible / PostHog / Ads scripts |
| `svg-sprite.html` | Hidden SVG sprite with all icon definitions |

### Blog Sidebar (`cosmoscalibur/recentposts.html`)

Recent posts sidebar widget — shows the 5 most recent posts filtered
by current page language, with a "View all" link to the archive.
Uses `cosmoblog-sidebar-item` class names.

### Internationalization (i18n)

**Module:** `extensions/i18n.py`

All UI strings and admonition titles are translated via JSON locale files.
No language codes are hardcoded in the theme — all language support is
derived dynamically from `blog_languages` in `conf.py`.

#### Locale Files

Translations are stored in `locale/{lang}.json`:

```
themes/cosmoscalibur/
├── locale/
│   ├── es.json          # Built-in Spanish (theme core)
│   └── en.json          # Built-in English (theme core)
```

Each JSON file contains two sections:

1. **UI strings** (top-level keys): Used by the `t()` template helper
   in Jinja2 templates (`{{ t("home") }}`).
2. **Admonitions** (`"admonitions"` key): Maps admonition titles from
   the build output to the correct title for that language. This handles
   both Sphinx standard admonitions (Note, Warning, etc.) and Cosmoblog's
   `update` directive.

#### Adding a Custom Language

1. Create `{confdir}/locale/{lang}.json` (user override) or
   `themes/cosmoscalibur/locale/{lang}.json`:

   ```json
   {
     "home": "Accueil",
     "on_this_page": "Sur cette page",
     "recent_posts": "Articles récents",
     "see_all_posts": "Voir tous les articles →",
     "related_posts": "Articles connexes",
     "built_with": "Construit avec {sphinx} et {cosmoblog}",
     "tagged_with": "Articles étiquetés <strong>{tag}</strong> sur {site}.",
     "draft": "Brouillon",
     "admonitions": {
       "Nota": "Remarque",
       "Advertencia": "Avertissement"
     }
   }
   ```

2. Register the language in `conf.py`:

   ```python
   blog_languages = {
       "es": ("Español", None),
       "en": ("English", None),
       "fr": ("Français", None),
   }
   ```

3. Create content under `fr/` directory.

User-override files at `{confdir}/locale/` take priority over built-in
theme locale files.

#### Template Translation

The `t()` function is injected into every page's Jinja2 context by
`extensions/context.py`. It supports format variables:

```html
{{ t("built_with", sphinx='<a href="...">Sphinx</a>',
     cosmoblog='<a href="...">Cosmoblog</a>') | safe }}
```

#### Admonition Translation

The theme overrides Sphinx's `language` to `"en"` internally (in
`_sync_config`) so all admonition titles come out in English — the
standard i18n base language. The user's actual language (from
`conf.py`) is saved as `blog_default_language` for theme logic.

The `<html lang>` attribute is fixed per-page via `{% set language =
page_lang %}` in `layout.html`, ensuring correct language metadata
for search engines and browsers.

The optimizer post-processes built HTML to translate admonition titles
for non-English pages. Each locale file's `"admonitions"` section maps
English titles to the target language (e.g., `"Note" → "Nota"`).

A trailing space in a key signals **prefix-match** mode. Cosmoblog's
`update` directive generates titles as `_("Updated on ") + date`, so
`"Updated on "` matches any date suffix (e.g., `"Updated on 2024-01-01"
→ "Actualizado el 2024-01-01"`).

> **Note:** `en.json` intentionally omits the `"admonitions"` section.
> Since the theme forces Sphinx to build in English, English admonition
> titles are already correct and need no translation. When adding a new
> language locale file, you **must** include an `"admonitions"` section
> that maps the English titles to the target language — otherwise
> admonition titles on those pages will remain in English.

## Dependencies

The theme requires these Python packages (already in `pyproject.toml`):

| Package | Used by |
|---|---|
| `sphinx>=8.1.3` | Core build system |
| `accessible-pygments>=0.0.5` | `a11y-dark` syntax highlighting style |
| `minify-html>=0.15.0` | HTML/CSS/JS minification (optimizer) |
| `Pillow` (via `matplotlib`) | WebP image conversion (optimizer) |

No frontend dependencies (no Bootstrap, no jQuery, no FontAwesome JS).
All icons are inline SVGs defined in `svg-sprite.html`.
