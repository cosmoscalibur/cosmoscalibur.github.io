# Rust

## Uso de `cargo`

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

Se puede compilar directamente el código fuente sin `cargo` usando `rustc`.

## Hola mundo en Rust

Los códigos ejecutables de Rust siempre requieren una función `main`. Las
funciones se especifican con `fn` seguido del nombre, los paréntesis para
argumentos, llave para el cuerpo de la función. Las líneas sentencias requieren
la terminación de `;`

```{code} rust
fn main(){
    println!("Hola, Edward! 🧠");
}
```

`println` es una macro (por eso termina en `!`) para imprimir, y esto nos ayuda
con el manejo de la existencia de múltiples argumentos.

## Asignación de variables

Para asignar variables usamos `let` seguido del nombre de la variable, `:` el
tipo de variable, `=` y el valor de la variable.

Los tipos de variables primitivos se pueden consultar en la documentación del
[*crate* `std`](https://doc.rust-lang.org/std/index.html#primitives).
