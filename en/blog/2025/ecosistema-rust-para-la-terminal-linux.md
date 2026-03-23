---
date: 2026-03-23
tags: rustlang, terminal, manjaro, kde, linux applications
category: technology, linux
language: en
---

# Rust Ecosystem for the Linux terminal

Besides my personal interest in this language, I am also interested in the
ecosystem of tools that have been developed in Rust for the Linux terminal
and for supporting other programming languages (like its impact on Python,
which is my main development language).

I previously told you about
[Starship](/en/blog/2024/configurar-starship-en-manjaro-y-zsh.md), and next
we are going to expand this universe of Rust possibilities for the Linux terminal.

## Accelerate your work in the terminal

While *Zsh* is not implemented in Rust, this terminal language (*shell*)
is very powerful and flexible, with a large number of plugins available
to customize and improve its experience. So I take advantage as part of
my newly reloaded Linux terminal to include it and tell you about how to switch
to using it by default. Additionally, this is necessary to mention since, the
configuration will require knowing our *shell*, and this defines why the
instructions we are going to learn. I still use it like a general *bash*,
but I have already seen very interesting things that I will soon share.

Just as we saw the extra information experience that Starship offers us,
we are going to explore utilities that help us improve our fast experience in the
terminal with greater agility in our workflows.

We will start with *zoxide*, a replacement for `cd` that allows us to navigate through
our directory history faster and more efficiently. It has
autocomplete and priority assignment for directory shortcuts.
We can use it by indicating a short form of the directory or similar, and through
fuzzy search in the directories we have already navigated (using *zoxide* as
a usual `cd`) it can guess the directory we are looking for, or if we know that
there can be several directories with the same name, it can show a list
of options to choose from when typing space and tab.

We can also speed up our experience with a terminal emulator in Rust
like *Alacritty*, which offers a faster and more efficient interface than the default
Linux terminal, and its rendering is with OpenGL. This emulator is
also available on MacOS and Windows, and has a *Vi* mode for
navigation, as well as extended selection options and opening links with
the _mouse_.

*Alacritty* does not have a multiplexer, but we can give it this capability
through *Zellij*, a terminal multiplexer (this allows us to have
multiple windows and panes within a single terminal). We can have floating panes,
custom layers and a series of shortcuts to do proper
navigation. A lock mode is available to avoid confusion with system shortcuts,
and this is used with {kbd}`Ctrl+g`, and there the shortcuts {kbd}`p` for
pane management or {kbd}`t` for tab management, and with options to
create ({kbd}`n`), close ({kbd}`x`), navigate (arrows), among others.
We can generate floating panes with {kbd}`Alt+f` (which can then be
moved with the *mouse*) or normal panes with {kbd}`Alt+n`. To
navigate in this mode, we can use {kbd}`Alt` with arrows.

And finally, a terminal editor with *Vi* mode support, quite
comfortable to use and with native *tree sitter* and *LSP* support. This editor is
*Helix*. And it has become my favorite terminal editor and I have linked it
as the editor for git editing.

Now, let's get down to business to install and configure.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

In Manjaro (and Arch derivatives) we have the necessary packages in the
official repository.

```{code} bash
pamac install zsh alacritty zellij zoxide helix --no-confirm
pamac install --as-deps fzf --no-confirm  # Interactive search for zoxide
```
````
````{tab-item} Ubuntu
:sync: ubuntu

In the case of Ubuntu, we will need to use not only packages from the official
repository, but also packages installed with [{program}`cargo`](/en/blog/2024/instalar-rust-en-linux.md) or [{program}`flatpak`](/en/blog/2024/que-hacer-despues-de-instalar-manjaro.md#ubuntu-instalar-flatpak).

```{code} bash
sudo apt install -y zsh alacritty zoxide fzf
cargo install --locked zellij
flatpak install flathub com.helix_editor.Helix
```
````
`````

To configure {program}`zsh` as your default *shell* we proceed as
follows:

```{code} bash
chsh -s /bin/zsh  # Configure default shell: enter password
```

You may need to restart your session for the change to take effect. Then,
we can configure the other utilities that depend on the
*shell* to know the configuration options.

*Zoxide* requires executing its initialization *script* indicating the *shell*
that is being used. Depending on the installation method, you might need to check the
associated executable, in my case it stays as `z` and I feel comfortable with it.

```{code} bash
echo 'eval "$(zoxide init zsh)"' >> ~/.zshrc
source ~/.zshrc
```

In the case of *Alacritty*, we must indicate the *shell* that is being used in the
configuration file (TOML format) and incidentally we will link the use of
*Zellij* at its startup.

```{code} bash
mkdir -p $HOME/.config/alacritty
cat << 'EOF' > $HOME/.config/alacritty.toml
[terminal.shell]
args = ["-l", "-c", "zellij attach --index 0 || zellij"]
program = "/bin/zsh"
EOF
```

Regarding the use of *Zellij*, I recommend the *unlock first* mode to avoid
collision of shortcuts that we have in the system (it is a bad experience). To configure it, inside a Zellij session, press {kbd}`Ctrl+o` followed by {kbd}`C` to open the configuration, then use {kbd}`Tab`, down arrow to option 2 ("Unlock First"), and finally {kbd}`Alt+a` to save the changes.

Remember also to configure
[starship](/en/blog/2024/configurar-starship-en-manjaro-y-zsh.md) so you
have the complete combo.

Finally, for *Helix* to be your default editor in the console, you must configure the `EDITOR` environment variable. You can append it to your *shell* configuration:

```{code} bash
echo 'export EDITOR=helix' >> ~/.zshrc
source ~/.zshrc
```

### Associate Alacritty as default terminal in KDE.

At this point we have the basics ready, and if you launch directly
{program}`alacritty` nothing else is needed. However, if you use terminal
shortcuts or there are applications that launch the terminal that is associated by
default, they will continue to launch the terminal (emulator) that you had before. So that
this does not happen, you will have to do some additional steps that depend on your desktop
environment. In my case, since I use KDE, the steps are the following.

To link *alacritty* as the default terminal emulator:
{menuselection}`Default Applications --> Terminal emulator --> Alacritty`

To configure the keyboard shortcut:
{menuselection}`Custom Shortcuts --> Add new --> Application --> Alacritty`
We configure the "Launch" shortcut by clicking {guilabel}`Add`, and after that the
desired shortcut. In my case I prefer the usual terminal one
{kbd}`Control-Alt-T`. We apply the change ({guilabel}`Apply`).

## New ecosystem of utilities

We have here a replacement for our favorite console commands, which
we take advantage to modernize with Rust and in some cases to have an important
performance improvement (in their reimplementation) or of agility with the new
options they offer us.

- `bat`: Replacement for `cat`. I highlight its syntax coloring, git change
  marks and the option to show invisible characters.
- `bottom` (`btm`): Replacement for `top`. It has cross-platform support and
  process management allows you to kill them there (you select the process and then
  {kbd}`d d`)
- `eza`: Replacement for `ls`. I haven't explored much of its potential yet, but its
  default coloring is much more useful to me than the original one.
  It allows knowing additional information of the files and directories during the
  query, such as their git status or mount point information.
- `procs`: Replacement for `ps`. Cross-platform, and with better readability than the
  original.
- `du-dust` (`dust`): Replacement for `du`. Its default visualization seems
  much more informative than the original command.

Now, let's proceed to install.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

In Manjaro (and Arch derivatives), we again have everything available in the official repository.

```{code} bash
pamac install bat bottom dust eza procs --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

In Ubuntu, we will need to mix the official repository with the Rust repository.

```{code} bash
sudo apt install -y bat du-dust eza
cargo install --locked bottom procs
```
````
`````

## References

Now that we have *rusted* our Linux terminal, I invite you to visit the
official information of these projects.

- [Alacritty](https://alacritty.org/)
- [Zellij](https://zellij.dev/)
- [Zoxide](https://github.com/ajeetdsouza/zoxide)
- [zsh](https://www.zsh.org/)
- [Oh my zsh](https://ohmyz.sh/)
- [Helix](https://helix-editor.com/)
- [Dust](https://github.com/bootandy/dust)
- [Eza](https://eza.rocks/)
- [procs](https://github.com/dalance/procs)
- [Bat](https://github.com/sharkdp/bat)
- [Bottom](https://github.com/ClementTsang/bottom)

You can learn more Rust utilities for your console
[here](https://github.com/sts10/rust-command-line-utilities).
