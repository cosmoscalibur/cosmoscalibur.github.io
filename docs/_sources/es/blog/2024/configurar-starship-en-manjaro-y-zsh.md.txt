---
date: 2024-12-15
tags: zsh, manjaro, starship, shell prompt, utilidades en rust
category: tecnología, linux
---

# Configurar *Starship* en Manjaro y Zsh

Hace poco vengo cambiando múltiples herramientas en mi día a día, y en el
manejo de la terminal Linux hay varios de esos cambios. Uno de esos es el
*shell prompt* (que podría traducirse tal vez como "indicador de terminal"),
y estoy usando {program}`starship`. Sin embargo, hay detalles no documentados
sobre como habilitarlo en Manjaro con {program}`zsh`, que aquí les cuento.

:::{figure} /images/configurar-starship-en-manjaro-y-zsh/indicador-starship.png
   :alt: Apariencia visual de mensajes del indicador starship en la terminal para git, python y batería baja.
   :align: center
   :width: 500px
   :height: 250px

   Apariencia del indicador *Starship* en un directorio *git* con ambiente
   Python, y con indicación de batería baja.
:::

Para empezar, primero, un indicador de terminal es un programa que genera los
textos asociados a cada ejecución de comandos en la terminal y lo que hay
antes del cursor. Un buen indicador de terminal nos aporta información útil
rápidamente del directorio en el cual nos ubicamos, de la ejecución de una
línea de comandos o incluso la batería. Starship nos entrega esto, y hace parte
del nuevo ecosistema de utilidades desarrolladas en rust.

## Instalar *Starship*

En Manjaro, disponemos de [*starship*](https://starship.rs/) en el repositorio
oficial, pero igual puedes instalar a partir de la rutina de instalación
oficial que aplica a cualquier distribución Linux (útil si usas una distro
como Ubuntu).

::::{tab-set}
:::{tab-item} Manjaro
:sync: m

```{code} bash
sudo pamac install starship --no-confirm
```

:::
:::{tab-item} Ubuntu
:sync: u

```{code} bash
curl -sS https://starship.rs/install.sh | sh
```
:::
::::

## Iniciar *Starship*

Al usar {program}`zsh`, la inicialización la podemos hacer añadiendo el
`init` al archivo {file}`~/.zshrc`.

::::{tab-set}
:::{tab-item} zsh

```{code} bash
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
source ~/.zshrc
```

:::
:::{tab-item} bash

El lenguaje de terminal por defecto es {program}`bash` y si estás cómodo con
este, la forma de inicializar es la siguiente.

```{code} bash
echo 'eval "$(starship init bash)"' >> ~/.bashrc
source ~/.bashrc
```

:::
::::

Finalmente, estamos listos, o al menos, según el procedimiento oficial.

En Manjaro, {program}`zsh` posee una configuración predeterminada para el
indicador de terminal, en el archivo {file}`~/.zshrc` y en el archivo
{file}`/usr/share/zsh/manjaro-zsh-prompt`. Esta configuración es para
habilitar *powerline* y *powerlevel10k* (*p10k*) y evita el uso de un *prompt*
adicional.

Es necesario deshabilitar el uso de estos dos. Para ello, debemos pasar a falso
el uso de *powerline* y comentar (o borrar) las líneas de la configuración
del *prompt*.

```{code-block} text
:emphasize-lines: 2, 12-14

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
eval "$(starship init zsh)"
```

Ahora, reconstruimos la configuración y tenemos *starship* en Manjaro con
*Zsh*.

```{code} bash
source ~/.zshrc
```

## Archivo de configuración

En general, la configuración por defecto es buena y no hay una necesidad de
cambios fuertes. Sin embargo, el módulo de `gcloud` se muestra en general en
la sesión lo cual no me es agradable y poco útil en mi caso. Por este motivo
creo el archivo de configuración {file}`~/.config/starship.toml` y deshabilito
el módulo.

```{code} bash
cat << 'EOF' > ~/.config/starship.toml
[gcloud]
disabled = true
EOF
```

Puedes consultar otras opciones de configuración en
[Starship: Configuration](https://starship.rs/config/).

## Referencias

+ [GitHub: Starship](https://github.com/starship/starship)
+ [Starship prompt won’t work on manjaro KDE plasma](https://forum.manjaro.org/t/starship-prompt-wont-work-on-manjaro-kde-plasma/83608).
+ [Starship prompt for zsh - need help installing](https://forum.manjaro.org/t/starship-prompt-for-zsh-need-help-installing/93481).
+ [Powerline in manjaro-zsh-config](https://forum.manjaro.org/t/powerline-in-manjaro-zsh-config/42941).
+ [Powerline](https://github.com/powerline/powerline).
+ [Powerlevel10k](https://github.com/romkatv/powerlevel10k).
