import os
from pathlib import Path
import sys

sys.path.append(str(Path("_ext").resolve()))

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

# Font Awesome
fontawesome_included = False

## categories, tagcloud, archives, postcard, recentposts, authors, languages, locations
html_sidebars = {
    "index": [],
    "blog": ["ablog/categories.html", "ablog/archives.html"],
    "*/blog/**": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/archives.html",
    ],
}
ablog_website = "docs"


# --- Opengraph ---
ogp_site_url = "https://www.cosmoscalibur.com"
ogp_custom_meta_tags = [
    '<meta name="twitter:creator" content="@cosmoscalibur" />',
    '<meta name="fediverse:creator" content="@cosmoscalibur@col.social">',
    '<link rel="me" href="https://col.social/@cosmoscalibur">',
    # <a rel="me" href="https://col.social/@cosmoscalibur">Mastodon</a>
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
    "ed_sitemap",
    "sphinx_copybutton",
    "sphinxext.rediraffe",
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

# Redirect
# Inspired by https://chrisholdgraf.com/blog/2022/sphinx-redirects-folder
rediraffe_redirects = {}
base_redirect = Path("es/blog")
years_redirect = [2010, 2011, 2012, 2013, 2014, 2017, 2018, 2019, 2020, 2021]
for year in years_redirect:
    for newpath in (base_redirect / str(year)).glob("*"):
        oldpath = "blog/" + newpath.parts[-1]
        rediraffe_redirects[oldpath] = str(newpath)

# General information about the project.
project = "Cosmoscalibur"
copyright = "2024, Edward Villegas-Pulgarin"
author = "Edward Villegas-Pulgarin"
language = "es"

# -- Options for HTML output ----------------------------------------------
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_toc_level": 2,
    "twitter_url": "https://twitter.com/cosmoscalibur",
    "github_url": "https://github.com/cosmoscalibur/",
}

# Después, esto servirá para separar local de desplegado con Action
if not os.getenv("DEPLOY_LOCAL"):
    html_theme_options["analytics"] = {"google_analytics_id": "G-4YFQBC69LB"}

html_title = "Cosmoscalibur"
html_short_title = "Cosmoscalibur"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "static/cosmoscalibur_logo.png"
html_favicon = "static/cosmoscalibur_favicon.png"

html_static_path = ["static"]
html_extra_path = ["files"]
templates_path = ["templates"]
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
]

html_show_sourcelink = True
