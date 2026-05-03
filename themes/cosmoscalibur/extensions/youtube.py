"""YouTube video directive for Sphinx.

Provides a ``.. youtube:: VIDEO_ID`` directive that generates a
responsive, lazy-loaded iframe embed. Drop-in replacement for
``sphinxcontrib-youtube`` with accessibility improvements.
"""

from __future__ import annotations

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx


class YouTube(Directive):
    """Embed a YouTube video via responsive iframe.

    Usage (RST)::

        .. youtube:: dQw4w9WgXcQ
           :align: center

    Usage (MyST)::

        ```{youtube} dQw4w9WgXcQ
        ```
    """

    required_arguments = 1  # VIDEO_ID
    optional_arguments = 0
    has_content = False
    option_spec = {
        "width": directives.positive_int,
        "height": directives.positive_int,
        "align": lambda arg: directives.choice(arg, ("left", "center", "right")),
        "aspect": directives.unchanged,  # e.g. "16:9"
    }

    def run(self) -> list[nodes.Node]:
        video_id = self.arguments[0].strip()
        width = self.options.get("width", 560)
        height = self.options.get("height", 315)
        align = self.options.get("align", "center")
        align_css = {"left": "left", "center": "center", "right": "right"}.get(
            align, "center"
        )
        html = (
            f'<div class="youtube-wrapper" '
            f'style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;'
            f'margin:1.5rem auto;max-width:100%;text-align:{align_css}">'
            f'<iframe src="https://www.youtube.com/embed/{video_id}" '
            f'width="{width}" height="{height}" '
            f'style="position:absolute;top:0;left:0;width:100%;height:100%" '
            f'allowfullscreen frameborder="0" loading="lazy" '
            f'title="YouTube video {video_id}" '
            f'referrerpolicy="no-referrer-when-downgrade">'
            f"</iframe></div>"
        )
        return [nodes.raw("", html, format="html")]


def setup(app: Sphinx) -> dict:
    """Register the ``youtube`` directive."""
    app.add_directive("youtube", YouTube)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
