`cargo new proyecto` para crear proyecto nuevo con su directorio. Si el
directorio existe, usamos `cargo init` en el directorio para su inicialización.
La inicialización incluye un directorio `src` con un archivo `main.rs` con
ejemplo, un archivo de exclusión de git `.gitignore` (el sistema de
versionamiento se puede configurar con la opción `--vcs`) y el archivo de
proyecto `Cargo.toml`. El nombre del proyecto puede ser diferente al directorio,
y se puede pasar en la opción `--name`. Por defecto se usa la opción `--bin`
para la creación de un binario, pero puede ser `--lib` para generar una
biblioteca. Por defecto, es la edición 2021, pero se puede configurar con
`--edition` (ejemplo, usar la nueva edición, `2024`). Estas opciones son tanto
en la creación con `new` como en la inicialización con `init`.

El archivo de proyecto es necesario para la compilación (`cargo build`) o
ejecución (`cargo run`).
