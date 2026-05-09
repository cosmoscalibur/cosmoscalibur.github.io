import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path("themes").resolve()))
sys.path.insert(0, str(Path(".").resolve()))

## --- Cosmoblog ---
# All optional — defaults shown. Languages inferred from directory structure.
blog_path = "blog"
blog_post_pattern = "*/blog/*/*"
blog_feed_fulltext = True

## categories, tagcloud, archives, postcard, recentposts, authors, languages, locations
html_sidebars = {
    "index": ["cosmoscalibur/recentposts.html"],
    "*/index": ["cosmoscalibur/recentposts.html"],
    "blog": ["cosmoscalibur/recentposts.html"],
    "blog/**": ["cosmoscalibur/recentposts.html"],
    "*/blog/20*/*": [],
    "*/blog/category/*": [],
    "*/blog/archive": [],
    "*/me/**": ["cosmoscalibur/recentposts.html"],
    "404": [],
}


# --- Sphinx Options ---
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinxext.opengraph",
    "cosmoblog",
    "cosmoscalibur",
]

html_baseurl = "https://www.cosmoscalibur.com/"

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
author = "Edward Villegas-Pulgarin"
language = "es"

# -- Options for HTML output ----------------------------------------------
html_theme = "cosmoscalibur"
html_theme_options = {
    "show_toc_level": 2,
    "github_url": "https://github.com/cosmoscalibur/",
    "mastodon_url": "https://col.social/@cosmoscalibur",
    "x_url": "https://x.com/cosmoscalibur",
    "facebook_url": "https://www.facebook.com/cosmoscalibur",
    "youtube_url": "https://www.youtube.com/c/CosmoscaliburCo",
    "linkedin_url": "https://www.linkedin.com/in/cosmoscalibur/",
}

if os.getenv("DEPLOY_LOCAL"):
    html_theme_options["posthog_api_key"] = "phc_DohK6STAPe2d7fv33DgsHz2HZ5cpkHQjKVPhEyLEuMLe"
else:
    html_theme_options["analytics_id"] = "G-4YFQBC69LB"
    html_theme_options["google_adsense_id"] = "ca-pub-0356238418278924"


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "static/cosmoscalibur_logo.png"
html_favicon = "static/cosmoscalibur_favicon.png"

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
    "cosmoblog",
]
