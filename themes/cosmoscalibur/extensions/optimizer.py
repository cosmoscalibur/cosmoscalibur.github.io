"""Performance optimizer — post-build HTML processing and image conversion.

Post-processes built HTML to improve Core Web Vitals:

1. Converts PNG/JPEG images to WebP format (Pillow, no new dependency).
2. Adds ``loading="lazy"`` and ``decoding="async"`` to below-the-fold images.
3. Adds ``defer`` to Sphinx's synchronous ``<script>`` tags in ``<head>``.
4. Adds explicit ``width``/``height`` to ``<img>`` tags from local images.
5. Prunes unused CSS/JS ``<link>``/``<script>`` on pages that don't need them.
6. Minifies all HTML, CSS, and JS files using ``minify-html``.
"""

from pathlib import Path
import re

import minify_html
from PIL import Image
from sphinx.application import Sphinx
from sphinx.util.logging import getLogger

logger = getLogger(__name__)

# Sphinx scripts that load synchronously in <head> and can be safely deferred
_DEFERRABLE_SCRIPTS = {
    "documentation_options.js",
    "doctools.js",
    "sphinx_highlight.js",
    "clipboard.min.js",
    "copybutton.js",
    "translations.js",
}

# Conservative minify-html configuration — safe for all browsers
_MINIFY_CFG = {
    "minify_css": True,
    "minify_js": True,
    "keep_closing_tags": True,
    "keep_html_and_head_opening_tags": True,
    "minify_doctype": True,
}

# CSS/JS files that can be conditionally removed from pages.
# Each entry maps a filename substring to HTML markers that indicate usage.
_PRUNABLE_ASSETS = {
    "mystnb.": {"cell_input", "cell_output", "nb-cell", "cell tag_"},
    "sphinx-design.min.css": {"sd-tab-set", "sd-card", "sd-dropdown", "sd-col"},
    "pygments.css": {'class="highlight'},
}

# CSS files to always remove (redundant with theme dark-only pygments.css)
_ALWAYS_REMOVE = {"pygments_dark.css", "basic.css"}

# Image extensions eligible for WebP conversion
_CONVERTIBLE_EXTS = {".png", ".jpg", ".jpeg"}

# JPEG marker byte for image dimension parsing
_JPEG_MARKER = 0xFF


def post_process_html(app: Sphinx, exception: Exception | None) -> None:
    """Unified ``build-finished`` handler for all HTML optimizations.

    Called by the theme's ``post_build`` pipeline after pygments CSS
    generation and sitemap creation. Execution order:

    1. Convert images to WebP.
    2. Post-process HTML (lazy, defer, dimensions, prune, reference update).
    3. Minify HTML.
    4. Minify standalone CSS/JS files.
    """
    if exception:
        return

    outdir = Path(app.outdir)

    # --- 1. Convert images to WebP ---
    webp_count, webp_saved = _convert_images_to_webp(outdir)

    # --- 2-5. Post-process HTML files ---
    html_files = list(outdir.rglob("*.html"))
    lazy_count, defer_count, dim_count, prune_count, html_bytes_saved = (
        _process_html_files(html_files, webp_count)
    )

    # --- 4. Minify standalone CSS/JS files ---
    static_files, static_bytes = _minify_static_files(outdir)

    total_saved = html_bytes_saved + static_bytes + webp_saved
    logger.info(
        "optimizer: lazy=%d, defer=%d, dimensions=%d, pruned=%d refs, "
        "minified=%d static, webp=%d images, "
        "saved=%.1f KB (html=%.1f, static=%.1f, webp=%.1f)",
        lazy_count,
        defer_count,
        dim_count,
        prune_count,
        static_files,
        webp_count,
        total_saved / 1024,
        html_bytes_saved / 1024,
        static_bytes / 1024,
        webp_saved / 1024,
        type="optimizer",
        subtype="information",
    )

    # --- 5. Copy 404/index.html → 404.html for GitHub Pages ---
    # The dirhtml builder outputs 404/index.html, but GitHub Pages
    # requires 404.html at the site root to serve custom 404 pages.
    _copy_404_page(outdir)

    # --- 6. Delete always-removed CSS files from _static ---
    for filename in _ALWAYS_REMOVE:
        dead = outdir / "_static" / filename
        if dead.exists():
            dead.unlink()


def _copy_404_page(outdir: Path) -> None:
    """Copy ``404/index.html`` to ``404.html`` at the output root.

    The ``dirhtml`` builder generates ``404/index.html``, but GitHub Pages
    requires ``404.html`` at the site root to serve custom error pages.
    This copies the file after all optimizations have been applied.
    """
    import shutil

    src = outdir / "404" / "index.html"
    dst = outdir / "404.html"
    if src.is_file():
        shutil.copy2(src, dst)
        logger.info(
            "optimizer: copied 404/index.html → 404.html",
            type="optimizer",
            subtype="information",
        )


def _process_html_files(
    html_files: list[Path],
    webp_count: int,
) -> tuple[int, int, int, int, int]:
    """Apply lazy loading, defer, dimensions, pruning, and minification.

    Returns ``(lazy_count, defer_count, dim_count, prune_count, bytes_saved)``.
    """
    lazy_count = 0
    defer_count = 0
    dim_count = 0
    prune_count = 0
    html_bytes_saved = 0

    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8")
        original = content
        original_size = len(content.encode("utf-8"))

        content, had_lazy = _add_lazy_loading(content)

        new_content = _defer_sphinx_scripts(content)
        if new_content != content:
            defer_count += 1
            content = new_content

        html_dir = html_file.parent
        new_content = _add_image_dimensions(content, html_dir)
        if new_content != content:
            dim_count += 1
            content = new_content

        new_content, pruned = _prune_unused_assets(content)
        if pruned > 0:
            prune_count += pruned
            content = new_content

        if webp_count > 0:
            content = _update_image_references(content)

        try:
            content = minify_html.minify(content, **_MINIFY_CFG)
        except Exception:
            logger.debug(
                "optimizer: skipped HTML minification for %s",
                html_file,
                type="optimizer",
                subtype="debug",
            )

        if content != original:
            html_file.write_text(content, encoding="utf-8")
            html_bytes_saved += original_size - len(content.encode("utf-8"))
            if had_lazy:
                lazy_count += 1

    return lazy_count, defer_count, dim_count, prune_count, html_bytes_saved


def _add_lazy_loading(content: str) -> tuple[str, bool]:
    """Add ``loading="lazy"`` to below-the-fold images.

    Skips the site logo and the first content image.
    Returns ``(modified_content, had_lazy_images)``.
    """
    skip_count = 0
    pattern = re.compile(
        r"<img(?![^>]*loading=)([^>]*?)(/?)\/>",
        re.IGNORECASE,
    )

    def _replacer(match: re.Match[str]) -> str:
        nonlocal skip_count
        img_attrs = match.group(1)
        closing = match.group(2)
        if "cosmoscalibur_logo" in img_attrs:
            return match.group(0)
        if skip_count == 0:
            skip_count += 1
            return match.group(0)
        return f'<img loading="lazy" decoding="async"{img_attrs}{closing}>'

    result = pattern.sub(_replacer, content)
    return result, skip_count > 0


# ── WebP conversion ──────────────────────────────────────────────────────


def _convert_images_to_webp(outdir: Path) -> tuple[int, int]:
    """Convert PNG/JPEG images to WebP, reusing existing conversions.

    Skips conversion when a ``.webp`` file already exists and is at least
    as recent as the source. Handles shared images between language versions
    (Sphinx copies to a single ``_images/`` directory).

    Returns a tuple of (files_converted, bytes_saved).
    """
    images_dir = outdir / "_images"
    if not images_dir.is_dir():
        return 0, 0

    converted = 0
    bytes_saved = 0

    for img_path in list(images_dir.iterdir()):
        if img_path.suffix.lower() not in _CONVERTIBLE_EXTS:
            continue

        webp_path = img_path.with_suffix(".webp")

        # Reuse already-converted files (from previous build or same build)
        if (
            webp_path.exists()
            and webp_path.stat().st_mtime >= img_path.stat().st_mtime
        ):
            original_size = img_path.stat().st_size
            bytes_saved += original_size - webp_path.stat().st_size
            img_path.unlink()
            converted += 1
            continue

        original_size = img_path.stat().st_size
        is_lossless = img_path.suffix.lower() == ".png"

        try:
            with Image.open(img_path) as img:
                if img.mode in ("RGBA", "P"):
                    save_img = img.convert("RGBA")
                else:
                    save_img = img.convert("RGB")

                save_img.save(
                    webp_path,
                    "WEBP",
                    lossless=is_lossless,
                    quality=85,
                    method=6,
                )

            webp_size = webp_path.stat().st_size
            bytes_saved += original_size - webp_size
            converted += 1
            img_path.unlink()
        except Exception:
            logger.debug(
                "optimizer: skipped WebP conversion for %s",
                img_path,
                type="optimizer",
                subtype="debug",
            )

    return converted, bytes_saved


def _update_image_references(content: str) -> str:
    """Replace image file extensions in HTML for converted ``_images/`` files.

    Only rewrites paths containing ``_images/`` to avoid breaking
    references to logos, favicons, and other static assets.
    """
    return re.sub(
        r'(_images/[^"]*)\.(png|jpe?g)',
        r"\1.webp",
        content,
    )


# ── Lazy loading, defer, dimensions ──────────────────────────────────────


def _add_image_dimensions(content: str, html_dir: Path) -> str:
    """Add width and height attributes to local images missing dimensions.

    Only processes images whose ``src`` points to a local file within
    the build output directory (``_static/``, ``_images/``, etc.).
    """
    img_pattern = re.compile(
        r'<img(?![^>]*width=)([^>]*?)src="([^"]+)"([^>]*?)(/?)\>',
        re.IGNORECASE,
    )

    def _dimension_replacer(match: re.Match[str]) -> str:
        pre_src = match.group(1)
        src = match.group(2)
        post_src = match.group(3)
        closing = match.group(4)

        if src.startswith(("http://", "https://", "data:", "//")):
            return match.group(0)

        img_path = html_dir / src
        if not img_path.is_file():
            return match.group(0)

        try:
            width, height = _get_image_size(img_path)
            if width and height:
                return (
                    f'<img{pre_src}src="{src}"{post_src}'
                    f' width="{width}" height="{height}"{closing}>'
                )
        except (OSError, ValueError):
            pass

        return match.group(0)

    return img_pattern.sub(_dimension_replacer, content)


def _get_image_size(path: Path) -> tuple[int | None, int | None]:
    """Read image dimensions from file header without external dependencies.

    Supports PNG, JPEG, and WebP formats.
    """
    data = path.read_bytes()

    # PNG: width and height at bytes 16-23 in the IHDR chunk
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        width = int.from_bytes(data[16:20], "big")
        height = int.from_bytes(data[20:24], "big")
        return width, height

    # JPEG: scan for SOF0 marker (0xFFC0)
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data) - 9:
            if data[i] != _JPEG_MARKER:
                break
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                height = int.from_bytes(data[i + 5 : i + 7], "big")
                width = int.from_bytes(data[i + 7 : i + 9], "big")
                return width, height
            length = int.from_bytes(data[i + 2 : i + 4], "big")
            i += 2 + length

    # WebP: RIFF header, width/height at bytes 26-29
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        if data[12:16] == b"VP8 ":
            # Lossy WebP
            width = int.from_bytes(data[26:28], "little") & 0x3FFF
            height = int.from_bytes(data[28:30], "little") & 0x3FFF
            return width, height
        if data[12:16] == b"VP8L":
            # Lossless WebP
            bits = int.from_bytes(data[21:25], "little")
            width = (bits & 0x3FFF) + 1
            height = ((bits >> 14) & 0x3FFF) + 1
            return width, height

    return None, None


def _defer_sphinx_scripts(content: str) -> str:
    """Add ``defer`` attribute to synchronous Sphinx scripts in ``<head>``."""
    for script_name in _DEFERRABLE_SCRIPTS:
        pattern = re.compile(
            rf'<script(?!\s+defer)(\s+src="[^"]*{re.escape(script_name)}[^"]*")>',
            re.IGNORECASE,
        )
        content = pattern.sub(r"<script defer\1>", content)
    return content


# ── CSS/JS pruning ───────────────────────────────────────────────────────


def _prune_unused_assets(content: str) -> tuple[str, int]:
    """Remove ``<link>``/``<script>`` for CSS/JS not used by the page."""
    pruned = 0

    for filename in _ALWAYS_REMOVE:
        pattern = re.compile(
            rf'<link[^>]*href="[^"]*{re.escape(filename)}[^"]*"[^>]*/?>',
            re.IGNORECASE,
        )
        new_content = pattern.sub("", content)
        if new_content != content:
            pruned += 1
            content = new_content

    for filename_substr, markers in _PRUNABLE_ASSETS.items():
        page_uses_asset = any(marker in content for marker in markers)
        if not page_uses_asset:
            css_pattern = re.compile(
                rf'<link[^>]*href="[^"]*{re.escape(filename_substr)}[^"]*"[^>]*/?>',
                re.IGNORECASE,
            )
            new_content = css_pattern.sub("", content)

            js_pattern = re.compile(
                rf'<script[^>]*src="[^"]*{re.escape(filename_substr)}[^"]*"[^>]*>'
                r"</script>",
                re.IGNORECASE,
            )
            new_content = js_pattern.sub("", new_content)

            if new_content != content:
                pruned += 1
                content = new_content

    return content, pruned


# ── Static file minification ─────────────────────────────────────────────


def _minify_static_files(outdir: Path) -> tuple[int, int]:
    """Minify standalone CSS and JS files in ``_static/``.

    Returns a tuple of (files_minified, bytes_saved).
    """
    static_dir = outdir / "_static"
    if not static_dir.is_dir():
        return 0, 0

    files_minified = 0
    bytes_saved = 0

    for filepath in static_dir.rglob("*"):
        if not filepath.is_file():
            continue
        if filepath.suffix not in (".css", ".js"):
            continue

        original = filepath.read_text(encoding="utf-8")
        original_size = len(original.encode("utf-8"))

        suffix = filepath.suffix
        if suffix == ".css":
            wrapped = f"<style>{original}</style>"
        else:
            wrapped = f"<script>{original}</script>"

        try:
            minified_wrapped = minify_html.minify(
                wrapped,
                minify_css=True,
                minify_js=True,
            )
            if suffix == ".css":
                minified = minified_wrapped[7:-8]
            else:
                minified = minified_wrapped[8:-9]

            minified_size = len(minified.encode("utf-8"))
            saved = original_size - minified_size

            if saved > 0:
                filepath.write_text(minified, encoding="utf-8")
                files_minified += 1
                bytes_saved += saved
        except Exception:
            logger.debug(
                "optimizer: skipped minification for %s",
                filepath,
                type="optimizer",
                subtype="debug",
            )

    return files_minified, bytes_saved
