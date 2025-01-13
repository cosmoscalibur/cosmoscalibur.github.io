:date: 2020-01-06
:tags: python, sphinx, restructuredtext, documentation
:category: technology
:language: en

Creating Documentation for a Python Project with Sphinx
=======================================================

Without a doubt, an important step in any development project (and not just
software projects) is generating documentation. For software projects, it's
possible to rely on tools that help automate documentation generation by
extracting comments from the code, using keywords and markup language to modify
style in the text, or including other elements such as images, equations, and
links.

Some tools for this purpose are `Doxygen` (commonly used for C/C++ projects),
`Javadoc` (also commonly used for Java and TypeScript projects), `ESDoc` (for
JavaScript), and of course Sphinx for Python.

In this entry, we will install the necessary tools to generate documentation for
our Python project and make a small example.

LaTeX
-----

If you want to generate web documentation, this package is not necessary, but it
is an essential dependency if you want to generate your documentation in PDF
format. The installation recommended will depend on the operating system used.

Mac
    You can use `MacTeX <https://www.tug.org/mactex/>`_, which includes the
    TeXLive compiler and editors like TeXShop, along with other dependencies
    required for LaTeX to work on your Mac.

Windows
    The most convenient option is `MikTeX <https://miktex.org/download>`_, which
    allows automatic download of additional packages as needed (installation "on
    the fly").

    It's essential that you don't change to silent mode in the configuration, as
    this can affect subsequent execution in cases requiring installation.

    If you use Anaconda, you can include it from the *conda-forge* channel with:
    ``conda install -c conda-forge miktex``

    In the first installation method, you'll need to install Perl. In the
    second, this is already included as a pre-installed dependency by the
    package manager. You can also use `TeXLive
    <https://tug.org/texlive/acquire.html>`_ for Windows, which ensures
    consistency in results across the three operating systems.

Linux
    On Linux, we will use TeXLive, but its installation will be done directly
    from the package manager of the operating system. In most Linux
    distributions, it will be available through the package manager.

    For Debian-based distributions (such as Ubuntu and Linux Mint), you can
    install it in the following way:

    ::

        sudo apt install -y texlive texlive-latex-base texlive-latex-extra \
            texlive-lang-spanish latexmk

Sphinx
------

If we use Python through Anaconda, we can use the `conda` manager for
installation, so `conda install sphinx`, whereas otherwise we can use the
package manager *PIP*: `pip install -U Sphinx`.

.. note::

    If you want a Windows experience similar to Linux, using the traditional
    `Makefile` and the possibility of combining with Bash, I recommend using Git
    Bash. If you're using Anaconda in conjunction, you can install the `make`
    package with Anaconda (`conda install make`) or install `Mingw-w64
    <http://mingw-w64.org/doku.php>`_.

Configuration of Sphinx
-----------------------

We will open a terminal (if on Windows, keep in mind that you'll need to use
either Anaconda Prompt, Anaconda PowerShell or another one if you've configured
it - like Git Bash, which I mentioned earlier) and navigate to the directory
where we're setting up our documentation. It's common practice to set aside a
`docs` directory for this purpose.

Now, we run `sphinx-quickstart` and respond to the questions that appear. We
should note that if using Windows, we need to add the `.exe` extension to the
command, like `sphinx-quickstart.exe`.

::

    > Separate source and build directories (y/n) [n]: y
    > Project name: my_project
    > Author name(s): Edward Villegas-Pulgarin
    > Project release []: 0.1.0
    > Project language [en]: en

I always recommend separating the source code directory from the documentation
directory, and the output of compiled files. Regarding versioning schemes, I
prefer `semantic versioning <https://semver.org/>`_ that allows users to get a
better idea of the project's maturity with numbers, but you can also use
`calendar versioning <https://calver.org/>`_. In language specification, we
specify the language in two-letter international code, as supported by Sphinx
(https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language).

Although the terminal suggests that we can continue with the `index.rst` file,
we need to make some small changes to the `conf.py` file located in the
`docs/source` directory.

You can learn more about configuration options in Sphinx documentation under
`conf.py <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_.

Extensions
~~~~~~~~~~

I recommend including the Autodoc extension to automatically extract
documentation from the API, MathJax for support of mathematical equations in the
Web version, and Napoleon for the Numpy and Google styles in the documentation.
With Coverage, you can validate that functions have been documented, and doctest
integrates code tests from the documentation (compare outputs with a
documentation example).

Modifying this file:

::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.mathjax',
        'sphinx.ext.napoleon',
        'sphinx.ext.coverage',
        'sphinx.ext.doctest'
    ]

Import your project
~~~~~~~~~~~~~~~~~~~

To update metadata automatically from the code (e.g., author or version), you
can import the package in your configuration file. Since you'll be in
development mode, the package hasn't been installed yet and needs to be
uncommented by removing the three lines of code at the top of the `Path setup`
section. The default point refers to the same `docs/source` directory, so you
need to replace it with `../..` to get two levels up, which is necessary.

::

    import os
    import sys
    import datetime
    sys.path.insert(0, os.path.abspath('../..'))
    import my_project

Now, you can do things like this, if available in your code.

.. code-block:: python

    author = my_project.__author__
    copyright = str(datetime.date.today().year) + ", " + author
    release = my_project.__version__

This has an impact on some dependencies, which can cause errors or if we don't
have all the package dependencies for documentation generation. In my case, I've
had issues when having Tensorflow or ArcPy without the license installed. In
such cases, we can create a "mock" of the packages:

.. code-block:: python

    autodoc_mock_imports = ["tensorflow", "arcpy"]

Cross-references
~~~~~~~~~~~~~~~~

To use cross-references, i.e., numbering of tables, figures, code and equations
if they have a footer (object reference), and being referenced in the text by
number, you need to configure the following:

::

    numfig = True
    numfig_format = {'figure': 'Fig. %s', 'table': 'Tabla %s',
                     'code-block': 'Código %s', 'section': 'Sección %s'}
    numfig_secnum_depth = 1
    math_numfig = True
    math_eqref_format = 'Ec. {number}'

Thus, it's possible to use ``:label:`` to assign a reference to objects and
``:numref`` and ``:eq:`` when mentioning them. With `numfig_secnum_depth`
configuration, you can control the numbering of objects, where 0 indicates
continuous numbering (i.e., no section or subsection number), 1 means section
number, and 2 means subsection number.

LaTeX
~~~~~

There's a basic LaTeX configuration that you can add. The main document, the
name of the TeX file, the name of our documentation, the author's name (which we
can use the variable already defined), and the type of document (whose `manual`
class is defined by Sphinx)

::

    master_doc = 'index'
    latex_documents = [
        (master_doc, 'proyecto.tex', 'Documentación Proyecto',
         author, 'manual'),
    ]

ReStructuredText Markup
-----------------------

On this topic, it's worth checking out the documentation of `DocUtils
<https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html>`_ and
Sphinx's `ReStructuredText Primer
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

Once you have a grasp of ReStructuredText basics, you can start editing the
basic parts. From there, to fully take advantage of Sphinx, you need to learn
about elements like roles, directives, and domains (`Sphinx ReStructuredText
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_).

And why domains? They add syntax to manage relationships with code, such as
linking related functions generated by `autodoc` and the way to document a
function (or another code element) in its source code, which can be extracted.
For example, the `Python domain
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain>`_.

What files should I edit?
~~~~~~~~~~~~~~~~~~~~~~~~~

First, we'll edit `docs/source/index.rst`, where we need to add the names of the
files included in the documentation, both generated and automatic ones. One file
per line, without extension, and with relative positioning relative to the
location of `index.rst`.

I recommend always having a `README.rst` file that defines the general scope and
intention of the project, an `history.rst` file for documenting changes between
versions (like a manual changelog but more condensed), a `usage.rst` file
documenting how to use the project, an `installation.rst` file with installation
instructions, and add additional files, such as a route to the documentation API
(the same path we'll indicate later). You can add more files, for example, I
usually use a `concepts.rst` file to detail necessary concepts before using the
software or explain theoretical aspects that help interpret results or expand on
information so someone can analyze or continue development.

::

    .. toctree::
       :maxdepth: 3
       :caption: Contenido:

       README
       installation
       usage
       api/modules
       concepts
       history

And we can delete those lines of *Indices and tables*.

We see a mention of ``api/modules``, which is important for including
automatically generated documentation extracted by Sphinx, which will be
explained in the next section.

Execution of Sphinx
-------------------

As we're using `autodoc`, our first step is to generate the API extraction.

::

    sphinx-apidoc -f -M -o source/api/ ../proyecto

Remember that on Windows, we need to add `.exe` (e.g., `sphinx-apidoc.exe`).
`-f` forces regeneration of files (important if we update API documentation).
`-M` prioritizes module documentation over function documentation by default,
which doesn't seem natural to me.

Next, is the path to the API documentation (one of the files will be
`api/modules.rst`) and finally, the path where the package is located. Both
paths are relative to the documentation directory.

Now, all we need to do is generate the documentation: `make latexpdf` if using
the `Makefile`, or `make.bat latexpdf` if you haven't installed `make` on
Windows. Here, we need to go back up one level in the directory hierarchy to
execute it.

Publish
-------

Now, you'll find the LaTeX files in the *build* directory, and one of them will
be the PDF we want. You can also do HTML compilation (`make html`) and use it to
publish as a `GitHub Pages <https://pages.github.com/>`_ or on `ReadTheDocs
<https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_
