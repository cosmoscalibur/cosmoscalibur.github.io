```{code-block} bash
pamac checkupdates -a

# Similar a apt update -q && apt dist-upgrade -y
pamac upgrade
pamac upgrade -a  # Si deseamos usar AUR

pamac search
pamac search -a # Incluye opciones del AUR

pamac install --no-confirm base-devel  # Similar a build-essential
pamac build dropbox google-chrome  --no-confirm  # No es necesario manual como en ubuntu. Dropbox listo para login
pamac build spotify --no-confirm  # En Ubuntu necesitamos snap o agregar ppa
pamac build slack-desktop --no-confirm  # En ubuntu es snap o descarga manual
pamac install --no-confirm telegram-desktop discord # En ubuntu con snap o manual
```

flatpak remote-add --if-not-exists flathub
https://flathub.org/repo/flathub.flatpakrepo

Activar teclado numérico desde booteo
https://wiki.archlinux.org/title/Activating_numlock_on_bootup#KDE_Plasma
