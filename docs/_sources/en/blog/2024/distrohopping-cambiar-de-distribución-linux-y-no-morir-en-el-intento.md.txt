---
date: 2024-12-03
tags: distrohopping, linux distribution, ubuntu, manjaro, kde
category: technology, linux
language: en
---

# "Distrohopping": Switching Linux Distributions Without Losing Your Mind

I've recently switched Linux distributions twice, which got me thinking about
the associated effort and how it could be reduced. It also reminded me of the
concept of "distrohopping" and the discussions about this practice, where many
claim that it's a waste of time and offers little value. However, I disagree and
want to share the value I see in it and how to make it easier.

What have I tried before? Mandriva (discontinued), OpenSuse, Ubuntu, Debian,
Antix, Lubuntu, Antergos, Arch, Gentoo, Funtoo, Linux Mint, Xubuntu, and now
Kubuntu and Manjaro KDE.

Which ones have I had stable periods with for years? Ubuntu, Lubuntu, Linux
Mint, and Xubuntu. This year's transition to Kubuntu made me fall in love with
KDE, and it has become my favorite desktop environment (DE).

## Is distrohopping a good idea?

You'll find many reasons to distrohop: the thrill of the new, wanting to try the
distro everyone's talking about, the latest package manager that's going to
revolutionize installation, the best proprietary driver manager, having a distro
that lets you take full advantage of your latest computer or accessory, or even
reasons related to increasing your knowledge and experience in the world of
Linux and distributions, or generating varied content about all the available
options, or even work-related conditions like the distro used by the servers of
the service you provide as a developer.

For each of these, you'll find a forum or blog that discusses it, and they'll
probably end up telling you that you wasted your time and that it didn't bring
you any value, and they'll recommend that you skip the experience because in
their many years of distrohopping they've concluded that you don't need to try
everything, but just choose one from the beginning that fits your needs and
stick with it. But do you know what? It took them years to figure out what they
were looking for and that it existed.

Distrohopping is exactly what we do when we don't know exactly what we need or
what's out there to choose from, so we start trying. And just like with
smartphones, smart TVs, the apartment you rent, the car you buy, or even the PC
you buy, your tastes and needs change, making the decision you made no longer
the best one, and that's okay.

When you fall in love with a Linux distribution, you'll think that distrohopping
was never necessary and that it didn't help you discover what you eventually
found, but that's a big lie. You have the elements of comparison because you
dared to try, you know that the distribution you chose existed because you were
looking for options every time you found details you didn't like about the
current one. But just like in romantic relationships, we also lose love because
we're not always the same, and Linux distributions aren't either. They change
continuously, taking advantage of technological revolutions or due to their
definitions necessary for self-sustainability or marketing. Even the surrounding
communities can change and affect the distribution.

So, go ahead, it's good to distrohop, but I'm not going to lie to you, those who
claim it's a bad idea have a valid point, and that's the mental and physical
effort involved in the transition. So, we'll focus on how to distrohop while
reducing the impact.

## What do I gain from distrohopping?

Let's delve into this a bit more, taking advantage of the points that many blogs
often highlight about why distrohopping doesn't contribute, and concluding with
what I believe it does contribute.

### Learning more about Linux: No

Let's not sugarcoat it: distrohopping doesn't teach you anything new. If you
really want to learn, you can do it on any distribution. Just face problems the
hard way. For instance, don't rely too much on graphical elements, buttons, or
shortcuts. Use more console commands. And don't always install software from
repositories; sometimes, compile it or install from an archive. Don't use dialog
boxes to modify settings; find the associated plain text configuration file (if
it exists—in KDE Plasma and Wayland, I've found many settings that exist in a
configuration file but are probably undocumented, and you'll have to rely on
dialog boxes or taskbar options because there's not even an associated command).

What you learn in a specific distribution are specific tools for that
distribution, and that knowledge isn't universal or replicable. It won't be
useful if you switch distributions again or if your friend who uses a different
distribution asks for help.

### Better system performance: No

Distrohopping doesn't provide any significant performance boost either.
Generally, performance is determined by hardware, software tailored for specific
tasks, and the level of optimization you achieve. All these can be addressed by
upgrading hardware, switching to software better suited for a particular task,
or fine-tuning processes and uninstalling unnecessary packages. And what if your
hardware is old? You can do all this on any Linux distribution the hard way.

So, you'll clearly see better performance if you edit videos with
GPU-accelerated software instead of CPU-based software, or if your Python code
runs faster when you upgrade to Python 3.12 from 3.9. Your system will boot
faster and have a smoother startup if you disable Dropbox and Discord from
starting at login. Switching from Ubuntu to Arch won't change that. Remember,
accumulated cache and temporary files also need to be cleaned up.

If you want better performance, take advantage of optimizations in newer
versions of the software you use (for example, Python 3.12 offers experimental
JIT and GIL-less mode, which don't exist in 3.9), or use alternative software
that optimizes your desired workflow faster (for example, switching your data
analysis from Pandas to Polars or FireDucks). Or consider whether your hardware
is reaching its limits if it's several years old. And above all, pay close
attention to services that start during boot.

Take advantage of your distribution's cleanup, package, and process managers, or
use optimization and monitoring software like
[Stacer](https://oguzhaninan.github.io/Stacer-Web/).

### Up-to-date software: No

It's clear that there are distributions with more up-to-date software. This is
the difference between rolling release, fixed release, or long-term support
(LTS) models. If you want the newest software, a rolling release is preferable,
but its stability can be compromised. If you want more stability, you'll use an
LTS, but this often means a delay of years in using new software or improving
hardware support. Periodic releases offer a middle ground (although depending on
the distribution's commitment to stability, some periodic releases might be
slower to update packages, like Ubuntu).

However, official repositories aren't the only way to get updated software. You
can easily use Snap if you're on Ubuntu or its derivatives (it might not be as
natural on other distributions) or Flatpak (which is pre-installed on some
distributions or can be installed). You can also use AppImages, which don't
require installation on the system (they're a kind of portable application for
Linux), although they don't have a large centralized repository, so managing
each AppImage becomes a manual process. These options not only allow you to get
the latest versions (if they're the official versions) but also bypass
dependency issues. For example, on Manjaro with my NVIDIA graphics card, I have
trouble installing OBS Studio with Pamac due to a dependency (I mention the
graphics card because the problem isn't reproducible if I install it on a system
with integrated graphics), but if I use Flatpak, it works without any issues.

There are also simple installation options through the package managers of the
development languages in which they were implemented. For example, you can
install the Alacritty terminal emulator in its latest version with cargo (Rust)
or install the video downloader YT-DLP with PIP/UV (Python).

And as always, there's the hard way: you can download the tar.gz file that many
programs provide (like Dropbox, to avoid using a PPA on Ubuntu) or download the
source code from a website or GitHub repository and manage the build
dependencies.

### Philosophical consistency (including fanaticism or purism): No

Many people switch or choose a distribution for philosophical consistency. But
this doesn't really provide it either.

To avoid proprietary software, uninstall it and find alternatives to install. If
you disagree with Ubuntu's default use of Firefox as a Snap and other packages,
uninstall the software, block package managers or software stores from
redirecting to Snap, and then reinstall the DEB version (you've achieved
"desnapping" Ubuntu).

Finally, to ensure freedom of choice, uninstall any component and install the
one that makes you feel good.

Philosophical consistency or purism can be achieved through specific actions on
the distribution.

### Comfort and ease (the path of least resistance): Yes

This is what really matters when choosing a product or service, and it applies
when selecting a Linux distribution. It should be comfortable for us, not for
others; it should be easy for us, not for others.

We want our daily activities to be pleasant, for problems to be easily solved,
and for the task of reinstalling the distribution from scratch if we change
computers or need to reinstall to take little time. But these details are
personal details that adjust to each user's expectations, needs, and experience,
and these elements change in us over time, as well as what we find in
distributions.

This means that all the points I previously indicated could be done the hard way
can be achieved the easy way when changing Linux distributions. Each Linux
distribution is designed for a specific type of user and purpose, and therefore
that focus is natural and optimized. But there is such a wide variety of users
and purposes that the variety of Linux distributions is equally wide, and
finding one that fits like love at first sight, like a perfect match, can take
years (only to change our interests and start a new search process later).

The problem is that this transition process between our old love and the new
love, in Linux distributions, has a high cost.

## Facilitating the transition: healthy distrohopping

What is not commonly found in publications about distrohopping is the easy way
to do it. I even once read about how to do distrohopping easily, and the focus
was on distributions that "allowed" it (in some way, easy-to-use distributions).

But if we want to try even the difficult distributions, is there a healthy and
simple way to do it?

### Evaluate your needs

The first point I want to highlight is that we must be clear about the need for
change. This allows us to jump to a distribution with a prior evaluation of what
we are going to find, and the capabilities required for it. We must bear in mind
that these needs are not only about unsatisfied needs, but also about satisfied
needs, since otherwise we have a high probability of making a jump losing
something necessary.

In my case, my unmet needs are:

- Availability of new software (essentially, the ecosystem of alternatives in
  Rust): I could install them by compiling with cargo, but this increases the
  total installation time. In some cases, compilation is very demanding on the
  system, and it starts to overheat while I'm using it, and its integration into
  the system is not straightforward.
- Availability of updated software: For popular software, typically with a GUI,
  I have no problem finding options in Flatpak that are official or
  well-supported and have all the functionality. However, for advanced uses,
  I've found that GUI software in Flatpak or Snap packages doesn't expose all
  the command-line utility options, or that due to the level of isolation they
  don't integrate properly or even can't connect with other operating system
  services. In my experience, I've also seen a lot of problems with command-line
  utilities or with elements that require notifications or other monitoring of
  their activity.
- Freedom of choice in the installation mechanism: As a user of Ubuntu and its
  derivatives, my Firefox is in snap. But many packages are linked to snap and
  this is not clear at the time of deciding the installation and due to what
  they don't expose being snap I've sometimes had problems. Similarly, with snap
  I've had initialization problems that don't happen with their versions from
  the official repository or even the equivalent in flatpak. But blocking snap
  can have the hidden risk of causing other integration failures that Ubuntu
  expects to have with snap.

And my satisfied needs:

- Proprietary software and drivers: Undoubtedly, with Ubuntu derivatives I have
  a good experience at this level, since having the largest community, it is the
  community that companies focus on the most when generating official versions.
  For example, my experience with NVIDIA has only been good on Ubuntu and
  derivatives (and this also impacts my use of Wayland).
- Stability: Although I have experience with Linux and with intermediate or
  advanced knowledge, I don't want to have to constantly solve problems, and I
  don't want to be afraid of every update or installation.
- Excellent documentation or community: In case of having problems, or wanting
  to validate information before trying something, or to consult how to do
  something, I want to have good options to consult or ask. This is achieved
  with good project documentation or with a very active or large community.

And finally, a few that give me mixed feelings:

- Hardware support: On Ubuntu and its derivatives, this has been a problem when
  I change computers (usually, a new computer). The transition period to be able
  to use it typically forces me to stay on Windows because the kernel that comes
  is not very up-to-date, and therefore does not support the processor, or the
  proprietary drivers are not up-to-date. In general, there is good support, but
  you have to wait until the next periodic release (6 months). When I have tried
  other distributions with rolling release models after changing computers, I
  have had that support, but typically I lost the system in days or weeks, or
  the time required for installation processes was high.
- Pre-installed software according to my activities: This should not be a
  primary criterion because if it is easy to install, I can do it, but without a
  doubt, if there is pre-installed software I can start using it faster. In
  addition, this avoids having to configure the integration of these packages.

It's important that, in the process, we're clear about which needs are
negotiable. In my case, I can lose a bit of freedom of choice in the
installation mechanism if it benefits me, and lose proprietary drivers and
software, if I have alternatives.

With these needs clear, it's possible to delve a little into forums, blogs, and
[DistroWatch](https://distrowatch.com/), to find potential candidates.

Some conclusions based on my needs:

- Continuous release model distribution: Allows me to have new and updated
  software, and I am willing to monitor information and adjustments that may
  come from some instability. To compensate, flatpak sources can be used for GUI
  software, with many dependencies or that have unstable sources in the
  traditional package manager. As well as using PIP/UV, Pixi or Cargo for some
  packages whose main use is in development rather than general use. This way of
  compensating also helps to facilitate distrohopping, as it makes the
  installation of many packages independent of the specific package manager of
  the distribution.
- Avoid immutable release models or Ubuntu derivatives (except Linux Mint):
  Immutable cases continuously resort to using isolation options like flatpak,
  snap or AppImage for user applications. This not only reduces the freedom of
  choice, but also the set of available applications. Ubuntu is discarded due to
  its tendency to use snap below apt.
- Avoid FOSS distributions: A FOSS distribution (like Fedora) does not easily
  allow or support proprietary software. This is a big problem for hardware
  support such as NVIDIA graphics cards or some Wi-Fi drivers, or even the wave
  of machine learning that makes use of CUDA. This discards a distribution like
  Fedora.
- KDE desktop environment: Something that has happened to me over time is that I
  have used more, and more software associated with KDE projects, it is also
  common that many other packages that I use are based on Qt which is the basis
  of KDE. And in base applications, which I normally use little, even the KDE
  base set is more sophisticated (for example, its screenshot tool and
  configuration managers). The KDE project has an Ubuntu-based distribution
  called Neon, and according to multiple sites, the best experiences in KDE have
  been perceived in Kubuntu, which can be two good options in case of staying in
  the Ubuntu families.
- Well-documented distributions with an active community: In my appreciation,
  this is a strong point of Arch and Ubuntu distributions, and by extension to
  its derivatives.
- Distributions with extensive repositories: If I want some of my daily
  activities to be covered in pre-installed packages or that, failing that, can
  be easily installed, it is best to rely on distributions with extensive
  repositories. At this point, but only as a wish and not a firm criterion, we
  favor Arch, Ubuntu and its derivatives again. For example of minimum elements,
  I should have LibreOffice and Firefox pre-installed, and not other text
  processors and browsers. A surprise is that Manjaro includes git, and this
  even serves me to synchronize my installation scripts.

### Keep common problems in mind

There are four major issues on Linux that you should be prepared for and
validate before making the switch:

- Wi-Fi: Easily the thing you'll break most often with distribution changes or
  after a kernel or driver version update. I've had computers where the Wi-Fi
  works perfectly in the live versions, but when installing the distribution,
  the driver is not directly supported, or when updating the kernel the driver
  version is not compiled for that kernel, and it is necessary to manually
  adjust the header of the source code and compile it. In other cases, as
  happened to me in the recent change to Manjaro, the Wi-Fi started losing
  available networks randomly after updating the kernel and adjustments in the
  BIOS and driver configuration file were necessary. Have a wired network
  connection available.
- NVIDIA graphics card: Definitely a big pain if you require maximum
  utilization. In Wayland, this is a limitation in multiple distributions, but
  if it's really important to you, an Ubuntu derivative is probably the best.
  Some software that uses GPU video acceleration can also be affected, and it
  may be convenient to omit acceleration, use a sandboxed version, or wait a few
  months for support to be achieved (in my case, I hope the NVIDIA 560 branch
  arrives soon in Manjaro Stable). This partially affects my experience in
  Wayland and applications that use Vulkan for rendering (like Zed), but I'm
  still using the KDE X11 version on this computer and the computer with an
  integrated graphics card works without any Wayland problems. In some cases,
  the problem may be having a completely black screen or continuous display
  errors if the driver is not supported properly (nothing functional). Validate
  the support of your NVIDIA card with the available driver versions and Wayland
  integration.
- New processors (or hardware in general): If the distribution is not
  continuously released, the kernel version will not be the necessary one to
  support the latest generation computer, contrary to what happens with your
  pre-installed Windows. Validate if your processor is supported in the kernel
  version of the distribution to be tested.
- Proprietary software: Sometimes we can't just look for an alternative, because
  it doesn't compensate for the fact that we have to interact with other people.
  If this is important, for example, for work or study purposes, your transition
  should probably involve continuing to use Windows or alternatives for which
  there is an official version. Validate if the software exists for the
  distribution.

### Create a testing environment or a backup plan

Without a doubt, things can go wrong if you make a radical distribution change,
such as when switching between distribution families. For this reason, it's good
to take small, safe steps like:

- Start testing with a virtual machine: You can use QEMU-KVM or VirtualBox. This
  will help you with the initial approach to installing the operating system,
  quickly exploring the desktop environment and the initial adaptation flow,
  such as installing the software that is most important to you and verifying
  that it works properly. Test it for a few days to see the stability, but this
  is not a victory, because in emulation you don't have the same hardware.
- When moving to real hardware, it would be preferable to maintain a partition
  for the new system while keeping another for the previous one. In case of
  failure, you can resume your work and activities in the previous distro.
- Document or create scripts of the steps performed. This will be important when
  you need to reinstall from scratch or replicate on another machine.
- As soon as it becomes your daily distribution, create backups of your data
  (documents and other own files), as well as configuration files. Take
  advantage of synchronization services like Drive, Dropbox or GitHub. You can
  also keep copies on an external drive or have a partition for the
  {file}`/home` directory.
- Consider having a stable kernel installed on continuously released
  distributions. This way, you can switch to this kernel in case of failure.

### Create a seamless transition

**Package installation**

A quick option to focus on the real problems that may exist in the distribution
you have chosen is to depend less on the distribution's package manager. This
allows you to document or have scripts that will be replicable in an eventual
new change and to reduce the impact of looking for how to adapt your system.

**Desktop environment**

Explore the desktop environments in the Linux distribution you already use. This
will make it easier for you to explore the visual behavior and general
management tools and basic applications with low effort and low risk. Once you
are clear about the desktop environment, look for the new distribution with this
desktop environment. In my case, I was able to explore KDE through Kubuntu (an
Ubuntu variant) and thus noticed that it suited my interest over other
environments. Then, this leads me to only evaluate with respect to the
distributions that have adequate support for KDE.

**Wired and Wi-Fi internet**

Remember that in the face of possible Wi-Fi driver problems, it is always good
to be able to have a wired connection.

## Happy distrohopping

Hopefully this helps you dive into your new Linux distro adventure with
confidence!

I'm personally using Manjaro KDE right now, and I'm really happy to have git and
flatpak pre-installed.

Enjoy your distrohopping!
