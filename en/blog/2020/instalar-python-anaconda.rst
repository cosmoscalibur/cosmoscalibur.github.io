:date: 2026-04-18
:tags: anaconda, package manager, python
:category: linux, programming
:author: Edward Villegas-Pulgarin
:language: en

Install Anaconda Python
=======================

In recent years, a tool has become popular not only as a base
for the data analytics ecosystem ("data science" as some also
call it) but also generally for Python development
(scientific, web, or general purpose). This tool is Anaconda, which not
only provides us with a cross-platform package distribution system, a
main repository with broad cross-platform support (*default* or
*anaconda* channel) but also an environment manager to allow isolating our
dependencies, facilitating reproducibility and avoiding conflicts.

Get installer
-------------

Our first step is to obtain the Anaconda Python installer according to our
operating system, installation mode, and storage space or
bandwidth limitation. Although Anaconda still has installers for
Python 2.7, I do not recommend their use but rather the versions associated with Python 3.X
(Python 2 lost support on December 31, 2019).

If we have storage space or bandwidth limitations, we can
use the installer for
`miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, which
corresponds to an installer of around 60 MB on the 3 operating systems.
This installer gives us greater control over the installed packages, and only
includes by default what is necessary for the Python interpreter and the Conda
manager.

If we want a collection of packages ready to use, we will go to the
`Anaconda Python <https://anaconda.org/>`_ installer (we select *Download Anaconda*).
Now we go to the installers section (*Anaconda Installers*) and we will choose
the one according to our need:

+ 32 and 64-bit graphical installer for Windows.
+ Command-line installer for Windows (64-bit).
+ Graphical and command-line installer for Mac (64-bit).

This download is around 500 MB for all cases.

Command line installation
-------------------------

Command-line installation applies in the same way for both Mac
and Linux, both using an installer based on bash code (regardless of
whether it is Anaconda or Miniconda).

For this case we will rely on silent installation [cmd-en]_ to avoid
interactive questions and thus not worry during the installation. We invoke
the installer with Bash as follows (make sure to use the full and
correct path of the :code:`sh` installer you will use).

.. code:: bash

   bash Anaconda3-2020.02-Linux-x86_64.sh -b -p $HOME/anaconda
   echo ". $HOME/anaconda/etc/profile.d/conda.sh" >> $HOME/.bashrc
   source $HOME/.bashrc

In the Bash invocation, the :code:`-b` argument implies the acceptance of
licenses and with :code:`-p` we indicate the path for the Anaconda installation
(you can change it to your desire).

The second and third lines are specific if you use a Bash console. This
allows the Conda manager to be recognized by the console when a new
session is started and the last line applies it for the current session.

Although it is not my preference and can also generate potential conflicts, if
you want the Anaconda Python environment to be activated by default you can
add the line :code:`conda activate` to the :code:`.bashrc`.

.. youtube:: UFfsg56qigY
   :align: center

The version of *Anaconda Navigator* included in 2020.02 on Linux has a
bug, so if when executing it you see the message
:code:`UnboundLocalError: local variable 'DISTRO_NAME' referenced before assignment`
it will be enough to update the package [navigator-en]_.

.. code:: bash

   conda update anaconda-navigator

Graphical installation
----------------------

Installation on Windows with the graphical installer [gui-en]_ is simple. The
default options are exactly the recommended ones, so it is only
necessary to click "*Next*" every time.

It is strongly recommended to use the installation with the default options,
to avoid future conflicts. That is, install "*Just Me*" so as not to require
administrator permissions, do not add to the :code:`PATH` (to avoid conflicts with
programs that make use of Python or other packages included in Anaconda), and
register Anaconda Python as the default Python (so it will be recognized by
code editors that detect Anaconda).

.. youtube:: zFk6beeQ-CU
   :align: center

For the graphical installation on Mac you can also follow the default options.

Verify installation
-------------------

Validating the list of included packages is enough to know that Anaconda
works properly. We open the Bash console (Linux or Mac) or
*Anaconda Prompt* (Windows, or opening *Anaconda Navigator* is enough), and
we execute :code:`conda list`. If we observe the list of packages, it works.

References
----------

.. [cmd-en] `Installing in silent mode <https://conda.io/projects/conda/en/latest/user-guide/install/linux.html#installing-in-silent-mode>`_.
   conda.
.. [navigator-en] `UnboundLocalError: local variable 'DISTRO_NAME' referenced before assignment <https://github.com/ContinuumIO/anaconda-issues/issues/11662>`_. Anaconda issues.
.. [gui-en] `Installing on Windows <https://docs.anaconda.com/anaconda/install/windows/>`_. Anaconda.

----

*This article was originally published in Spanish on 2020-06-29.*
