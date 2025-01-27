---
date: 2025-01-26
tags: python, uv, setuptools
category: technology, programming
language: en
---

# No module named `pkg_resources` found in UV environment

If, like many others, you have already started migrating to the package manager
{program}`uv`, you might have encountered the
`ModuleNotFoundError: No module named 'pkg_resources'` issue. Don't worry, this
won't be an obstacle to continuing the migration.

## What is `pkg_resources`?

The `pkg_resources` module belongs to the *setuptools* package and allows access
to resource files and discovery of extensions. However, this module is not
recommended and has been marked as deprecated; instead, `importlib.resources`
and `importlib.metadata` should be used. Nevertheless, despite being obsolete,
many packages still use it. What produces the error?

## What is Setuptools?

*Setuptools* is a library designed to help generate Python library packages,
with complementary routines to `distutils`. However, this library is not part of
the *core* of Python and is actually an independent package. The base
installation on operating systems or standard Python installations, or in some
environment managers like {program}`conda`, usually includes it. But the
installation created with the {program}`uv` environment does not have it. This
is where the problem arises: many packages depend on the assumption that
`setuptools` is installed by default, and {program}`uv` does not provide it in
this way. By default, Python does not come with a packaging and publishing tool
as part of its *core* (`setuptools` is under the governance of *PyPA*, but this
does not imply that it is core).

## Adding `setuptools` to Dependencies

With the context provided, the solution is clear. The issue does not lie with
{program}`uv`; rather, the affected packages have forgotten to add `setuptools`
as a dependency. Therefore, our solution to the problem is straightforward: add
`setuptools` to the dependencies.

If your project uses a `requirements.txt` file, this is the appropriate place to
add it (see
[here](/en/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md#installing-python-packages)).
However, if you are using {program}`uv`'s project management tools
([see here](/en/blog/2025/configuracion-de-proyectos-y-herramientas-python-con-uv.md)),
you can use `uv add setuptools`. If it is a tool, you will need to inject the
dependency with `--with setuptools`.

## References

- [Package Discovery and Resource Access using pkg_resources](https://setuptools.pypa.io/en/latest/pkg_resources.html).
  Setuptools.
- [Guides on backward compatibility & deprecated practice](https://setuptools.pypa.io/en/latest/deprecated/index.html).
  Setuptools.
- [Some tools are installed without pkg_resources](https://github.com/astral-sh/uv/issues/6384).
  GitHub UV.
