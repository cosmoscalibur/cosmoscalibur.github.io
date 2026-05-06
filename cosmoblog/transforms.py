"""Doctree transforms — image optimization at the node level.

Implements two image optimizations as native Sphinx post-transforms:

* ``LazyImageTransform``     — ``loading="lazy"`` on below-the-fold images.
* ``ImageDimensionsTransform`` — ``width``/``height`` from source files
  to prevent CLS.

WebP conversion stays in the post-build optimizer because it operates
on output files only (``_images/``), keeping the source tree clean.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform

if TYPE_CHECKING:
    from sphinx.application import Sphinx

logger = logging.getLogger(__name__)


# JPEG marker byte for dimension parsing
_JPEG_MARKER = 0xFF


# ---------------------------------------------------------------------------
# Post-transform: lazy loading
# ---------------------------------------------------------------------------


class LazyImageTransform(SphinxPostTransform):
    """Add ``loading="lazy"`` to below-the-fold images.

    Skips images that already have a ``loading`` attribute.
    The first content image in the document is assumed to be
    above-the-fold and is left eager (browser default).
    """

    default_priority = 800
    formats = ("html",)

    def run(self, **kwargs: Any) -> None:
        seen = 0
        for node in self.document.findall(nodes.image):
            # Already has loading set (e.g., from directive option)
            if node.get("loading"):
                seen += 1
                continue

            # Skip the very first image (above-the-fold / LCP candidate)
            if seen == 0:
                seen += 1
                continue

            node["loading"] = "lazy"
            seen += 1


# ---------------------------------------------------------------------------
# Post-transform: image dimensions
# ---------------------------------------------------------------------------


class ImageDimensionsTransform(SphinxPostTransform):
    """Inject ``width`` and ``height`` from source image files.

    Sets intrinsic dimensions on ``<img>`` tags so the browser can
    reserve layout space before the image loads, preventing Cumulative
    Layout Shift (CLS).

    Only processes local images that don't already have explicit
    width/height from the directive.
    """

    default_priority = 810  # After lazy-image, before writer
    formats = ("html",)

    def run(self, **kwargs: Any) -> None:
        srcdir = Path(self.app.srcdir)

        for node in self.document.findall(nodes.image):
            # Already has explicit dimensions
            if node.get("width") or node.get("height"):
                continue

            uri = node.get("uri", "")

            # Skip external/data URIs
            if uri.startswith(("http://", "https://", "data:", "//")):
                continue

            # Resolve relative to source directory.
            # RST absolute refs start with "/" — strip it.
            img_path = srcdir / uri.lstrip("/")
            
            # Fallback for excerpt images or nested paths that might be incorrectly resolved
            if not img_path.is_file() and "images/" in uri:
                # Try finding it relative to root images/ directly
                parts = uri.split("images/")
                if len(parts) > 1:
                    img_path = srcdir / "images" / parts[-1]

            if not img_path.is_file():
                continue

            try:
                width, height = _get_image_size(img_path)
                if width and height:
                    node["width"] = str(width)
                    node["height"] = str(height)
            except (OSError, ValueError):
                pass


# ---------------------------------------------------------------------------
# Post-transform: table wrapper
# ---------------------------------------------------------------------------


class TableWrapperTransform(SphinxPostTransform):
    """Wrap tables in a scrollable div.

    Prevents layout overflow on small screens without using
    'display: block' on the table element itself.
    """

    default_priority = 820
    formats = ("html",)

    def run(self, **kwargs: Any) -> None:
        for node in self.document.findall(nodes.table):
            # Create a wrapper div
            wrapper = nodes.container()
            wrapper.attributes["classes"].append("table-wrapper")

            # Replace the table node with the wrapper
            node.replace_self(wrapper)
            # Add the table to the wrapper
            wrapper.append(node)


# ---------------------------------------------------------------------------
# Image size reader (zero-dependency, header-only)
# ---------------------------------------------------------------------------


def _get_image_size(path: Path) -> tuple[int | None, int | None]:
    """Read image dimensions from file header without loading the full image.

    Supports PNG, JPEG, GIF, and WebP formats.  Only reads the first
    few hundred bytes of the file.
    """
    with open(path, "rb") as f:
        data = f.read(4096)  # Header is always in first 4KB

    # PNG: width and height at bytes 16-23 in the IHDR chunk
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        width = int.from_bytes(data[16:20], "big")
        height = int.from_bytes(data[20:24], "big")
        return width, height

    # JPEG: scan for SOF marker
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

    # GIF: width and height at bytes 6-9
    if data[:6] in (b"GIF87a", b"GIF89a"):
        width = int.from_bytes(data[6:8], "little")
        height = int.from_bytes(data[8:10], "little")
        return width, height

    # WebP: RIFF header
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        if data[12:16] == b"VP8 ":
            width = int.from_bytes(data[26:28], "little") & 0x3FFF
            height = int.from_bytes(data[28:30], "little") & 0x3FFF
            return width, height
        if data[12:16] == b"VP8L":
            bits = int.from_bytes(data[21:25], "little")
            width = (bits & 0x3FFF) + 1
            height = ((bits >> 14) & 0x3FFF) + 1
            return width, height

    return None, None


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------


def register_transforms(app: Sphinx) -> None:
    """Register all doctree post-transforms with the Sphinx application.

    Post-transforms run at write time (after ``doctree-resolved``),
    just before the HTML writer renders.  This is the correct phase
    for image attribute injection since the doctree is fully resolved
    and images are registered in the builder.
    """
    app.add_post_transform(LazyImageTransform)
    app.add_post_transform(ImageDimensionsTransform)
    app.add_post_transform(TableWrapperTransform)
