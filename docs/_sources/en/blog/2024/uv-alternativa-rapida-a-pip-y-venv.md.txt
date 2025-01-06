---
date: 2024-06-30
tags: package manager, virtualenv manager, rust, python, uv, pip, venv
category: technology, programming
language: en
---

# UV: A Fast Alternative to PIP and VENV

UV is a package manager and virtual environment alternative for _Python_,
developed in _Rust_, which promises to be very fast in the processes it aims to
replace those of PIP and VENV. In this sense, all you need to do is add `uv`
before the usual instructions, and it should work (except for some particular
cases of compatibility or lack of implementation).

This is one of many tools that are emerging with _Rust_ to permeate the _Python_
ecosystem, generating a new value, such as improved performance. And from the
same creator, we also have _Ruff_ as an efficient replacement for _linters_, and
other tools like _PyO3_ for creating Python libraries in Rust, Polars as an
alternative to Pandas, or Robyn as an alternative to Flask.

This project, [UV](https://astral.sh/blog/uv), aims to be the equivalent of a
_cargo_ (the _Rust_ package manager) for Python, integrating multiple utilities
into a single binary.

## Instalación de UV

Si tenemos en nuestro sistema más de una versión Python, la forma recomendada
para instalar será a partir del _script_ de instalación que provee, ya que de
esta forma queda disponible para todas nuestras instalaciones sin depender de un
ambiente Python en particular. Esto es porque el binario evalúa la instalación
de Python correspondiente a través de las variables de entorno y soporta las
funciones de gestión para el ambiente detectado.

You can install {program}`uv` with following script:

`````{tab-set}
````{tab-item} Linux and Mac
```{code} bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
````
````{tab-item} Windows
```{code} bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
````
`````

UV is also available as a Python package, so you can use _pip_ to install it. If
you need to validate another method or operating system, you can check out the
[official repository](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started).

```{code} bash
pip install uv
```

As we'll see later, there will be some good improvements in package installation
times and environment creation. However, it's worth noting that if you plan to
use this tool to reduce the execution time of GitHub Actions, the installation
time of UV or its
[cache management](https://github.com/actions/setup-python/issues/822) may not
be an alternative at the moment, unless the actual execution time is
significantly reduced. In my case, the direct method took 7.8 seconds, while the
installation with PIP took 5.8 seconds.

To update _UV_ from the binary, we can use `uv self update` (available since
version 0.1.23).

### Uninstalling UV

This is not well-documented, but it's available in a
[repository issue report](https://github.com/astral-sh/uv/issues/1696#issuecomment-2031776112),
considering it's simply a binary. So, we're interested in clearing the UV cache
and removing the binary.

```{code} bash
rm -rf $HOME/.cache/uv
rm $HOME/.cargo/bin/uv
```

## Virtual Environment Creation

Like with the _venv_ utility, the virtual environment created depends on the
Python installation used (detected by environment variables), and we will have
an option to manage it using its default name or assigning a new one.

```{code} bash
python3 -m venv testvenv  # VENV: 2.5 s
uv venv testuv  # UV: 0.01 s
```

## Installing Python Packages

In general, it's a good practice to use environments and UV will do so by
default. However, in case of a global installation, we can pass `--system` as an
argument (suitable for CI or containers).

In my case, I need to activate the environment to compare the installation of
_pip_ and _UV_. The test scenario will be installing the dependencies used in
the [blog repository](./crear-un-blog-con-sphinx.md#dependencies).

```{code} bash
source testenv/bin/activate
python3 -m pip install -r requirements.txt -r requirements-dev.txt
```

```{code} bash
source testuv/bin/activate
uv pip install -r requirements.txt -r requirements-dev.txt
```

While _pip_ took 25.5 seconds to install, _UV_ took only 5.9 seconds. We can
already notice significant differences that in a Continuous Integration (CI)
workflow like GitHub Actions, could represent interesting savings.

I also repeated this exercise for the main repository at my work, and it took 6
seconds with UV without caching and installing UV, whereas PIP takes typically
32 seconds without caching and 24 seconds with caching. In this case, it's
essential to pass the `--system` option to use it in GitHub Actions.

```{code} bash
pip install uv
uv pip install --system -r requirements.txt -r requirements-dev.txt
```

It's essential to keep in mind the change in syntax when installing a package
from a repository, and it involves using `"package @url_repo"` syntax. And
especially if the package has credentials, consider the corresponding support as
per
[the instructions](https://github.com/astral-sh/uv?tab=readme-ov-file#git-authentication)
