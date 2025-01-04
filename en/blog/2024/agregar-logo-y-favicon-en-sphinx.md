---
date: 2024-09-24
tags: blog, sphinx, favicon, blogging with sphinx
category: technology
language: en
---

# Adding Logo and Favicon to Sphinx

A new step in my blog, I decided to leave a personal touch through a logo,
something simple but distinctive from pre-downloaded images like before, and
which is why I hadn't configured it yet. I'll tell you how to configure the logo
and favicon for Sphinx.

## Assets Directory

To start, we need to configure the directory that will hold our static files for
the logo and favicon. In our configuration file, {file}`conf.py`, we'll adjust
the value of the `html_static_path` variable, as explained in a previous
[publication](#sphinx-dir-setup-en).

This step is especially important if you host your blog on GitHub, since the
default value doesn't allow files with a leading `_` to be loaded during
deployment.

## Logo

Well, this point isn't too unusual, but I'll leave a recommendation. It's better
to have an editable source file for our logo so we can make adjustments easily.
For example, we might want to create dark and light versions of our logo, and we
can make these changes without having to start over from scratch.

In my case, I created this logo using [Inkscape](https://inkscape.org/es/) in
vector format (`.svg`), and I synchronized it in the
[repository](https://github.com/cosmoscalibur/cosmoscalibur.github.io/blob/master/static/logo/cosmoscalibur.svg)
as well. This is part of our static files.

Another suggestion is to keep in mind that when it comes to dimensions, it's
better to have a more horizontal shape than vertical, but the width shouldn't
exceed 200 pixels.

Now, let's go back to our `conf.py` file again, and we'll find the `html_logo`
variable where we can assign the relative path to our logo configuration. For
example:

```{code} python
html_logo = 'static/cosmoscalibur_logo.png'
```

In my opinion, with a single logo version, it's okay. However, if you need to
use a version per theme, this depends on the theme selected, and in PyData, we
can use the options for
[`html_theme_options`](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html#different-logos-for-light-and-dark-mode)
which allow us to switch between light and dark logos.

```{figure} /images/agregar-logo-y-favicon-en-sphinx/logo-en-sphinx.png
---
alt: Configured logo in blog
align: center
width: 800px
height: 250px
---
Configured logo in blog
```

## Favicon

For the favicon as well, we can use Sphinx's own options with the variable
`html_favicon`. Our favicon must be 16x16 pixels in size and can be in ICO, PNG,
SVG, or GIF format.

Due to the square size of the favicon, which will appear in browser tabs or
bookmarks, it's convenient to have a second design based on our logo that adapts
to these dimensions.

So, in our {file}`conf.py` file, we make the adjustment:

```{code} python
html_logo = 'static/cosmoscalibur_favicon.png'
```

Now, the favicon published.

```{figure} /images/agregar-logo-y-favicon-en-sphinx/favicon-en-sphinx.png
---
alt: Square favicon icon in tab browser.
align: center
width: 289px
height: 125px
---
   Our favicon icon in tab browser.
```

## Referencias

- [Sphinx - Configuration - HTML logo](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo).
- [Sphinx - Configuration - HTML favicon](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon).
- [PyData Theme - Branding and logo](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html).
