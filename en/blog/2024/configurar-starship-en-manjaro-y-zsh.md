---
date: 2024-12-15
tags: zsh, bash, ubuntu, manjaro, starship, shell, rust
category: technology, linux
language: en
---

# Configuring *Starship* on Manjaro and Zsh

Recently, I've been switching multiple tools in my daily work, including changes
in handling the Linux terminal. One of these changes is the *shell prompt* (the
terminal indicator), and I'm using {program}`starship`. However, there are some
undocumented details on how to enable it on Manjaro with {program}`zsh`, which
I'll explain here.

```{figure} /images/configurar-starship-en-manjaro-y-zsh/indicador-starship.png
---
alt: A visual appearance of *Starship* messages for Git, Python, and low battery.
align: center
width: 500px
height: 250px
---
   Appearance of the *Starship* indicator in a Git directory with a Python environment, and with a low battery indication.
```

To start, first, a terminal indicator is a program that generates text
associated with each command execution in the terminal, along with what comes
before the cursor. A good terminal indicator provides us with useful information
quickly about the directory we are in, the execution of a command line, or even
the battery level. *Starship* delivers this and forms part of the new ecosystem
of utilities developed in Rust.

## Installing *Starship*

In Manjaro, you have [*starship*](https://starship.rs/) available in the
official repository, but you can also install it from the official installation
routine that applies to any Linux distribution (useful if you use a distro like
Ubuntu).

`````{tab-set}
````{tab-item} Manjaro
:sync: m

```{code} bash
sudo pamac install starship --no-confirm
```

````

````{tab-item} Ubuntu
:sync: u

```{code} bash
curl -sS https://starship.rs/install.sh | sh
```
````

`````

## Starting *Starship*

When using {program}`zsh`, you can initialize it by adding the `init` command to
the {file}`~/.zshrc` file.

`````{tab-set}
````{tab-item} zsh

```{code} bash
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
source ~/.zshrc
```

````

````{tab-item} bash

The default terminal language is {program}`bash`, and if you are comfortable with this, initializing it looks like this.

```{code} bash
echo 'eval "$(starship init bash)"' >> ~/.bashrc
source ~/.bashrc
```

````
`````

Finally, we are ready, or at least according to the official procedure.

In Manjaro, {program}`zsh` has a default terminal indicator configuration in the
file {file}`~/.zshrc` and in the file {file}`/usr/share/zsh/manjaro-zsh-prompt`.
This configuration enables *powerline* and *powerlevel10k* (*p10k*) and avoids
using an additional prompt.

It's necessary to disable the use of these two. To do this, we must set
`USE_POWERLINE` to `false` and comment out (or delete) the lines of the `prompt`
configuration.

```{code-block} text
---
emphasize-lines: 2, 12-14
---
# Use powerline
USE_POWERLINE="false"
# Has weird character width
# Example:
#    is not a diamond
HAS_WIDECHARS="false"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
#if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
#  source /usr/share/zsh/manjaro-zsh-prompt
#fi
```

After sourcing the `.zshrc` file, you should have *starship* enabled on Manjaro
with *Zsh*.

```{code} bash
source ~/.zshrc
```

## Configuration File

In general, the default configuration is good and significant changes are not
necessary. However, the {program}`gcloud` module shows up generally in the
session which is not appealing or useful for me. For this reason, I create the
configuration file {file}`~/.config/starship.toml` and disable the module.

```{code} bash
cat << 'EOF' > ~/.config/starship.toml
[gcloud]
disabled = true
EOF
```

You can consult other configuration options in
[Starship: Configuration](https://starship.rs/config/).

## References

- [GitHub: Starship](https://github.com/starship/starship)
- [Starship prompt won’t work on manjaro KDE plasma](https://forum.manjaro.org/t/starship-prompt-wont-work-on-manjaro-kde-plasma/83608).
- [Starship prompt for zsh - need help installing](https://forum.manjaro.org/t/starship-prompt-for-zsh-need-help-installing/93481).
- [Powerline in manjaro-zsh-config](https://forum.manjaro.org/t/powerline-in-manjaro-zsh-config/42941).
- [Powerline](https://github.com/powerline/powerline).
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k).
