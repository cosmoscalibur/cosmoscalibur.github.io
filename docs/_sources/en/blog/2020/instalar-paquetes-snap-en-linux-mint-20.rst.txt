:date: 2020-06-29
:tags: linux mint, snap, apt
:category: technology
:language: en

Install snap packages in Linux Mint 20
=======================================

Do you already have Linux Mint 20 and do you want to
:ref:`install Snap packages <en-instalando-paquetes-en-linux-mint#snap>`? Mint has
decided to disable the default installation of Snap, and it is necessary to change
the apt configuration in order to do so.

The problem
-----------

If you already have Linux Mint 20, you will notice that when you try to install the
package :code:`snapd` (the snap manager), you will be surprised to find that it cannot
be installed. You will encounter a message similar to the following:

.. raw:: html

    <pre><font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#739FCF"><b>~</b></font>$ apt install snapd
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    Package snapd is not available, but is referred to by another package.
    This may mean that the package is missing, has been obsoleted, or
    is only available from another source

    <font color="#EF2929"><b>E: </b></font>Package &apos;snapd&apos; has no installation candidate</pre>

    <pre><font color="#8AE234"><b>cosmoscalibur@edliviano</b></font>:<font color="#739FCF"><b>~</b></font>$ apt show snapd
    Package: snapd
    State: not a real package (virtual)
    <font color="#C4A000">N: </font>Can&apos;t select candidate version from package snapd as it has no candidate
    <font color="#C4A000">N: </font>There is 1 additional record. Please use the &apos;-a&apos; switch to see it
    <font color="#C4A000">N: </font>No packages found</pre>


The reason
----------

This problem is caused by a modification in the preferences of :code:`apt` that
tricks it into believing there is no available package to fulfill the request.
This behavior is due to the *Chromium* installer, which, for easier maintenance
by the Ubuntu team, uses a DEB package whose sole function is to invoke the
installation from snap (installing snap if it is not already installed).

Personally, I do not see this as problematic; in an ideal case, having package
managers that automatically install components from another manager would be
preferable over me having to handle such tasks. However, the Mint team finds a
lack of transparency with their users who are not warned about this and even
consider it a security flaw [snap-mint]_.

The solution
-----------

To solve this problem, simply remove or comment out the lines in a file
:code:`/etc/apt/preferences.d/nosnap.pref`. In my case, I do not see any reason
to keep it, so I proceed by removing it and then installing the snap manager.
If you feel more comfortable, you can comment out the lines and then uncomment
them after installing the snap manager [snap-install]_.

.. code:: bash

   sudo rm /etc/apt/preferences.d/nosnap.pref
   sudo apt install -y snapd
   snap help

Now you can install your snap packages in the way I explained in a
:ref:`previous article <en-instalando-paquetes-en-linux-mint#snap>`.

References
-----------

.. [snap-mint] Snapping at Canonical's Snap: Linux Mint team says no to Ubuntu
   store 'backdoor'.
   `The register, 2 Jun 2020 <https://www.theregister.com/2020/06/02/linux_mint_team_snap/>`_.
.. [snap-install] How To Enable Snap And Install Snap Packages On Linux Mint 20?
   `fossbytes, June 12, 2020 <https://fossbytes.com/how-to-enable-snap-and-install-snap-packages-on-linux-mint-20/>`_
