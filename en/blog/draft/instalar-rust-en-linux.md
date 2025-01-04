---
date: 2024-06-15
tags: rust, rustlang, vscode, notebook, evcxr, rust-analyzer
category: technology
language: en
---

# Instalar Rust en Linux

En mi proceso por aprender Rust, iré compartiendo algunos pasos con ustedes. En
esta ocasión, como instalar Rust en Linux, y prepararnos para usarlo en VSCode y
en Notebook.

[Rust](https://www.rust-lang.org/) es un lenguaje de bajo nivel, desarrollado
con el patrocinio de Mozilla, enfocado en el rendimiento y seguridad, con muy
buenas validaciones en tiempo de compilación que nos ayudará a prevenir algunos
errores en tiempo de ejecución. Por diseño, intenta dar mayor ergonomía que un
lenguaje de bajo nivel, al tiempo que permite un mayor control.

## Instalación

La [instalación recomendada](https://www.rust-lang.org/tools/install) es con la
herramienta _rustup_, para esto procedemos con

```{code} bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Esto descarga _rustup_, e inicia el proceso de instalación de Rust y otras
utilidades. Allí podemos aceptar la opción por defecto con _enter_.

Así tendremos instalados [`cargo`](https://doc.rust-lang.org/cargo/) (el gestor
de paquetes de Rust), [`clippy`](https://doc.rust-lang.org/clippy/) (el linter
integrado de Rust), `rust-docs` (documentación de Rust),
[`rust-std`](https://doc.rust-lang.org/std/) (la biblioteca estándar de Rust),
[`rustc`](https://doc.rust-lang.org/rustc/what-is-rustc.html) (el compilador de
Rust) y [`rustfmt`](https://github.com/rust-lang/rustfmt) (el formateador de
código Rust). Y por supuesto, el mismo
[`rustup`](https://rust-lang.github.io/rustup/) que nos permite gestionar el
_toolchain_ de Rust.

Respecto a _cargo_, hay que decir algo interesante, y es que el gestor integra
la ejecución de pruebas (`cargo test`) que es una opción también del compilador,
y la generación de documentación (`cargo doc`) con
[`rustdoc`](https://doc.rust-lang.org/rustdoc/index.html).

Ahora terminamos con

```{code} bash
source "$HOME/.cargo/env"
```

Esto nos permite asociar las variables de ambiente necesarias en la consola
actual.

Si ahora ejecutamos `rustc --version`, debemos ver la versión del compilador. Si
no lo ves, puede que hayas omitido el paso anterior para asociar la variable de
entorno.

Cuando deseemos actualizar la versión del compilador, usaremos `rustup update`.

## Configurar VSCode

Para tener la ayuda necesaria en nuestra IDE de VSCode al programar en Rust,
vamos a instalar la extensión [rust-analyzer](https://rust-analyzer.github.io).
Esta extensión nos provee de opciones de autocompletado, ir a definiciones,
búsqueda de referencias, acceso a documentación, resaltado semántico, asistencia
y sugerencias. Esto lo tenemos como beneficio gracias a la implementación del
LSP (_Language Server Protocol_) para Rust.

_Rust Analyzer_ se encuentra disponible también para otros editores.

Podemos iniciar con un pequeño proyecto por defecto para ver la extensión en
acción, así como nuestra instalación base. Para crear un nuevo, usamos

```{code} bash
cargo new miniproyecto
```

Esto crea una plantilla básica de proyecto de aplicación Rust, con los archivos
de dependencias de Cargo y el directorio de fuente con un hola mundo. Podemos
usar un código básico errónea y verlo en acción.

```{figure} /images/instalar-rust-en-linux/rust-analyzer.png
---
alt: Diagnóstico de rust analyzer sugiriendo el uso de let para asignar una variable
align: center
width: 800px
height: 400px
---
   Diagnóstico de rust analyzer sugiriendo el uso de let para asignar una variable.
```

## Rust Notebook

Ahora, tenemos opción de agregar un _kernel_ Rust a Jupyter Notebook para tener
una experiencia interactiva de Rust, mezclada con el beneficio de documentar de
forma natural. Esto lo podemos lograr gracias al _kernel_
[Evcxr](https://github.com/evcxr/evcxr).

Instalamos con _cargo_ la dependencia necesaria primero.

```{code} bash
cargo install --locked evcxr_jupyter
```

Una vez instalado, debemos tener en cuenta de tener activo el ambiente en el que
disponemos nuestra instalación de Jupyter Notebook (en caso de tenerlo en un
ambiente). Si no tenemos instalado, en Ubuntu podemos proceder como:

```{code} bash
sudo apt install -y jupyter-notebook
```

O con el gestor de paquetes de Python (instalamos también jupyterlab), como:

```{code} bash
pip install notebook jupyterlab
```

Ahora, agreguemos el _Kernel_ a Notebook.

```{code} bash
evcxr_jupyter --install
```

Una vez agregado, podemos abrir Notebook o Jupyterlab, y veremos la opción para
usar Rust.

```{code} bash
jupyter notebook  # Abrir notebook
jupyter lab  # Abrir Jupyterlab (recomendado)
```

```{figure} /images/instalar-rust-en-linux/jupyter-evcxr.png
---
alt: Disponibilidad de Rust como Kernel en Jupyter Notebook
align: center
width: 800px
height: 400px
---
   Disponibilidad de Rust como Kernel en Jupyter Notebook
```

```{figure} /images/instalar-rust-en-linux/jupyter-cells-rust.png
---
alt: Ejemplo básico de asignación de variable de Rust en Notebook
align: center
width: 800px
height: 400px
---
   Ejemplo básico de asignación de variable de Rust en Notebook
```
