:date: 2019-10-22
:tags: linux mint, snap, flatpak, appimage, apt, package manager, ubuntu
:category: technology, linux
:language: en

Installing Packages in Linux (Mint)
===================================

In Linux, we now have many more options for installing our favorite and
daily-use programs according to personal interests in reducing disk space,
increasing stability, improving security, always having the latest version,
having very good integration with the operating system, or not requiring
administrator permissions. Some of these strategies even make it possible to use
the same mechanism across multiple Linux distributions, thus enabling a smoother
transition.

This article provides a superficial overview of each package manager, but later
I will publish dedicated articles on each one to give you more options and tips.

Programas generales
-------------------

Aunque no es una clasificación estricta, es la forma que veo para hablar de
estos paquetes de *software*. Son paquetes de uso general, lo suficiente para
ser de interés para disponer a través de medios de distribución para público
general. En ocasiones, esto puede incluir paquetes de uso científico o propio de
desarrollo, o de alguna disciplina particular.

Distribution Package Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The majority of Linux distributions come with *software package managers*, which
are tools for searching, downloading, installing, and configuring these
packages. These managers connect to official repositories maintained by the
distribution developers, ensuring that they meet minimum standards of
compatibility and stability.

Additionally, some package managers can also connect to community-maintained
repositories, providing users with a simple way to extend their software
options. However, this comes with the risk of instability or conflicts due to
interactions with official repository packages (this is not common, but it does
occur). I recommend using these community repositories as a last option.

In Ubuntu and Linux Mint, you have the option to use the Software Center
(pre-installed) or Synaptic (pre-installed in Linux Mint) for graphical package
management. However, you can also use `apt-get` or `apt` (recommended) for
console-based management.

::

    sudo apt update -q
    sudo apt install -y okular

Now you have the PDF file reader installed on your system. You can access it
through the menu or by using the command (``okular``). The first line is
recommended to update the addresses from which software and metadata are
downloaded. The second line performs the installation without requesting
confirmation.

AppImage
~~~~~~~~

This seems to be the best option among the new strategies. It allows for
immediate program execution (no installation required), manages updates, and
does not require administrator permissions since it does not need to install
anything. In theory, it can run on any modern Linux distribution.

Since the file runs directly, multiple versions of the same program can coexist.
This isolation, similar to snap and flatpak options, prevents conflicts in the
system (programs that may require the same dependency but different versions, or
where the dependency cannot manage multiple instances or expose a security
vulnerability).

We will use Stellarium as an example, and you can search for `AppImageHub
<https://appimage.github.io>`_ to see a collection of available AppImages.

.. _appimagecode:

We can download the `Stellarium AppImage <https://stellarium.org/>`_ from the
official software website (the second penguin).

::

    chmod 755 Stellarium-0.19.2-x86_64.AppImage
    ./Stellarium-0.19.2-x86_64.AppImage

Make sure the file is executable. You can do this by running the following
command in a terminal (first line, only the first time). And run the AppImage
file.

If you want to execute it in a more convenient way, you can move the AppImage
file to your user's binary execution directory or a system-wide binary execution
directory to make it available for all users (`/usr/local/bin/`).

::

    mv Stellarium-0.19.2-x86_64.AppImage ~/.local/bin/stellarium
    stellarium

.. _en-instalando-paquetes-en-linux-mint#snap:

Snap
~~~~

Snap packages are the installation mechanism promoted by Canonical (the
developers of Ubuntu). While it remains a centralized mechanism, it requires
approval from Canonical to be included in the repositories and necessitates
administrative permissions for installation.

In Ubuntu, snap is pre-installed, but in Linux Mint you need to install that.

::

    sudo apt install -y snapd

Once installed, we can proceed to install a Snap package.

::

    sudo snap install code --classic
    snap run code # Ejecuta

The execution with `snap run` is necessary if the package is not recognized
after installation. After the first execution or after opening a new terminal or
rebooting the system, the package will be recognized and can be run directly by
name (`code`) or from the menu.

.. update:: 2020-07-02 12:00:00

    Starting with Linux Mint 20, you need to first configure APT to be able to install Snap. You can review my publication for more details.
    :doc:`/en/blog/2020/instalar-paquetes-snap-en-linux-mint-20`.

Flatpak
~~~~~~~

The flatpak case is not very convenient, as it has some centralization like
Snap, but for indexing purposes. A developer can create their own flatpak
repository. And just like AppImage, it does not require administrator
permissions.

In Linux Mint, it comes preconfigured starting from version 18.3, but if you use
Ubuntu, you need to install it. Since version 18.10, it is found in the official
repositories.

::

    sudo apt install flatpak
    sudo apt install gnome-software-plugin-flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

The first line installs the Flatpak manager. The second line allows you to use
Flatpak with the Gnome Software Center. And the third line adds the most popular
Flatpak repository, `Flathub <https://flathub.org/home>`_.

To exemplify, we will install the package peek.

::

    flatpak install -y flathub com.uploadedlobster.peek
    flatpak run com.uploadedlobster.peek

Unfortunately, the execution is always done this way, but you can create a
script to facilitate the process.

::

    echo "flatpak run com.uploadedlobster.peek" > ~/.local/bin/peek
    chmod 755 ~/.local/bin/peek
    peek

Graphically, by default, it will be added to the menu.

Compilation and Binaries
~~~~~~~~~~~~~~~~~~~~~~~~

These options are not part of the narrative. Compilation remains fundamental for
optimizing critical or high-performance code as required in scientific
computing. Compilation takes advantage of the used processor architecture.

In this case, it will typically involve using `configure` and `make`. For more
information, you should read the `README` file, which should detail the
installation process.

With binary packages, you get a pre-compiled version that is generic regarding
the processor or optimized but not necessarily for the specific processor used
in your machine.

Once we have the binary (precompiled or compiled on our own machine), we need to
give execution permissions to the binary (`chmod 755`) and add it to a directory
that is part of the `path` (for example, `~/.local/bin/`).

Installation Scripts
~~~~~~~~~~~~~~~~~~~~

Sometimes we will find files with extensions `.run` or `.sh` that assist in the
installation by downloading components or encoding different files into a single
file.

For this case, it is necessary to confer execution permissions to the file and
proceed to execute it. This procedure is similar to the first two lines of an
AppImage as described `here <#appimagecode>`_.

Referencias
-----------

- `AppImage <https://appimage.org/>`_.
- `Flatpak <https://www.flatpak.org/>`_.
- `Snap <https://snapcraft.io/>`_.
- `Gnome Software Center <https://wiki.gnome.org/Apps/Software>`_.
- `Ubuntu APT <https://help.ubuntu.com/lts/serverguide/apt.html>`_.
