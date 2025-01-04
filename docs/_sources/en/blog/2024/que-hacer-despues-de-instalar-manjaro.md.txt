---
date: 2024-12-05
tags: manjaro, arch, ubuntu, kubuntu, kde, pamac, flatpak
category: technology, linux
language: en
---

# What to do after installing Manjaro KDE 24?

I recently decided to switch to Manjaro KDE (24.1) and I'm very happy with the
change. So, taking this opportunity, I'll share some things to do after
completing the installation.

Since I'm coming from a transition from Kubuntu (24.10) and Xubuntu (22.10),
I'll draw parallels with these steps, so it can also serve as a list of "what to
do after installing Kubuntu 24.10".

Regarding many popular and traditional GUI applications, I don't see a problem
with using Flatpak environments if the native packages represent a problem or
potential problem. For example, OBS doesn't work if I install it natively, but
it does in Flatpak. Moreover, if it's available as a verified Flatpak, I prefer
this over a package available in the AUR. I discuss this a bit more in
[](/en/blog/2024/distrohopping-cambiar-de-distribuci%C3%B3n-linux-y-no-morir-en-el-intento.md),
as this allows me to adapt more quickly and compensate for some stability
issues.

## Review the release announcements

It's important to review the
[release announcements](https://forum.manjaro.org/t/stable-update-2024-10-10-kernels-pacman-7-0-kde-frameworks-6-6-virtualbox-7-1-2-mesa/169192/2),
especially to be aware of potential conflicts and errors that we might
encounter, as well as the options for handling the errors. For example, in the
24.1 release version that I had when installing, I encountered the following
documented errors:

- [Manjaro KDE doesn't shut down and the screen is left black with the pointer](https://forum.manjaro.org/t/kde-dont-shut-down-anymore-since-last-update/168818/2):
  The solution to this case is to go to "Desktop Session" and in the "Restore
  session" options, select "Start with an empty session".
- [After suspension the system freezes](https://bbs.archlinux.org/viewtopic.php?pid=2180537#p2180537):
  This happened to me, but after the general update it didn't happen again, so I
  didn't have a chance to test the solution.

An extra detail, during the installation if you start with the NVIDIA
proprietary drivers, your screen may turn gray. In my case, it was enough to
wait a little longer for the process to resume normality (compared to what I
observed when installing it in a VM and on the PC that doesn't have a dedicated
graphics card).

## Update repository mirrors

This step is useful for ensuring that you download packages from the fastest and
most up-to-date servers. In my case, the mirror I was using started to fail, and
this process allows you to remove those that are no longer functional.

```{code} bash
sudo pacman-mirrors --fasttrack
```

This step is not native to Ubuntu and presents a high level of complexity for
the target audience of the distribution.

## Update the system

Our package management tool on Manjaro is {command}`pamac`. It's an easy-to-use
tool that doesn't require extra effort to memorize the single-letter argument
options of {command}`pacman`, and shares similarities with {command}`apt` from
Ubuntu.

We use `-a` to indicate that we also consider the AUR (Arch User Repository)
source. This instruction updates both the package sources (official repository
and AUR), not just the packages. The AUR is equivalent to the PPA (Personal
Package Archive) on Ubuntu, but in a unified form, unlike the segmented approach
by Ubuntu maintainers, which can lead to many more conflicts and configuration
files.

In general, for a rolling release distribution like Manjaro and its derivatives
(Arch), it's a good practice to frequently update the system to avoid
accumulated updates conflicts.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code} bash
pamac upgrade -a
```

Also, you can use `update` instead of `upgrade`. This updates the entire
distribution and not just the installed packages.

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
apt update -q && apt dist-upgrade -y
```

The first step updates the repository indexes (including PPAs) and the second
step updates the installed packages themselves, including system changes that
may not necessarily be related to the installed packages.
````
`````

For general package management from the repository, we are interested in knowing
how to:

- Install packages from the official repository,
- Install packages from the Arch User Repository (AUR),
- Remove packages.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code-block} bash
:name: pamac-commands-en

sudo pamac install PACKAGE --no-confirm # Official Repository
pamac build PACKAGE_AUR --no-confirm # AUR
sudo pamac remove PACKAGE --no-confirm
pamac search -a KEY
pamac info PACKAGE
```

There's an interesting variant of package installation using the `--as-deps`
flag to explicitly mark installed packages as dependencies rather than explicit
installations. This means that when packages are removed that were previously
installed for us, they will be marked as orphaned.

While it might seem "irresponsible" to use the `--no-confirm` option, since it's
only used on the first installation of packages that have been validated
beforehand, we're fine with it. However, this must be done with caution and in
some cases, it may require validation and even cancellation of the transaction.

If you plan to update or add packages after your initial install, it might be a
good idea to do so interactively as a check and then leave them for your
routines without confirmation. I recommend not using this option at all and make
your own decisions.

When installing from the AUR, my recommendation is always to proceed without
`sudo` unless we have context that doesn't require a GPG key. Otherwise, this
will be stored at an administrative level, causing errors of "_broken pipe_",
which happens because the key needs to be stored in a common user. For example,
this happens with services like Dropbox and Spotify.

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo apt install -y PACKAGE
sudo dpkg -i PACKAGE.deb  # After manually download
sudo apt remove -y PACKAGE
apt search KEY
apt show PACKAGE
```

On Ubuntu, installing from a PPA (Personal Package Archive) is similar, but it
requires prior setup to add the PPA source.

Occasionally, when installing from a _DEB_ package or from a PPA, common issues
arise where dependencies aren't met or aren't resolved correctly. In such cases,
{command}`sudo apt install -f` needs to be applied at the end to fix these
problems.

````
`````

## Installs dependencies for package compilation

When using different source repositories other than the official repository,
you'll need to have a set of additional dependencies that help facilitate this
process. This would be equivalent to the `build-essential` package on Ubuntu.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code}
pamac install base-devel --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo apt install -y build-essential curl git ca-certificates pkg-config
```

````
`````

It's worth noting that the additional packages mentioned for Ubuntu are
installed by default in Manjaro when used directly with `pamac`.

As an alternative to package installation, Manjaro comes with Flatpak
preconfigured, while Ubuntu also comes with Snap preconfigured.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

Flatpak is ready to use.

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

````
`````

## Installs a stable kernel

Use the latest available kernel in Manjaro, but it's recommended to install a
stable kernel (currently 6.6, but possibly 6.12 as well) at this time. This will
be necessary if you need to upgrade your kernel and one of them breaks the
system, requiring you to use an older one. Keep in mind that, as it happens with
Manjaro, unstable kernel versions are removed from the repositories, so they
can't be reinstalled, leaving another risk.

You can install a stable kernel using the Manjaro configuration manager with the
"Kernel" option.

Remember to edit the {file}`/etc/default/grub` file to change the style and time
out lines. The most important thing is the `menu` option in the style variable.

```{code} text
GRUB_TIMEOUT=5

GRUB_TIMEOUT_STYLE=menu
```

This way, we will have GRUB visible at boot and be able to use advanced options
to change kernels.

On Ubuntu, due to its stability, as the kernel is tightly tied to the
distribution version, this is not a preventive step to consider, and it would
only be useful if you require specific hardware support or a very particular
feature.

## Protect your eyes

Select a dark theme in the system. You can search for the menu option "Colors"
and choose between "Breath Dark" or "Breeze Dark". I prefer the first one. This
selection has an impact on how long-term applications take into account the
system theme. You can also search for the "Plasma Styles" option in the menu,
and use "Breath".

If you're using KDE Plasma like me, you can use the "Night Color" mode. You can
adjust the location manually and configure the color temperature that you think
is suitable. In my case, I use 4500K for daytime light and 3700K for nighttime.

If you don't use KDE, you can install
[RedShift](https://github.com/jonls/redshift), but keep in mind that this tool
does not support Wayland.

## Enable numeric keypad at startup

If you want the numeric keypad to be active from boot, we need to go to the
numeric lock setting of hardware keyboard and select 'Activate'. You can quickly
access this option by searching for "Keyboard" in the menu.

This is environment-dependent, so if you don't use KDE Plasma, I recommend
checking the documentation of
[Arch: Activating numlock on bootup](https://wiki.archlinux.org/title/Activating_numlock_on_bootup)
directly.

## Prepare your documents

During Manjaro installation, we have the option to choose between LibreOffice
and OnlyOffice as an office suite. My preference is for
[LibreOffice](https://wiki.archlinux.org/title/LibreOffice#Installation), but
since the installed package is not the latest version, I skip it and install it
now.

Additionally, there are times when we need a compatible alternative with Office,
which occurs in my case due to work-related reasons with Excel, and I need to
use WPS. There were two issues that affected me and was useful the Arch
documentation on
[WPS Office: Troubleshooting](https://wiki.archlinux.org/title/WPS_Office#Troubleshooting).

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code} bash
sudo pamac install libreoffice-fresh --no-confirm
sudo pamac install --as-deps libreoffice-extension-texmaths --no-confirm
pamac build wps-office-bin ttf-wps-fonts libtiff5 --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

In the case of Ubuntu, this comes with LibreOffice pre-installed. And to install
WPS, you will need to download the manual _DEB_ file from its
[website](https://es.wps.com/office/linux/) and install it using
{command}`dpkg`.
````
`````

```{attention}
With a dark theme, LibreOffice icons may not have good visibility by default.
To fix this, go to "Tools > Options" and in the "View" section, evaluate which
option suits you best. In my case, I chose "Breeze (SVG + Dark)"
```

## Password storage

When applications start asking to create a wallet (*kdewallet*), we will accept
it with *blowfish*. Additionally, if the password is the same as our login, this
will be automatically activated.

## Instala Google Chrome

Both in Manjaro and Ubuntu, we will have Firefox as our default browser, but
it's essential to note that Google Chrome becomes necessary many times.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code} bash
pamac build google-chrome --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f
```

This will leave configured the required PPA (Personal Package Archive) for
updates.
````
`````

Remember to synchronize your account in both browsers.

## Synchronize your files

There are multiple options for file synchronization, but undoubtedly
[Dropbox](https://www.dropbox.com/referrals/AABBG1MmL-hedPRRiOrFIiDH6UePOg71THw?src=global9)
remains a common service among many of us as it offers a free hosted alternative
with Linux desktop client support.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code}
pamac build dropbox --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
wget -O https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2024.04.17_amd64.deb
sudo dpkg -i dropbox_2024.04.17_amd64.deb
```

This will leave configured the required PPA (Personal Package Archive) for
updates.

````
`````

After installation, start using it. At this point, we go to the session manager
of Dropbox and can link our account.

## Ready to chat

We don't just chat on our mobile devices, so it's good that we have options on
our PC. I use Telegram for personal reasons, and Discord and Slack for
work-related purposes.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code}
sudo pamac install telegram-desktop discord --no-confirm
pamac build slack-desktop --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
flatpak install flathub org.telegram.desktop
flatpak install flathub com.discordapp.Discord
sudo snap install slack
```

````
`````

## Take screenshots

KDE has a very good and sophisticated screenshot tool (*Spectacle*), but I find
that it also overflows for quick use. For this task, I prefer *Flameshot*
typically.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code}
sudo pamac install flameshot --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo snap install flameshot
```

````
`````

## Ready for creativity

To write an entry on our blog, our thesis project, a lab report, executive
report, marketing presentation, our process flow diagram or code diagram, we
need to do drawings, diagrams, videos, format conversions or basic edits.

That's why here is our creative combo.

- *ImageMagick*: Useful for converting image file formats.
- *FFmpeg*: A command-line utility for audio and video processing.
- *OBS Studio*: An advanced tool for recording and editing video.
- *Draw.io*: Allows creating diagrams and offers a wide range of symbols.
- *Inkscape*: A vector drawing tool, an alternative to Corel Draw.
- *GIMP*: A painting and bit-map editing tool, an alternative to Photoshop. You
  can also explore *Krita* (keep in mind that files with the `.csv` extension
  are associated with this). If you need to edit, it's recommended to use
  {program}`gimp`, and if you want to draw, {program}`krita`.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code}
pamac install imagemagick ffmpeg drawio-desktop inkscape gimp krita --no-confirm
flatpak install -y flathub com.obsproject.Studio
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
sudo apt install -y imagemagick ffmpeg
sudo snap install drawio
flatpak install -y flathub org.inkscape.Inkscape
flatpak install -y sflathub org.gimp.GIMP
flatpak install -y flathub org.kde.krita
flatpak install -y flathub com.obsproject.Studio
```

````
`````

During my installation with _pamac_, I had problems with OBS and this motivated
me to use _flatpak_ in general for various cases and thus avoid managing
optional dependencies or some controller issues. In this particular case, OBS
generated problems with `DeckLink` that is related to the `libva-vdpau-driver`
controller. According to the error message, it couldn't find the installation
and therefore couldn't configure virtual cameras, although the controller was
installed. This is a common issue, according to forums, but I didn't find
anything that helped solve it.

## Leisure time

My entertainment 3-in-1 combo is Spotify, Stremio, and Steam (in that order of
use). Spotify has become my go-to option for passing the time while working from
home and in the absence of other sounds, I need to have at least some music or a
podcast. Stremio is my alternative to streaming services
([](/en/blog/2024/la-mejor-alternativa-gratis-a-netflix.md)) and on Steam, I
have good times with my collection of
[video games](/en/blog/2024/proton-modo-de-compatibilidad-de-steam.md) and
[retro games](/en/blog/2021/configurar-retroarch-en-steam.rst).

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code}
sudo pamac install steam --no-confirm
pamac build spotify --no-confirm
flatpak install -y flathub com.stremio.Stremio
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code}
flatpak install -y flathub com.valvesoftware.Steam
flatpak install -y flathub com.stremio.Stremio
sudo snap install spotify
```

````
`````

## Now look at the sky

A small bonus for astronomy enthusiasts.

The installation of the planetarium software Stellarium and a 3D universe
visualization tool, Gaia Sky.

```{code}
flatpak install flathub org.stellarium.Stellarium
flatpak install flathub de.uni_heidelberg.zah.GaiaSky
```
