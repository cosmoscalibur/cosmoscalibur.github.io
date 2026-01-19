---
date: 2025-04-29
tags: rustlang, terminal, manjaro, kde, aplicaciones para linux
category: tecnología, linux
---

# Ecosistema Rust para la terminal Linux

Además de mi interés personal por este lenguaje, también me interesa el
ecosistema de herramientas que se han desarrollado en Rust para la terminal
Linux y para el soporte de otros lenguajes de programación (como su impacto en
Python, que es mi lenguaje principal de desarrollo).

Antes les comenté sobre
[Starship](/es/blog/2024/configurar-starship-en-manjaro-y-zsh.md), y a
continuación vamos a expandir este universo de posibilidades de Rust para la
terminal Linux.

## Acelera tu trabajo en la terminal

Si bien *Zsh* no está implementado en Rust, este lenguaje de terminal (*shell*)
es muy potente y flexible, con una gran cantidad de complementos disponibles
para personalizar y mejorar su experiencia. Por lo que aprovecho como parte de
mi nueva terminal Linux recargada a incluirlo y contarles sobre como cambiar a
que sea usado por defecto. Adicional, esto es necesario mencionarlo ya que, la
configuración va a requerir de conocer nuestra *shell*, y esto define porque las
instrucciones que vamos a conocer. Todavía lo sigo usando como un *bash* en
general, pero ya he visto cosas muy interesantes que pronto les compartiré.

Así como vimos la experiencia extra de información que nos ofrece Starship,
vamos a explorar utilidades que nos ayudan a mejorar nuestra experiencia en la
terminal con mayor agilidad en nuestros flujos de trabajo.

Empezaremos con *zoxide*, un reemplazo para `cd` que nos permite navegar por
nuestra historia de directorios de forma más rápida y eficiente. Posee
autocompletado y asignación de prioridad para los atajos a los directorios.
Podemos usarlo indicando una forma corta del directorio o similar, y mediante
búsqueda difusa en los directorios que ya hemos navegado (usando *zoxide* como
un `cd` habitual) puede adivinar el directorio que buscamos, o si sabemos que
pueden existir varios directorios con el mismo nombre, puede mostrar una lista
de opciones para elegir al digitar espacio y tabulador.

Podemos también acelerar nuestra experiencia con un emulador de terminal en Rust
como *Alacritty*, que ofrece una interfaz más rápida y eficiente que la terminal
predeterminada de Linux, y su renderizado es con OpenGL. Este emulador está
disponible también en MacOS y Windows, y dispone de modo *Vi* para la
navegación, así como opciones de selección extendida y apertura de enlaces con
el _mouse_.

*Alacritty* no posee un multiplexador, pero podemos darle esta capacidad a
través de *Zellij*, un multiplexador de terminales (esto nos permite tener
múltiples ventanas y paneles dentro de una sola terminal). Podemos tener paneles
flotantes, capas personalizadas y una serie de atajos para hacer adecuada
navegación. Se dispone de un modo de bloqueo para evitar la confusión con atajos
de sistema, y este se usa con {kbd}`Ctrl+g`, y allí los atajos {kbd}`p` para
gestión de paneles o {kbd}`t` para la gestión de pestañas, y con opciones para
crear ({kbd}`n`), cerrar ({kbd}`x`), navegar (direccionales), entre otros.
Podemos generar los paneles flotantes con {kbd}`Alt+f` (los cuales se pueden
desplazar luego con el *mouse*) o los paneles normales con {kbd}`Alt+n`. Para
navegar en este modo, podemos usar {kbd}`Alt` con direccionales.

Y finalmente, un editor para la terminal con soporte de modo *Vi*, bastante
cómodo de usar y con soporte nativo de *tree sitter* y *LSP*. Este editor es
*Helix*. Y se ha convertido en mi editor de terminal favorito y lo he vinculado
como el editor para edición de git.

Ahora, manos a la obra para instalar y configurar.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

En Manjaro (y derivadas de Arch) disponemos de los paquetes necesarios en el
repositorio oficial.

```{code} bash
sudo pamac install zsh alacritty zellij zoxide helix --no-confirm
sudo pamac --as-deps fzf --no-confirm  # Búsqueda interactiva de zoxide
```
````
````{tab-item} Ubuntu
:sync: ubuntu

En el caso de Ubuntu, vamos a necesitar usar no solo paquetes del repositorio
oficial, sino también paquetes instalados con [{program}`cargo`](/es/blog/2024/instalar-rust-en-linux.md) o [{program}`flatpak`](#ubuntu-instalar-flatpak).

```{code} bash
sudo apt install -y zsh alacritty zoxide fzf
cargo install --locked zellij
flatpak install flathub com.helix_editor.Helix
```
````
`````

Para configurar {program}`zsh` como tu *shell* por defecto procedemos de la
siguiente manera:

```{code} bash
chsh -s /bin/zsh  # Configurar shell por defecto: ingresamos contraseña
```

Puede que sea necesario reiniciar tu sesión para que el cambio surta efecto. A
continuación, ya podremos configurar las demás utilidades que dependen del
*shell* para saber las opciones de configuración.

*Zoxide* requiere ejecutar su *script* de inicialización indicando el *shell*
que se está usando. Según el método de instalación, podrías necesitar revisar el
ejecutable asociado, en mi caso queda con `z` y me siento cómodo con él.

```{code} bash
echo 'eval "$(zoxide init zsh)"' >> ~/.zshrc
source ~/.zshrc
```

En el caso de *Alacritty*, debemos indicar el *shell* que se está usando en el
archivo de configuración (formato TOML) y de paso vincularemos el uso de
*Zellij* en su arranque.

```{code} bash
cat << 'EOF' > ~/.config/alacritty.toml
[terminal.shell]
args = ["-l", "-c", "zellij attach --index 0 || zellij"]
program = "/bin/zsh"
EOF
```

Respecto al uso de *Zellij* te recomiendo el modo *unlock first* para evitar
colisión de atajos que tengamos en el sistema (es una mala experiencia).

Recuerda también configurar
[starship](/es/blog/2024/configurar-starship-en-manjaro-y-zsh.md) para que
tengas el combo completo.

### Asociar Alacritty como terminal por defecto en KDE.

En este punto ya tenemos lo básico listo, y si lanzas de forma directa
{program}`alacritty` no hace falta nada más. Sin embargo, si usas atajos de
terminal o hay aplicaciones que lancen la terminar que esté asociada por
defecto, seguirán lanzando la terminal (emulador) que tenías antes. Para que
esto no suceda, deberás hacer unos pasos adicionales que dependen de tu entorno
de escritorio. En mi caso, que uso KDE los pasos son los siguientes.

Para vincular *alacritty* como emulador de terminal por defecto:
{menuselection}`Aplicaciones predeterminadas --> Emulador de terminal --> Alacritty`

Para configurar el atajo de teclado teclado:
{menuselection}`Atajos de teclado --> Añadir nuevo --> Aplicación --> Alacritty`
Configuramos atajo de "Lanzar" dando clic a {guilabel}`Añadir`, y tras ello el
atajo deseado. En mi caso prefiero el habitual de la terminal de
{kbd}`Control-Alt-T`. Aplicamos el cambio ({guilabel}`Aplicar`).

## Nuevo ecosistema de utilidades

Tenemos aquí un reemplazo para nuestros comandos favoritos de la consola, que
aprovechamos a modernizar con Rust y en algunos casos a tener una mejora
importante de rendimiento (en su reimplementación) o de agilidad con las nuevas
opciones que nos ofrecen.## Nuevo ecosistema de utilidades

- `bat`: Sustituto de `cat`. Destaco su coloreado de sintaxis, marcas de cambios
  de git y la opción para mostrar caracteres invisibles.
- `bottom` (`btm`): Sustituto de `top`. Posee soporte multiplataforma y la
  gestión de procesos te permite matarlos allí (seleccionas el proceso y luego
  {kbd}`d d`)
- `eza`: Sustituto de `ls`. No he explorado mucho su potencial, pero su
  coloreado por defecto me es mucho más útil que el usado en el original.
  Permite conocer información adicional de los archivos y directorios durante la
  consulta, como su estado de git o información de puntos de montaje.
- `procs`: Sustituto de `ps`. Multiplataforma, y con mayor legibilidad que el
  original.
- `du-dust` (`dust`): Sustituto de `du`. Su visualización por defecto me parece
  mucho más informativa que el comando original.

Ahora, procedamos a instalar.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

En Manjaro (y derivados de Arch), disponemos nuevamente todo disponible en el repositorio oficial.

```{code} bash
sudo pamac install bat bottom dust eza procs --no-confirm
```

````
````{tab-item} Ubuntu
:sync: ubuntu

En Ubuntu, necesitaremos mezclar el repositorio oficial con el repositorio de Rust.

```{code} bash
sudo apt install -y bat du-dust eza
cargo install --locked bottom procs
```
````
`````

## Referencias

Ahora que hemos *oxidado* nuestra terminal Linux, te invito a visitar la
información oficial de estos proyectos.

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

Puedes conocer más utilidades en Rust para tu consola
[aquí](https://github.com/sts10/rust-command-line-utilities).
