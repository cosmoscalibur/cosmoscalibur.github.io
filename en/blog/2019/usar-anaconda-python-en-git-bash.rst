:date: 2026-04-18
:tags: anaconda, package manager, git bash
:category: linux, programming
:author: Edward Villegas-Pulgarin
:language: en

Use Anaconda Python in Git Bash
===============================

Recently, for work reasons I have had to work on Windows and that is
why I had the need to look for a comfortable option to use `Git <https://git-scm.com/>`_
on Windows, with support from `Bash <https://www.gnu.org/software/bash/>`_ to which
I am accustomed in Linux and with Python Anaconda recognized. Somehow,
the minimum version of how to use Windows without dying trying.

Anaconda Python
---------------

The first thing is to proceed to install Anaconda Python from its official site, but
I recommend first reviewing the real need to have everything included in
Anaconda or use something minimalist like Miniconda. Anaconda will represent an
installation and download of almost 500 MB, and therefore a longer time in both
steps. On the other hand, Miniconda only installs the minimum required to have
Python and the Conda package manager. This last option is recommended if
you have little disk space, want to install quickly, only want to test
the basics of Python or the equipment has low specs (I remember cases in
which my students—when I was a teacher—the mere installation of Anaconda
would freeze the computer and restart it).

If you use Anaconda for your development projects and use good practices,
you will surely be used to using environments and in that case you do not need
to have so many things in the base environment, Miniconda being a good option as well.

Download `Anaconda <https://www.anaconda.com/distribution/>`_ or
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ according to your
need and install like any Windows program. The important thing during
the installation is to indicate that it is only for the current user and that the
:code:`PATH` is not associated. Following this advice will avoid headaches in the
future.

.. update:: 2020-07-02 12:00:00

   To know more details about the installation process you can consult my
   post :doc:`/en/blog/2020/instalar-python-anaconda`.

Git Bash
--------

Although you can download it from the project site, we will take advantage of the
Conda manager to facilitate the download, installation, and configuration task.

We will open Anaconda PowerShell or Anaconda Prompt, and we will execute the following:

.. code:: bash

   conda create -n gitbash -c conda-forge git=2.24.0

The use of :code:`-c conda-forge` is important because the
version of Git that we will use will come from this channel. If the default channel is used, only the
console client is installed, while in this option Git Bash is included. I have also indicated
:code:`-n gitbash` to avoid possible conflicts between the
packages required to use Git and the packages available in the base
environment. In a later post I will talk about Conda to go deeper into
this.

Once the installation is finished, you can open the Windows menu and look for Git
Bash, which will already have Conda recognized. Now you just have to start
using it, :code:`conda activate base`.

.. note::

   At this time, our default environment will be gitbash. If you install without
   indicating the environment, you will have the base environment enabled by default but with
   possible conflicts.

And what happens if we already had Git Bash installed? Git Bash supports the typical
Bash files, like :code:`bashrc`. Thus, we can use the configuration that
is usually used in Linux.

We open Git Bash, and we execute:

.. code:: bash

   cd $HOME
   echo ". /c/Users/USER/ANACONDA/etc/profile.d/conda.sh" >> .bashrc
   source .bashrc

With the first line we make sure to go to the user's directory. In the second
line, we will create or edit the configuration file, but you must
replace :code:`USER` with your user's folder and :code:`ANACONDA` with
the Anaconda folder (usually :code:`Anaconda3` or :code:`Miniconda3` if
you used Miniconda). The third line updates the configuration in the current
console session allowing Conda to be used immediately. For the next
time you open Git Bash you will no longer have to configure anything, just start using
Conda (there is still no activated environment).

----

*This article was originally published in Spanish on 2019-12-31.*
