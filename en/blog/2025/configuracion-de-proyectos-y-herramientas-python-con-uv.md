---
date: 2025-01-06
tags: package manager, virtualenv manager, pyproject, python, uv
category: technology, blogging with sphinx, programming
language: en
---

# Configuration of Python Projects and Tools with UV

We will create a Python project using {program}`uv`, which utilizes the
{file}`pyproject.toml` format for its configuration, making it easier to port
across different environments. This format is also already widely used by other
package managers of Python, and is commonly used for configuring utilities.

For illustration purposes, I'll be migrating the blog management to UV, of which
I had already mentioned its benefits as an
[alternative to PIP and VENV](/en/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md).

## Creating a Project with `uv init`

If we create one from scratch, the project name will be the directory name, but
if we're inside and use the existing directory, it will be assigned as the
project name. In my case, the existing directory is my GitHub repository for
{file}`cosmoscalibur.github.io`, and this will be the project name.

We don't always need to use the same version of Python, and on Linux, we have it
installed by default, but not everyone has the same version. Therefore, it's
convenient to specify the version in the {file}`pyproject.toml` configuration
file, which generates files such as {file}`.python-version`, an example
{file}`hello.py` file.

```{code} bash
uv init . -p 3.12
```

When we're inside the directory, we can run `uv run hello.py`, which will use
the specified Python version and build the necessary environment to work. The
environment will be created in the {file}`.venv` subdirectory. Since we've done
this test, you can delete the example file now.

To add dependencies to the project, we use `uv add`. We can add them
individually or a list of packages.

```{code} bash
uv add sphinx
uv add ablog
uv add pydata-sphinx-theme
uv add sphinx-design sphinx-copybutton sphinxcontrib-youtube sphinxext-rediraffe
uv add sphinxext-opengraph matplotlib
uv add myst-parser jupytext myst-nb
```

These additions are appended to the project's dependencies field in the
{file}`pyproject.toml` file.

By default, if no explicit restriction is specified, it will use the maximum
compatible version available in the environment. If you need an explicit
restriction, you can specify it using the same syntax as with {program}`pip`,
and it must be enclosed within quotes.

Optional dependencies also have their own addition mechanism, which I'll take
advantage of to add one that I'm replacing with my own management approach, but
would like to compare. This is done by adding `--optional <group_name>` followed
by the name of a group for this optional dependency.

```{code} bash
uv add sphinx-sitemap --optional sitemap
```

We can also explicitly specify which dependencies are for development by using
`uv add --dev`. Or, if we want to indicate a specific group of development
dependencies, we use `uv add --group <group_name>` followed by the name of the
group and then the packages.

```{code} bash
uv add --dev jupyterlab jupyterlab_myst
uv add --group rest rstcheck doc8 docstrfmt "esbonio>=1.0.0b8"
uv add --group markdown mdformat mdformat-gfm mdformat-frontmatter \
  mdformat-footnote mdformat-gfm-alerts mdformat-myst
```

It's worth noting that the `--dev` option is a shortcut for specifying the "dev"
group (`--group dev`), which is the default group.

### Running Entry Points and Scripts with `uv run`

As with any virtual environment, this one can be activated and once it's done,
you can run entry points (the executable utility or function) or routines by
invoking {program}`python`.

```{code} bash
source .venv/bin/activate # With source
pipenv shell # With pipenv (also on Windows)
```

If you don't have {program}`pipenv`, you can install it as a tool using the
command `uv tool install pipenv`.

However, {program}`uv` itself offers a convenient way to run without explicitly
activating the environment, which is very useful in many cases, such as when
running a {file}`justfile` (which we'll cover later). From the initial example,
you already know how to run a routine, but if you need an executable utility
from the environment, you have a similar approach by initializing with
`uv run --`.

```{code} bash
uv run hello.py  # Ejecutar rutinas Python
uv run -- ablog clean  # Ejecutar utilidades en el ambiente
```

If the environment hasn't been created, this step creates it in {file}`.venv` or
ensures that the environment is up-to-date. Additionally, it also creates
{file}`uv.lock`, a format that ensures the exact reproducibility of
environments. This file can be created using `uv sync` and `uv lock`.

## Installing Tools with `uv tool`

In the previous example, packages added with groups do not require explicit
dependency on the project and can be installed globally. This type of usage
corresponds to the concept of tools, and with {program}`uv` we can manage it in
two ways:

- Temporal: They are stored in cache and always use the {program}`uvx` prefix.
  If they're not installed, they get installed and executed; if they're already
  installed, they run as usual.
- Permanent: They are linked to visibility across the entire OS with direct
  invocation of application's entry point. In this case, installation is
  required as a first step, and then invoked traditionally. I prefer this case
  because I often use them in other projects, but for cloud or isolated
  projects, the previous option is suitable. This is done using
  `uv tool install`.

For ReST-related packages in my repo, each one is a separate tool, so we proceed
with installing each one individually.

```{code} bash
uv tool install rstcheck
uv tool install doc8
uv tool install docstrfmt
uv tool install esbonio --prerelease=allow
```

Just like when adding dependencies, if no explicit version is specified, the
most recent one is used. In the case of {program}`esbonio`, there's a parameter
`--prerelease=allow` that allows us to use pre-release versions (alpha, beta,
candidates), but we can also specify an explicit version.

For Markdown packages in the group, these are actually extensions of a main
package, {program}`mdformat`. To inject additional dependencies, we do it using
the parameter `--with`.

```{code} bash
uv tool install mdformat \
  --with mdformat-gfm \
  --with mdformat-frontmatter \
  --with mdformat-footnote \
  --with mdformat-gfm-alerts \
  --with mdformat-myst
```

Finally, although the options are illustrated, as I'm testing modifications in
extensions, I also need Ruff for code adjustments (although this may not be
necessary depending on the IDE used)

```{code} bash
uv tool install ruff
```

## References

- [{menuselection}`uv-->Concepts-->Projects`](https://docs.astral.sh/uv/concepts/projects/).
- [{menuselection}`uv-->Guides-->Working on projects`](https://docs.astral.sh/uv/guides/projects/).
- [{menuselection}`uv-->Concepts-->Tools`](https://docs.astral.sh/uv/concepts/tools/#the-path).
