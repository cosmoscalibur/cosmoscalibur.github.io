# --- Ablog
blog_path = 'blog'
blog_post_pattern = '*/blog/*/*'
blog_title = 'Cosmoscalibur'
blog_baseurl = 'https://www.cosmoscalibur.com/'

# OpenGraph config
ogp_site_url = 'https://www.cosmoscalibur.com'
ogp_custom_meta_tags = [
    '<meta name="twitter:creator" content="@cosmoscalibur" />',
]

# -- Blog Post Related --------------------------------------------------------
post_date_format = '%Y-%m-%d'
post_auto_excerpt = 1
post_auto_image = 1
post_redirect_refresh = 0

# -- ABlog Sidebars -------------------------------------------------------

# categories, tagcloud, archives, postcard, recentposts, authors, languages, locations
html_sidebars = {
    'index': [],
    "blog": ["ablog/categories.html", "ablog/archives.html"],
    "*/blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}

# -- Blog Feed Options --------------------------------------------------------

blog_feed_fulltext = True

fontawesome_included = True

# -- Sphinx Options -----------------------------------------------------------
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    "myst_nb",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinxcontrib.youtube",
    'ablog',
    'sphinx_sitemap',
    'sphinx_copybutton',
]

sitemap_url_scheme = '{link}'
html_baseurl = 'https://www.cosmoscalibur.com/'

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

# General information about the project.
project = "Cosmoscalibur"
copyright = "2024, Edward Villegas"
author = "Edward Villegas"
language = 'es'

# -- Options for HTML output ----------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    'show_toc_level': 2,
    'twitter_url': 'https://twitter.com/cosmoscalibur',
    'github_url': 'https://github.com/cosmoscalibur/',
}
# Después, esto servirá para separar local de desplegado con Action
#html_theme_options['analytics'] = {'google_analytics_id': 'G-4YFQBC69LB'}
html_title = 'Cosmoscalibur'
html_short_title = 'Cosmoscalibur'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

html_static_path = ['static']
html_extra_path = ['files']
ablog_website = 'docs'
templates_path = ["templates"]
exclude_patterns = [
    '_build',
    '***/.ipynb_checkpoints/*',
    'Pipfile',
    'LICENSE',
    'README.md',
    'requirements*.txt',
    '.vscode',
    '.venv',
    'docs',
    '.doctrees',
    '.gitignore',
    '**/draft/*',
]

html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'
