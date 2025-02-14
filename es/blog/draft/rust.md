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
ejecución (`cargo run`). Puedes usar proyectos con múltiples binarios si en el
directorio {file}`src` añadimos otros archivos fuentes. Estos, {program}`cargo`
los puede inferir y crear los binarios, y si deseamos ejecutarlos bastará con
usar `cargo run` seguido de `--bin` y el nombre (por defecto es el nombre del
archivo sin extensión).

Sobre la organización general de archivos, puedes consultar en
[Package Layout](https://doc.rust-lang.org/cargo/guide/project-layout.html) de
*The Cargo Book*, y la configuración si no deseamos los nombres por defecto de
los binarios en
[Cargo Targets](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#configuring-a-target).

Se puede compilar directamente el código fuente sin `cargo` usando `rustc`
seguido de la ruta del código fuente.

```{hint}
Una instrucción interesante es `cargo check`, la cual te permitirá verificar si
el código es compilable sin necesidad de generar el ejecutable. Esto es mucho
más rápido y en ocasiones no necesitamos hacer la prueba de ejecución, sino solo
saber si puede generar errores de compilación.
```

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

## Asignación de variables y constantes

Para asignar variables usamos `let` seguido del nombre de la variable, `:` el
tipo de dato (aunque este puede ser inferido y no anotarse siempre), `=` y el
valor de la variable (y por supuesto, el terminador de línea). En Rust, las
variables por defecto son inmutable, lo cual implica que una vez se asigna el
valor, este no puede ser modificado. Si queremos que el valor sea modificable,
debemos agregar `mut` antes del nombre de la variable.

También podemos asignar constantes con la palabra clave `const`, y estas siempre
son inmutables y siempre deben anotar el tipo. Su estructura es `const` seguido
del nombre de la constante en mayúscula sostenida (puede contener guion bajo),
`:`, el tipo de dato, el valor y el terminador de línea. Las constantes pueden
ser asignadas con expresiones que se calculan en tiempo de compilación (esto nos
ayuda a la legibilidad y verificación de un valor, en lugar de poner su valor
directo), y a diferencia de las variables pueden ser de contexto global, útil
para valores que son requeridos en múltiples partes de nuestro código.

```{code} rust
const ANSWER: i32 = 42;

fn main() {
    let x: i32 = 26;
    let mut y: f32 = 5.6;
    y = 8.;
    let suma = x + ANSWER;
    println!("Mi primera variable 'x': {x}");
    println!("Mi primera variable mutable 'y': {y}");
    println!("Sumando {suma}")
}
```

Los tipos de datos podemos consultarlos en la sección de conceptos comunes de
programación del libro de Rust en
[Data types](https://doc.rust-lang.org/book/ch03-02-data-types.html).

## Referencias

- [The Rust Programming Language](https://doc.rust-lang.org/book/).
- [The Cargo Book](https://doc.rust-lang.org/cargo/index.html).
- [Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/index.html).
