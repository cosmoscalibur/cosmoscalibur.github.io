"""Atom feed generation for cosmoblog.

Generates one Atom feed per discovered language, plus a combined feed.
"""

from __future__ import annotations

import os
from datetime import date, datetime, timezone
from typing import TYPE_CHECKING, Any

from feedgen.feed import FeedGenerator


def _aware(dt: date | datetime) -> datetime:
    """Convert a date/datetime to a timezone-aware datetime (UTC)."""
    if isinstance(dt, datetime):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt
    # date → datetime at midnight UTC
    return datetime(dt.year, dt.month, dt.day, tzinfo=timezone.utc)

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from .engine import BlogEngine


def generate_atom_feeds(app: Sphinx) -> Any:
    """Generate Atom feeds as virtual pages via ``html-collect-pages``.

    Creates one feed per language at ``{blog_path}/atom.xml``
    (within each language directory).
    """
    engine: BlogEngine = getattr(app.env, "cosmoblog", None)
    if engine is None:
        return

    base_url = (app.config.html_baseurl or "").rstrip("/")
    if not base_url:
        return

    blog_path = app.config.blog_path or "blog"
    blog_title = app.config.project or "Blog"
    feed_fulltext = app.config.blog_feed_fulltext
    author_name = app.config.author or ""

    for lang in sorted(engine.languages):
        posts = engine.by_language(lang)
        if not posts:
            continue

        feed_path_rel = f"{lang}/{blog_path}/atom.xml"
        feed_url = f"{base_url}/{feed_path_rel}"
        feed_dir = os.path.join(app.builder.outdir, lang, blog_path)

        feed = FeedGenerator()
        feed.id(f"{base_url}/{lang}/")
        feed.title(f"{blog_title} ({lang.upper()})")
        feed.link(href=f"{base_url}/{lang}/")
        feed.link(href=feed_url, rel="self")
        feed.language(lang)
        feed.generator("cosmoblog", "0.1.0", "")

        for post in posts:
            post_uri = app.builder.get_target_uri(post.docname)
            post_url = f"{base_url}/{post_uri}"

            entry = feed.add_entry(order="append")
            entry.id(post_url)
            entry.link(href=post_url)
            entry.title(post.title)
            entry.author({"name": author_name})

            if post.date:
                entry.pubDate(_aware(post.date))
            if post.update:
                entry.updated(_aware(post.update))
            elif post.date:
                entry.updated(_aware(post.date))

            # Summary from excerpt
            if post.excerpt:
                entry.summary(post.excerpt)

            # Tags
            for tag in sorted(post.tags):
                entry.category(
                    dict(term=tag.strip().replace(" ", ""), label=tag)
                )

        # Write the feed file
        os.makedirs(feed_dir, exist_ok=True)
        feed_file = os.path.join(feed_dir, "atom.xml")
        with open(feed_file, "w", encoding="utf-8") as f:
            feed_str = feed.atom_str(pretty=True)
            f.write(feed_str.decode())

    # Generator function must yield for html-collect-pages compatibility
    if False:
        yield
