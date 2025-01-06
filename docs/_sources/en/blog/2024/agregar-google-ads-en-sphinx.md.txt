---
date: 2024-09-25
tags: google ads, sphinx
category: technology, blogging with sphinx
language: en
---

# Adding Google Ads to Sphinx

Following my recent adjustments to my blog, I wanted to give it another chance,
and some people may not like it, but I'm putting up _Google Ads_ and seeing if
this can generate some income now that many of us use blockers (yes, even me).
I'll tell you how to configure it through modifying the default templates.

## Assets Directory

We need to [configure directories of general files](#sphinx-dir-setup-en) that
will be at the root level of deployment and template directories, in order to
ensure that the directory does not have a problematic `_` prefix on _GitHub
Pages_ and be aware of the value rather than taking the default value.

```{code} python
html_extra_path = ['files']
templates_path = ['templates']
```

We create the directories `{file}`files`and`{file}`templates` if they haven't
been created yet.

## Ads File

A first step to include _Google Ads_ is to include our publisher validation and
this can be done by including scripts or an ad {file}`ads.txt` file. It's
recommended to use the latter option to reduce script load, and it's also
preferred by Google for ad validation, especially when there are multiple
providers involved.

This file needs to be at the root of our site, so we'll make sure it's available
in the `files` directory, which is meant for this type of files.

Once we have approval, we'll proceed with the script.

## Script in Head

Inside {file}`templates`, we need to create a new file that will be used to
modify the default behavior of the {file}`layout.html` template, which is the
template used by _Sphinx_ and contains what is added between the opening and
closing tags of `head`.

We create the file with the same name as the template we want to replace, and on
its first line, it indicates that it extends that template.

We now use the associated block for `extrahead` to add the _Google Ads_ script
that requires it to be in the `head`.

For my case, it would look like this (you should change it according to your
Google Adsense section).

```{code} html
{% extends "!layout.html" %}

{{ super() }}

{% block extrahead %}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-0356238418278924"
    crossorigin="anonymous"></script>
{% endblock %}
```

A few minutes (or hours) later, we'll have the display of ads on our site
generated with Sphinx.

```{figure} /images/agregar-google-ads-en-sphinx/ads-en-sphinx.png
---
alt: Ads display on site generated with Sphinx.
align: center
width: 500px
height: 250px
---
Ads display on site generated with Sphinx.
```

## Referencias

- [Sphinx - Configuration - `html_extra_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path).
- [Sphinx - Configuration - `templates_path`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path).
- [Sphinx - HTML theme development - Templating](https://www.sphinx-doc.org/en/master/development/html_themes/templating.html).
