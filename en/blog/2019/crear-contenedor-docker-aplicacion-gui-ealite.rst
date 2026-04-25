:date: 2026-04-18
:tags: container, docker, ealite, enterprise architect, wine
:category: linux
:author: Edward Villegas-Pulgarin
:language: en

Create Docker container GUI application - EALite
================================================

Continuing with the use of containers that I started in the previous post,
:doc:`/en/blog/2019/crear-contenedor-lxc-para-aplicacion-gui-ealite`, I will reproduce the
installation of Enterprise Architect Viewer (EALite) with Docker (and of course,
Wine). If you want to reproduce the example in this case, you need to reproduce
the mentioned article to extract the Wine directory.

Unlike LXC, Docker is more oriented towards application isolation and
not operating system isolation (LXC fulfills a function closer to a virtual
machine), which helps in better application deployment and the
standardization of development and testing stages.

Common to LXC, we have base images that we can use, available on
`DockerHub`_. From these we can complete
our needs by specifying them in the Dockerfile.

Install Docker
--------------

I recommend installing docker with snap on Linux.

.. code::

   sudo snap install docker

Later, we can associate our user for execution without being
administrator.

.. code::

   sudo groupadd docker
   sudo usermod -aG docker $USER
   newgrp docker

You can test by running as a regular user: :code:`docker run hello-world`.

Dockerfile
----------

This file is the mechanism by which the construction rules of our image are specified.
A common language is defined regardless of the base operating system, and
the specific functions of the system are used with an instruction that enables execution on it.

The comments in the file are as we are traditionally accustomed
in other languages (among them, bash), with the number sign :code:`#`. This has
one exception, which is the case where there is a directive afterwards like the case that
will be exemplified.

The :code:`escape` directive is used to change the line break character
for multi-line instructions. You can have the usual backslash
(``\``), which conflicts with paths with spaces in Linux or
Windows paths, and the option of the backtick (`````).

Next we can define the base image using :code:`FROM` followed by the
specification of the image in `DockerHub`_. In this case, we will use the `Ubuntu Docker image <https://hub.docker.com/_/ubuntu>`_ with i386 architecture and
version 18.04. In general, the invocation structure is
:code:`architecture/ubuntu:version`.

The instructions are executed by default by the *root* user
(administrator), so we can execute package installations by directly invoking the system call starting with :code:`RUN`. As
seen in the example below, this is a typical line executed in
Ubuntu.

.. note::

   User creation is necessary because Wine must be run by a
   regular user. Additionally, the username corresponds to the same name
   of the Linux user from which we brought the copy of the installation in Wine (Wine
   assigns the Windows username equal to the Linux user, so, when copying
   the Wine folder, it will only work if it finds the same user).

We can change the directory on which we execute using :code:`WORKDIR`.
In the following line we use :code:`COPY` to move a directory from the host system
to the image. There is a similar instruction, :code:`ADD`, which
supports the source being a URL by downloading it, and decompresses
*tar* files.

.. note::

   The directory we will move was generated in the LXC container we built
   in :doc:`/en/blog/2019/crear-contenedor-lxc-para-aplicacion-gui-ealite`. To do this,
   we start the container and extract the directory.

   .. code::

      sudo lxc start ea
      sudo lxc file pull -r ea/home/ubuntu/.wine .

With :code:`USER` we change the user running the processes. It is important
that when finishing, if a process is executed by a regular user,
our last user change must point to them; otherwise the
container will be active for the administrator user. Another important aspect
is the default behavior in Linux, where it can create the user if it doesn't
exist (but not the user directory).

Finally, it is necessary to indicate what executes when the container is launched.
This is possible with :code:`CMD` or with :code:`ENTRYPOINT`. The difference is that
the first allows overriding the execution by sending as a parameter what
you want to execute, while the second option only executes the configured one.

.. code::

   # escape=`
   FROM i386/ubuntu:18.04
   RUN apt update -q && apt install --install-recommends -y wine-stable
   RUN apt install -y fonts-crosextra-carlito
   RUN useradd -ms /bin/bash ubuntu
   WORKDIR /home/ubuntu
   COPY .wine .wine
   RUN chown -R ubuntu .wine
   USER ubuntu
   RUN mkdir -p .local/bin && `
           echo "wine $HOME/.wine/drive_c/Program\ Files/Sparx\ Systems/EA\ LITE/EA.exe" > .local/bin/ealite && `
           chmod 755 .local/bin/ealite
   CMD ".local/bin/ealite"

Build Docker image
------------------

The build is done with the :code:`build` option. The :code:`-t` argument is used
to indicate the tag we will assign to the image and :code:`-f`
to relate the path of the dockerfile that will be used. The next
argument has no flag to indicate it and corresponds to the context, which is
the path where the files we will use are located (which can be
replaced by a context file with the path to the different files).

.. code::

   docker build -t cosmoscalibur/ealite:latest -f dockerfile .

Run container
-------------

Now you can launch a graphical container based on the built image with the
following instruction.

.. code::

   docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" cosmoscalibur/ealite:latest

References
----------

+ `Docker docs: Post-installation steps for Linux <https://docs.docker.com/install/linux/linux-postinstall/>`_.
+ `Docker docs: Reference documentation <https://docs.docker.com/reference/>`_.
+ `Running GUI Applications inside Docker Containers <https://medium.com/@SaravSun/running-gui-applications-inside-docker-containers-83d65c0db110>`_.
+ `Installing Enterprise Architect under Linux <https://www.sparxsystems.com/enterprise_architect_user_guide/14.0/product_information/enterprise_architect_linux.html>`_.

.. _DockerHub: https://hub.docker.com

----

*This article was originally published in Spanish on 2019-11-22.*
