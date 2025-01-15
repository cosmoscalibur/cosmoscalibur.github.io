---
date: 2024-05-24
tags: sphinx, python, ablog, static site generator, blogging with sphinx
category: technology
language: en
---

# Migrating my blog from Nikola to Sphinx

Migrating from a static generator to another isn't an entirely transparent
process, so I'll explain some simpler steps to help you migrate your blog from
Nikola to Sphinx.

But before we begin, keep in mind that the basic steps for migration start by
having the bare minimum from scratch with Sphinx. For this purpose, follow the
instructions given at [](/en/blog/2024/crear-un-blog-con-sphinx.md).

## Migrating

Alright, once we have the foundation of our blog set up, continue making
adjustments to ensure that our previous posts still function properly.

### Post

#### Front Matter

Since we added a [path pattern](#blog-conf-en) for publications during the
initial configuration, there is no need to add the `..post:` directive or the
`:blogpost: true` attribute. Simply place your files in the path that matches
the pattern 👀.

It's important to note that in Nikola, we defined navigation paths using the
`..slug:`, but in Sphinx, this depends on the file name and its location within
the directory. Make sure to use the same directory path as defined in the
_slug_, and ensure the file name is equal to the last part of the slug 👀.
Alternatively, you can set up a redirect by using the value of _slug_ as the
value for `:redirect:` (in this case, add `post_redirect_refresh=0` to your
configuration).

To indicate the title in _Nikola_, we used the attribute `..title:`, but now it
must be explicitly defined in the publication markup. Example:

`````{tab-set}

````{tab-item} RST
```{code} rst

Migrating my blog from Nikola to Sphinx
=======================================
```
````

````{tab-item} MD
```{code} md

# Migrating my blog from Nikola to Sphinx
```
````

`````

This requires that existing titles be increased in heading level 👀.

In _ablog_, we don't have an equivalent for Nikola's `..status:`, but we can
control whether a current or past date is equivalent to `published` and if it's
a future or no-date date, it's the equivalent of `draft`. The case of `private`
could be handled by [excluding the file](#exclude-files-en). For `featured`,
it's more customizable, but it could be explored with the card objects on the
index.

If we want to indicate the preview image, in Nikola it was done using
`..previewimage:`, but in _ablog_, we use `:image:` and the value is not the
path of the image, but the number associated with its appearance order in the
publication. This can be set to a default value based on the variable in the
configuration file's `post_auto_image`.

The attribute `..description:` is taken by default as a truncation of the first
paragraph of the post (this is used for the publication metadata), but we can
also leave it customized if needed (this is done with the Open Graph extension).

For the case of `..link:`, this should be converted to `:external_link:`.

For updates, instead of being an attribute, it becomes a timestamp annotation
with context information.

`````{tab-set}

````{tab-item} RST
```{code} rst

.. update:: 2011-12-15

   Extra info added
```
````

````{tab-item} MD
```{code} md

```{update} 2011-12-15

Extra info added
```
```
````

`````

With the attributes of `.. nocomments:`, `.. tags:`, `.. date:`, `.. author:`,
and `.. category:`, simply change the initial `..` to `:`.

Regarding the date, it's important to note that unlike in Nikola, we cannot mix
types of date formats. These should be added according to the definition in the
configuration file, specifically in the variable `post_date_format`.

There is no attribute needed to enable equations as Sphinx enables them by
default. In Nikola, it was necessary with `.. has_math: true`.

The case of `.. type:` does not have an equivalent.

⚠️ If we are using _markdown_, the difference is to remove the initial `:`, as
evidenced in the section on
[the first publication](./crear-un-blog-con-sphinx.md#first-post), and the
separator `<!-- -->` changes to `---`.

#### Content

In some cases, we could use post lists with specific filters using
`.. post-list::` and the attribute `:categories`. This now changes to
`.. postlist::` with the attribute `:category:` (you can also use other filters
as well).

Regarding `.. thumbnail::`, this directive no longer exists and is replaced by
`.. figure::`.

The definition of the _teaser_ in Nikola relied on a specific markup directive
for the text, but in _ablog_, this is controlled by the attribute `:excerpt:` to
denote the number of paragraphs to include. However, we can leave it with a
default value based on `post_auto_excerpt` in the configuration file.

For document references, in Markdown we transition from
`{{% doc %}} path {{% /doc %}}` to `<project:path>` or `[](path)`, while in RST
we can continue using `:doc:` as long as it does not point to a label. In that
case, it would be `:ref:`.

### Configuration

#### Root Files

Files in the root are defined in a directory that we set with the variable
`html_extra_path`, which can be named the same as it comes in Nikola (`files`).

#### Comment System

If we use Disqus (in Nikola, `COMMENT_SYSTEM='disqus'`), the `disqus_shortname`
in the configuration file takes the value of the old `COMMENT_SYSTEM_ID`.

#### YouTube

We need to install `sphinxcontrib-youtube` and enable `sphinxcontrib.youtube` in
the extensions. In this way, the directive `.. youtube::` remains unchanged.

## References

- [Migrating the website to Sphinx + ABlog](https://adriaanrol.com/posts/2023/sphinx_migration/)
- [Migration to Cloudflare Pages](https://dailystuff.nl/blog/2021/migration-to-cloudflare-pages)
- [Ablog](https://ablog.readthedocs.io/en/stable/manual/ablog-quick-start.html)
- [Myst Parser](https://myst-parser.readthedocs.io/en/latest/)
