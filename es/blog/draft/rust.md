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
    // Esto es un comentario de una línea
    println!("Hola, Edward! 🧠");
}
```

`println` es una macro (por eso termina en `!`) para imprimir, y esto nos ayuda
con el manejo de la existencia de múltiples argumentos.

Si deseamos agregar comentarios, esto se hace con `//` por cada línea.

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
    let bandera = true;
    println!("Mi primera variable 'x': {x}");
    println!("Mi primera variable mutable 'y': {y}");
    println!("Sumando {suma}")
}
```

Los tipos de datos que existen son los enteros sin signo y con signo (`u` y `i`,
seguido de `8`, `16`, `32`, `64` y `128` acorde al tamaño en bits), los
flotantes (`f32` y `f64`), los booleanos (`bool`, usan 1 *byte*) y los
caracteres (`char`, usan 4 *bytes*).

Si quieres conocer la sintaxis de los operadores en Rust, puedes consultar el
apéndice de la documentación oficial de Rust,
[Appendix B: Operators and Symbols](https://doc.rust-lang.org/book/appendix-02-operators.html).

Existen también tipos de datos compuestos:

- Tuplas: Es una agrupación de valores de diferentes tipos en un tipo compuesto
  que se concibe como uno. Para obtener sus valores, se puede usar la notación
  `x.N` donde `N` es el índice del elemento en la tupla, comenzando desde 0.
  También se puede desestructurar una tupla usando la sintaxis
  `let (a, b, c) = tupla;`. Una vez asignada, las tuplas no pueden cambiar su
  tamaño ni tipo de datos. Se asignan valores a las tuplas usando la sintaxis
  `let tupla = (1, 2.0, 'a');` o indicando de forma explícita el tipo de cada
  elemento `let tupla: (i32, f64, char) = (1, 2.0, 'a');`.

- Arreglos: Es una colección de elementos del mismo tipo y de tamaño fijo. Se
  asignan valores a los arreglos usando la sintaxis `let arreglo = [1, 2, 3];` o
  indicando de forma explícita el tipo de cada elemento
  `let arreglo: [i32; 3] = [1, 2, 3];`. También se puede crear un arreglo con
  valores repetidos usando la sintaxis `let arreglo = [0; 5];` que crea un
  arreglo de 5 elementos todos iguales a 0. Los elementos de un arreglo se
  pueden acceder usando la notación `arreglo[i]` donde `i` es el índice del
  elemento en el arreglo, comenzando desde 0. Se soporta la iteración sobre el
  arreglo mediante la notación valor inicial seguido de `..` (con `..=` indica
  que el valor final está incluido) y el valor final. Y con `step_by` para
  iterar con un paso específico (similar a `range` en Python).

- Vectores: Son colecciones de elementos del mismo tipo y de tamaño variable (un
  comparativo con las listas de Python). Se asignan valores a los vectores
  usando la sintaxis `let vector = vec![1, 2, 3];` que es una macro, o
  `let vector = Vec::new();` (o indicando explícitamente el tipo de cada
  elemento `let vector: Vec<i32> = Vec::new();`) que es una función y asignando
  los valores usando la sintaxis `vector.push(4);`. Se puede acceder a los
  elementos de un vector usando la notación `vector[i]` donde `i` es el índice
  del elemento en el vector, comenzando desde 0.

- *Hash map*: Es una colección de pares clave-valor donde las claves son únicas
  y los valores pueden ser de cualquier tipo (equivalente de diccionarios de
  Python). Se asignan valores a los *hash maps* usando la sintaxis
  `let hash_map = HashMap::new();` que es una función y asignando los valores
  usando la sintaxis `hash_map.insert("clave", valor);`. Se puede acceder a los
  valores de un hash map usando la notación `hash_map["clave"]` donde `clave` es
  la clave del valor que se quiere obtener. Es necesario importar el módulo
  `std::collections::HashMap` para usar *hash maps*. Se dispone de una
  alternativa *pythonica* usando el *crate* de `maplit` con la macro `hashmap!`.

  ```{code} rust
  #[macro_use] extern crate maplit;

  let map = hashmap!{
      "daffy" => 80,
      "bugs" => 79,
      "taz" => 63,
  };
  ```

- *Hash set*: Es una colección de elementos únicos sin orden específico
  (equivalente de conjuntos de Python). Se asignan valores a los *hash sets*
  usando la sintaxis `let hash_set = HashSet::new();` que es una función y
  asignando los valores usando la sintaxis `hash_set.insert(elemento);`. Es
  necesario importar el módulo `std::collections::HashSet` para usar *hash
  sets*. Se dispone de una alternativa *pythonica* usando el *crate* de `maplit`
  con la macro `hashset!`.

  ```{code} rust
  #[macro_use] extern crate maplit;

  let set = hashset!{
      "daffy",
      "bugs",
      "taz",
  };
  ```

## Funciones en Rust

Cómo se mencionó anteriormente, en el ejemplo del "Hola mundo", las funciones se
definen iniciando por `fn`. En este caso, a diferencia del `main`, si una
función posee parámetros y retornos, se definen como sigue.

```{code} rust
fn suma(a: i32, b: i32) -> i32 {
    return a + b;
}
```

Es importante que en Rust, las funciones deben tener un tipo de retorno definido
explícitamente. Sin embargo, el `return` es opcional, y puede ser útil para el
retorno temprano, y se asume que el último valor de la función es el valor de
retorno.

## Flujos de control

### Condicionales

`if else` es una estructura de control que permite ejecutar diferentes bloques
de código dependiendo de si una condición es verdadera o falsa. En Rust, se
utiliza la palabra clave `if` seguida de una expresión booleana y luego un
bloque de código que se ejecutará si la condición es verdadera. Si se desea
ejecutar un bloque de código alternativo si la condición es falsa, se utiliza la
palabra clave `else` seguida de otro bloque de código.

```{code} rust
fn main() {
    let x = 5;

    if x < 10 {
        println!("x es menor que 10");
    } else {
        println!("x es mayor o igual que 10");
    }
}
```

Si es un condicional encadenado, se pueden utilizar múltiples `if` seguidos de
`else if` para evaluar múltiples condiciones.

```{code} rust
fn main() {
    let x = 5;

    if x < 10 {
        println!("x es menor que 10");
    } else if x == 10 {
        println!("x es igual a 10");
    } else {
        println!("x es mayor que 10");
    }
}
```

También disponemos de la estructura de control `match`, que permite comparar un
valor con una serie de patrones y ejecutar diferentes bloques de código según el
patrón coincidente.

```{code} rust
fn main() {
    let x = 5;

    match x {
        1 => println!("x es igual a 1"),
        2 => println!("x es igual a 2"),
        _ => println!("x es diferente de 1 y 2"),
    }
}
```

### Ciclos en Rust

Rust dispone de 3 tipos de estructuras cíclicas: `loop`, `while` y `for`. `loop`
es una estructura de control que permite ejecutar un bloque de código
indefinidamente hasta que se cumpla una condición (una salida manual por
interrupción de teclado o un `break`). `while` es una estructura de control que
permite ejecutar un bloque de código mientras una condición sea verdadera. `for`
es una estructura de control que permite iterar sobre una colección de
elementos.

La estructura general de estos 3 tipos de ciclos es la siguiente:

```{code} rust
loop {
    // Código a ejecutar indefinidamente
}

while condicion {
    // Código a ejecutar mientras la condición sea verdadera
}

for elemento in coleccion {
    // Código a ejecutar para cada elemento de la colección
}
```

Asociado a los ciclos, disponemos de las palabras clave `continue` y `break`,
que permiten controlar el flujo de ejecución dentro de los ciclos. `continue`
permite saltar a la siguiente iteración del ciclo, mientras que `break` permite
salir del ciclo. Ambos soportan la sintaxis de marcado de `loop` `'NAME` para
salir de un ciclo anidado. Ejemplo:

```{code} rust
'outer: for i in 1..=3 {
    'inner: for j in 1..=3 {
        if i == 2 && j == 2 {
            break 'outer;
        }
        println!("i: {}, j: {}", i, j);
    }
}
```

## Referencias

- [The Rust Programming Language](https://doc.rust-lang.org/book/).
- [The Cargo Book](https://doc.rust-lang.org/cargo/index.html).
- [Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/index.html).
- [py2rs](https://rochacbruno.github.io/py2rs/index.html).
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/index.html).
