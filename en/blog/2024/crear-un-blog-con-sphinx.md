---
date: 2024-05-16
tags: python, ablog, sphinx, static site generators, blogging with sphinx
category: technology
language: en
---

# Creating a blog with Sphinx

Finally, I've taken the step of restarting my blog, and with it, the migration
process that I wanted to undertake. On this process, I'll be telling you about
it in several entries, since the migration isn't complete yet, and this is the
first entry regarding this topic, covering the basics so you don't fail on your
attempt.

## Why Sphinx?

Sphinx is a static documentation generator that is almost the standard for
projects developed in Python, and has a good number of extensions that support
this generator, including even one that converts your project into a blog,
called Ablog.

Since my primary programming language is Python, it's clear why I want an option
based on Python. However, before I used Nikola, which is also developed in
Python but has Sphinx with a larger and more active community (including users
and developers). Additionally, the development of Sphinx and its extensions is
aligned with changes in the ecosystem and aligns with docutils directives. Given
the recent changes in the ecosystem, I find it interesting how Sphinx supports
Jupyter Notebooks and Myst, which results in code entries having a benefit, and
Myst expands on Markdown options (and is not supported well enough by Nikola or
other generators I reviewed).

Also, I've been more familiar with
[Sphinx](/en/blog/2020/crear-documentacion-de-un-proyecto-python-con-sphinx.rst),
but at the moment when I switched to a static generator, it wasn't very
well-known, but now it has attracted a larger community with MyST support.

## Creating the blog

Alright, let's get started. We'll follow the step-by-step process.

### Dependencies

We will use Sphinx for static content generation and Ablog will allow us to
include tags for dates, which is the essential difference between pages and
publications (and with that, options for filtering indices).

Regarding appearance, we can find different themes, but I have inclined towards
PyData (since several blogs that I follow use it, so I've seen its result and
want to dig deeper into how it's used). Additionally, it's a good idea to add
Sphinx Design to add additional components such as grids, tabs, cards, and
others.

Without a doubt (and although I used it in Nikola), having YouTube videos is
necessary, so we need to have Sphinx Contrib Youtube installed.

Although for sharing on social media we don't need anything special, having the
right metadata generation will help with better indexing and previewing. To this
end, we'll use Sphinx Ext OpenGraph (which not only includes the OpenGraph
protocol but also an extra tag for _Twitter Card_). In this case, we have a
detail to mention, and it's that generating images shared (since by default it
doesn't use the first image of the post and there isn't always one) requires
installing Matplotlib.

Finally, to support Markdown, we'll use Myst Parser. It's interesting that in
the extension with Myst NB, we'll get support for generating publications in
Notebook using MystMd (so we'll also install Jupyterlab). This is something I
love because it will be natural to publish notes on code with their results.

Sitemap generates the site map, although to use it with the desired
internationalization scheme, I'll have to modify it in the future.

Copy button will help us create the option to copy the code blocks to the
clipboard.

With these details, our file {file}`requirements.txt` will look like this:

```
# Static site generation and theme
sphinx
ablog
pydata-sphinx-theme

# Components
sphinx-design
sphinx-copybutton
sphinxcontrib-youtube

# Metadata
sphinxext-opengraph
matplotlib
sphinx-sitemap

# Markdown, MyST and Notebook support
myst-parser
jupyterlab
jupyterlab_myst
myst-nb
```

````{dropdown} Optionals
Not everything is about automatic content generation, we also need support
while writing. So, we can install doc8, rstcheck, and esbonio, for validating
our {file}`.rst` files and Jupyterlab Myst, to help with rendering in the
Notebook as we draft.

With that, we can have our `requirements-dev.txt` file like this:

```
jupyterlab_myst
rstcheck
doc8
esbonio
```

If we also use VSCode, it's worth installing the following extensions:

- MyST-Markdown: For editing MystMD
- Esbonio: For editing RST
- reStructuredText (lexstudio): For editing RST
- Jupyter: To manipulate notebooks
- Emoji: To insert emojis with the command palette 😀
- Spell Right: For spelling correction
- Font Awesome Gallery: To find the notation for Font Awesome icons if you plan
to use them (it has a significant impact on page load time).
````

```{dropdown} Extras
Well, here are some extensions that might be useful, but weren't for me:

- sphinxext-rediraffe: It's definitely worth having around. This extension is
  highly recommended for making redirects. In my case, I don't need advanced
  options yet, so I'm good with the redirect option from `:redirect:` in
  publication posts.
- sphinx-intl: Helps with internationalization. However, I don't think it's
  suitable for projects like a blog, where not all entries necessarily have
  translations or may require context that makes translation incomplete. I find
  it more suitable for documentation rather than a blog.
```

### ABlog configuration

You can use `ablog start` and respond to the basic initialization questions.

```
> Root path for your project (path has to exist) [.]:
> Project name: Cosmoscalibur
> Author name(s): Edward Villegas-Pulgarin
> Base URL for your project: https://www.cosmoscalibur.com/
```

Since GitHub Pages can only use the `docs/` directory for static sites, it's
convenient to set the root directory of the project to be the root directory of
the repository (if you're using a Git repository) so that the output directory
is at this level.

Regarding the project name, by default it will include the word "_blog_" at the
end of the name we provide (in English, it would be perfect). However, we also
find that the HTML file contains a mention of "_documentation_", which is not
suitable for our blog. We'll adjust this in the following variables:

```python
project = 'Cosmoscalibur'
blog_title = 'Cosmoscalibur'
html_title = 'Cosmoscalibur'
html_short_title = 'Cosmoscalibur'
```

Regarding the theme, by default Ablog sets up Alabaster, but as I mentioned
earlier, we will use the PyData theme and can remove Alabaster from the `import`
block.

```python
html_theme = 'pydata_sphinx_theme'
```

To include OpenGraph metadata, we'll add the base URL and can also add custom
brands. As a result, I'll be able to include my Twitter creator card (now known
as X), and the type specification will default to `summary_large_image` (this
setting doesn't seem to be customizable).

```python
ogp_site_url = 'https://www.cosmoscalibur.com'
ogp_custom_meta_tags = [
    '<meta name="twitter:creator" content="@cosmoscalibur" />',
]
```

To configure the default language, we use the corresponding variable with the
ISO code of the language (in my case, `es` from spanish).

```python
language = 'es'
```

In my case, spanish is my native language, but I plan to post some content in
English occasionally. That's why I'll be setting up an internationalization
pattern for the blog using the format `<lang>/blog/<year>/<post>`, so that by
changing just the `<lang>` segment, you can access the version in another
language.

This affects the `blog_path_pattern` variable, which allows defining the URL
pattern to automatically recognize and display publications (no need to add a
tag). Additionally, I'll need to define a route for the publication archive.

```{code-block} python
---
name: blog-conf-en
---
blog_path = 'blog'
blog_post_pattern = '*/blog/*/*'
```

We also need to set up other directories and files. For ease of use with GitHub
Pages, we'll remove the underscore from the directories destined for static
assets and templates (by default they're ignored if they start with this
notation). We'll also add a special directory that will allow us to add files
directly to the root deployment (for example, to add the CNAME file).

It's important to note that for GitHub Pages generation, the output directory
must be {file}`docs`.

Finally, we need to define the configuration variables in {file}`conf.py`.

```{code-block} python
---
name: sphinx-dir-setup-en
---
templates_path = ['templates']
html_static_path = ['static']
html_extra_path = ['files']
ablog_website = 'docs'
```

Now we'll define the files that shouldn't be processed. This is important
because when the Sphinx directory is at the same level as the repository
directory, all files are seen. Additionally, there are generated Sphinx files
that if not removed, will attempt to be processed in a subsequent deployment.

```{code-block} python
---
name: exclude-files-en
---
exclude_patterns = [
    "_build",
    "***/.ipynb_checkpoints/*",
    'Pipfile',
    'LICENSE',
    'README.md',
    'requirements*.txt',
    '.vscode',
    '.venv',
    'docs',
    '.doctrees',
    '.gitignore',
]
```

To enable the extensions we're going to use, we need to list them in
`extensions`. A detail is that although we have installed Myst Parser, we aren't
adding it explicitly because it's already defined within Myst NB.

Some errors are caused by this:

```
WARNING: while setting up extension myst_nb: role 'sub-ref' is already registered, it will be overridden
WARNING: while setting up extension myst_nb: directive 'figure-md' is already registered, it will be overridden
Extension error:
Config value 'myst_commonmark_only' already present
---
source_suffix '.md' is already registered
```

Thus, we can define:

```python
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
```

The first two cases we've enabled are default extensions that will help us
shorten URL notation and make convenient links to other Sphinx projects (we'll
review this in future entries).

Now that we have Myst NB enabled, we can remove the line from `source_suffix`
because it's configured by the extension, and the default value prevents
Markdown files from being compiled.

Regarding Myst options, we're going to enable several extensions that will allow
us to use directives more easily (not using backticks), make substitutions, and
enable dollar signs for equations. Additionally, we'll create references
(`targets`) for titles up to three levels deep (h1, h2, and h3). We can also add
tags more easily in blocks or lines, substitute with Jinja2, definition blocks,
replacements, or task lists. I'm omitting `linkify` as it doesn't seem
particularly useful.

```{code} python
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
```

Similarly, I hope that in the table of contents on the right, third-level titles
will be displayed. To do this, we need to adjust the theme configurations.

Our Google Analytics identifier is also available in this same section (PyData
also supports Plausible).

We can also add our Twitter and GitHub links to the theme configuration.

```{code} python
html_theme_options = {
    'show_toc_level': 2,
    'twitter_url': 'https://twitter.com/cosmoscalibur',
    'github_url': 'https://github.com/cosmoscalibur/',
}
html_theme_options['analytics'] = {'google_analytics_id': 'G-4YFQBC69LB'}
```

We have separated the `analytics` line to easily disable it in testing, so that
it doesn't affect metrics. Later, we want to make this happen with automatic
deployment on GitHub Actions and dependent on an environment variable.

Regarding sidebar panels, we are doing the following configuration at the
moment:

```{code} python
html_sidebars = {
    'index': [],
    "blog": ["ablog/categories.html", "ablog/archives.html"],
    "*/blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}
```

Don't worry, I'll explain it in another entry. For now, I'll take one by
default, since these panels need to be customized and we need to do HTML, so
that I can think carefully about what to put when they're not blog posts (where
the provided cases seem perfect to me).

We can also include icons from _Font Awesome_, but keep in mind that it may have
a significant impact on the site's load time, as this is not optimized. In my
case, when testing, I see that it is the biggest penalty to page loads at the
level of scripts.

```{code} python
fontawesome_included = True
```

I must say that I don't like the idea of enabling the display of source code
from the publication on the site itself, because it generates duplication of
files in the output directory, copying them. If someone wants to see the code, I
consider the repository for that purpose, unfortunately, disabling it would
still cause duplication, so I'll leave it enabled (if I find a way to remove the
duplicates, I'll disable it).

```{code} python
html_show_sourcelink = True
```

Now, the configuration for publications. We need to define the format of the
date stamp now, and we can set it at will (but it must be consistent with this
option across all publications). We can also specify how many paragraphs will be
used in the description and which image to consider for previewing. Finally, if
there's any redirection involved, the time in seconds for its execution.

```{code} python
post_date_format = '%Y-%m-%d'
post_date_format_short = '%Y-%m-%d'
post_auto_excerpt = 1
post_auto_image = 1
post_redirect_refresh = 0
```

Now we're going to enable full-text content for the _feeds_ so they can be
consumed in their entirety by readers of this format.

```{code} python
blog_feed_fulltext = True
```

It's essential to configure our sitemap generation to assist search engines.

```{code} python
sitemap_url_scheme = '{link}'
html_baseurl = 'https://www.cosmoscalibur.com/'
```

Finally, and although it's not the last thing I plan to configure (but will be
covered in another entry), let's talk about comments via Disqus (although I'm
considering changing it, but that will also be a topic for another entry).

```{code} python
disqus_shortname = 'XXXXXXX'
```

### Additional Files and Directories

Within the configuration ({file}`conf.py`), we added the {file}`files`
directory. This allows us to directly add files to the root directory of our
generated site. This is important because some validations require files in this
position, such as:

- {file}`CNAME`: For the validation of our domain name.
- {file}`.nokekyll`: To tell GitHub that we're using Jekyll for compilation. If
  we don't do this, directories and files starting with a hyphen are ignored.
- Google Site verification file: to demonstrate domain ownership to Google.
- Other ownership verification files.
- The {file}`robots.txt` file.

Additionally, if you use a directory at the root level of your repository, it
will become available here. This is my case with the {file}`images` directory
for the images I use.

### First Publication

Ablog helped us generate some demonstration files during initialization. You can
edit and customize them as you see fit.

The case of {file}`index.rst` requires that it be placed in the generated
location for project compilation.

It also created a default publication, which we can move to our
{file}`es/blog/2024` directory (based on the year of creation) and edit there.

Keep in mind that the first-level heading is the title of the publication. In
other generators, titles are added as part of a directive. Since we've already
configured the route pattern for publications and are following it, we don't
need to add directives but rather the front matter, such as:

`````{tab-set}

````{tab-item} RST
```{code} rst

:redirect: blog/configurar-retroarch-en-steam
:date: 2021-12-14
:tags: steam, retroarch, libretro, gaming, linux, controles, videojuegos, emuladores
:category: tecnología/videojuegos
:author: Edward Villegas-Pulgarin
:language: es
```
````

````{tab-item} MD
```{code} md

---
date: 2024-05-14
tags: blog, sphinx, python, ablog, pydata
category: tecnología
author: Edward Villegas-Pulgarin
language: es
---
```
````

`````

The syntax of Markdown and ReStructuredText is available for you to consult.
It's not difficult.

In my case, I am the only author of the blog and in general, I will publish in
Spanish, so it's worth defining the author and default language in the
{file}`conf.py` file.

```{code-block} python

blog_default_author = 'Edward'
blog_authors = {
    'Edward': ('Edward Villegas-Pulgarin', None),
}
blog_default_language = 'es'
blog_languages = {
    'es': ('Español', None),
    'en': ('English', None),
}
```

### Blog Generation

We're ready, so let's generate the site.

```bash
ablog clean && ablog build && ablog serve
```

The part of `ablog clean` is necessary if we want a full rebuild, as it clears
the temporary files generated to avoid recompiling everything. With
`ablog serve`, the browser will open and we can explore.

Now, add, commit and push to your GitHub repo (or any host).

## What's the next?

Well, I'll tell you that now the blog posting process will continue. However,
there's still some exploration left to do.

As for me, here are some details I want to work on soon:

- A Google-based search bar.
- Manual internationalization support based on directory, rather than using
  {file}`.pot`.
- Support for sitemaps with internationalization, following the previous scheme.
- Linking to external resources beyond just GitHub and Twitter (e.g. Mastodon).

## References

- [Sphinx blogging](https://chrisholdgraf.com/blog/2020/sphinx-blogging/)
- [Sphinx Redirects Folder](https://chrisholdgraf.com/blog/2022/sphinx-redirects-folder/)
- [Sphinx blog](https://www.errbufferoverfl.me/posts/2020/sphinx-blog/)
- [Sphinx blog part one](https://www.errbufferoverfl.me/posts/2020/sphinx-blog-part-one/)
- [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- [Ablog](https://ablog.readthedocs.io/en/stable/manual/ablog-quick-start.html)
- [Sphinx Myst Markdown](https://jdsalaro.com/cheatsheet/sphinx-myst-markdown/)
- [Myst Parser](https://myst-parser.readthedocs.io/en/latest/)
- [Migrating the website to Sphinx + ABlog](https://adriaanrol.com/posts/2023/sphinx_migration/)
- [Migration to Cloudflare Pages](https://dailystuff.nl/blog/2021/migration-to-cloudflare-pages)
