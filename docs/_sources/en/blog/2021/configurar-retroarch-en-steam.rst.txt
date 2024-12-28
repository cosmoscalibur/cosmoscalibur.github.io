:date: 2021-12-14
:tags: steam, retroarch, libretro, gaming, linux, controllers, videogames, emulators
:category: technology
:language: en

Setting Up RetroArch on Steam
=============================

Introduction
------------

`RetroArch <https://www.retroarch.com/>`_ is a cross-platform
(`supported platform downloads <https://www.retroarch.com/?page=platforms>`_)
and open-source emulator and game aggregator. Installing RetroArch
through Steam offers advantages by integrating Steam Play features and
Steam Cloud save states. This also benefits the community by providing
an additional distribution method.

If you prefer a video version, you can watch it on YouTube (spanish version):

.. youtube:: DIJTylhiHyo
   :align: center

Installation via Steam
----------------------

Let's proceed by searching for
`RetroArch on the Steam store <https://store.steampowered.com/app/1118310/RetroArch/>`_.
Install it and accept the subsequent download of *Steam Runtime Soldier*.

Installing Emulators (Cores)
---------------------------

To install emulators (referred to as "cores" within RetroArch), navigate
to the game's DLC option (*Manage > DLC*) and activate the desired
emulators. This list defaults to the *builtin* emulators that have been
gradually included.

Controller Configuration
------------------------

Once you launch RetroArch as a Steam game, to configure your controller,
go (using the keyboard or mouse) to *Settings > Drivers > Joypad Driver*
and change ``udev`` to ``sdl2``, after which you must restart RetroArch.
From this point on, your controller will be functional within the
RetroArch interface.

Loading Games (ROMs)
-------------------

Finally, you can navigate the Main Menu through the *Load Content*
options and find your games (previously downloaded ROMs, which are easily
found with a Google search).

Conclusion
----------

Enjoy your retro gaming experience!
