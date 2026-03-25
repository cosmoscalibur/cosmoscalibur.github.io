"""Performance optimizer extension for Sphinx.

Post-processes built HTML to improve Core Web Vitals:
1. Adds ``loading="lazy"`` and ``decoding="async"`` to below-the-fold images.
2. Adds ``defer`` to Sphinx's synchronous ``<script>`` tags in ``<head>``.
3. Adds explicit ``width``/``height`` to ``<img>`` tags from local images.
"""

import re
from pathlib import Path
from typing import Any

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


def setup(app: Sphinx) -> dict[str, Any]:
    """Register the build-finished event for HTML post-processing."""
    app.connect("build-finished", _post_process_html)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def _add_image_dimensions(content: str, html_dir: Path) -> str:
    """Add width and height attributes to local images missing dimensions.

    Only processes images whose ``src`` points to a local file within
    the build output directory (``_static/``, ``_images/``, etc.).
    """
    img_pattern = re.compile(
        r'<img(?![^>]*width=)([^>]*?)src="([^"]+)"([^>]*?)(/?)>',
        re.IGNORECASE,
    )

    def _dimension_replacer(match: re.Match[str]) -> str:
        pre_src = match.group(1)
        src = match.group(2)
        post_src = match.group(3)
        closing = match.group(4)

        # Only process local images (relative paths)
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

    Supports PNG and JPEG formats which cover the blog's image assets.
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
            if data[i] != 0xFF:
                break
            marker = data[i + 1]
            # SOF0, SOF1, SOF2 markers contain dimensions
            if marker in (0xC0, 0xC1, 0xC2):
                height = int.from_bytes(data[i + 5 : i + 7], "big")
                width = int.from_bytes(data[i + 7 : i + 9], "big")
                return width, height
            # Skip to next marker
            length = int.from_bytes(data[i + 2 : i + 4], "big")
            i += 2 + length

    return None, None


def _defer_sphinx_scripts(content: str) -> str:
    """Add ``defer`` attribute to synchronous Sphinx scripts in ``<head>``.

    Targets only known safe-to-defer scripts from the ``_DEFERRABLE_SCRIPTS``
    set, avoiding modification of third-party or theme scripts.
    """
    for script_name in _DEFERRABLE_SCRIPTS:
        # Match <script src="...script_name..."> (without existing defer)
        pattern = re.compile(
            rf'<script(?!\s+defer)(\s+src="[^"]*{re.escape(script_name)}[^"]*")>',
            re.IGNORECASE,
        )
        content = pattern.sub(r"<script defer\1>", content)
    return content


def _post_process_html(app: Sphinx, exception: Exception | None) -> None:
    """Post-process built HTML files for performance improvements.

    Applies three optimizations in a single pass per file:
    - Lazy loading for below-the-fold images
    - Defer attribute on synchronous Sphinx scripts
    - Explicit width/height on local images
    """
    if exception:
        return

    outdir = Path(app.outdir)
    html_files = list(outdir.rglob("*.html"))
    lazy_count = 0
    defer_count = 0
    dim_count = 0

    # Lazy loading pattern: <img> without loading=, excluding logo
    img_pattern = re.compile(
        r"<img(?![^>]*loading=)([^>]*?)(/?)>",
        re.IGNORECASE,
    )

    for html_file in html_files:
        content = html_file.read_text(encoding="utf-8")
        original = content

        # --- 1. Lazy loading (skip logo and first content image) ---
        skip_count = 0

        def _lazy_replacer(match: re.Match[str]) -> str:
            nonlocal skip_count
            img_attrs = match.group(1)
            closing = match.group(2)
            if "cosmoscalibur_logo" in img_attrs:
                return match.group(0)
            if skip_count == 0:
                skip_count += 1
                return match.group(0)
            return f'<img loading="lazy" decoding="async"{img_attrs}{closing}>'

        content = img_pattern.sub(_lazy_replacer, content)

        # --- 2. Defer Sphinx scripts ---
        new_content = _defer_sphinx_scripts(content)
        if new_content != content:
            defer_count += 1
            content = new_content

        # --- 3. Add image dimensions ---
        html_dir = html_file.parent
        new_content = _add_image_dimensions(content, html_dir)
        if new_content != content:
            dim_count += 1
            content = new_content

        if content != original:
            html_file.write_text(content, encoding="utf-8")
            if skip_count > 0:
                lazy_count += 1

    logger.info(
        "perf-optimizer: lazy=%d files, defer=%d files, dimensions=%d files",
        lazy_count,
        defer_count,
        dim_count,
        type="perf_optimizer",
        subtype="information",
    )
