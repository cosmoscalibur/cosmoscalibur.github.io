import os
import sys
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path("themes").resolve()))

## --- Ablog ---

# Blog
blog_path = "blog"
blog_post_pattern = "*/blog/*/*"
blog_title = "Cosmoscalibur"
blog_baseurl = "https://www.cosmoscalibur.com/"
blog_default_author = "Edward"
blog_authors = {
    "Edward": ("Edward Villegas-Pulgarin", None),
}
blog_default_language = "es"
blog_languages = {
    "es": ("Español", None),
    "en": ("English", None),
}

# Post
post_date_format = "%Y-%m-%d"
post_date_format_short = "%Y-%m-%d"
post_auto_excerpt = 1
post_auto_image = 1
post_redirect_refresh = 0

# Feed
blog_feed_fulltext = True


## categories, tagcloud, archives, postcard, recentposts, authors, languages, locations
html_sidebars = {
    "index": ["ablog/recentposts.html"],
    "*/index": ["ablog/recentposts.html"],
    "blog": ["ablog/recentposts.html"],
    "blog/**": ["ablog/recentposts.html"],
    "*/blog/20*/*": [
        "ablog/relatedposts.html",
    ],
    "*/blog/category/*": ["ablog/recentposts.html"],
    "*/blog/archiv*": ["ablog/recentposts.html"],
    "*/me/**": ["ablog/recentposts.html"],
}
ablog_website = "docs"


# --- Opengraph ---
ogp_site_url = "https://www.cosmoscalibur.com"
ogp_custom_meta_tags = [
    '<meta name="twitter:creator" content="@cosmoscalibur" />',
    '<meta name="fediverse:creator" content="@cosmoscalibur@col.social" />',
]


# --- Sphinx Options ---
extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "myst_nb",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinxcontrib.youtube",
    "ablog",
    "sphinx_copybutton",
    "cosmoscalibur",
]

sitemap_url_scheme = "{link}"
html_baseurl = "https://www.cosmoscalibur.com/"
sitemap_locales = ["es", "en"]
sitemap_excludes = [
    "search/",
    "genindex/",
]

# -- MyST options ------------------------------------------------------------

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

nb_execution_mode = "off"
nb_render_markdown_format = "myst"

# General information about the project.
project = "Cosmoscalibur"
copyright = f"2010-{datetime.now(tz=UTC).year}, Edward Villegas-Pulgarin"
author = "Edward Villegas-Pulgarin"
language = "es"

# -- Options for HTML output ----------------------------------------------
html_theme = "cosmoscalibur"
html_theme_path = ["themes"]
html_theme_options = {
    "show_toc_level": 2,
    "github_url": "https://github.com/cosmoscalibur/",
    "mastodon_url": "https://col.social/@cosmoscalibur",
    "x_url": "https://x.com/cosmoscalibur",
    "facebook_url": "https://www.facebook.com/cosmoscalibur",
    "youtube_url": "https://www.youtube.com/c/CosmoscaliburCo",
    "linkedin_url": "https://www.linkedin.com/in/cosmoscalibur/",
}

if not os.getenv("DEPLOY_LOCAL"):
    html_theme_options["analytics_id"] = "G-4YFQBC69LB"
    html_theme_options["google_adsense_id"] = "ca-pub-0356238418278924"

html_title = "Cosmoscalibur"
html_short_title = "Cosmoscalibur"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "static/cosmoscalibur_logo.png"
html_favicon = "static/cosmoscalibur_favicon.png"

html_static_path = ["static"]
html_extra_path = ["files"]
templates_path = ["themes/cosmoscalibur"]

exclude_patterns = [
    "_build",
    "***/.ipynb_checkpoints/*",
    "jupyter_execute",
    "Pipfile",
    "LICENSE",
    "README.md",
    "requirements*.txt",
    ".vscode",
    ".venv",
    "docs",
    ".doctrees",
    ".gitignore",
    "**/draft/*",
    "**/skills/*",
    "social-posts.md",
]
