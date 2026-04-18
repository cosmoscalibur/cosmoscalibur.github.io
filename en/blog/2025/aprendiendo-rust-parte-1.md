---
date: 2025-03-31
tags: rustlang
category: technology, programming
language: en
---

# Learning Rust: Part 1 - Basic use of cargo, variables and control flow

Almost two years ago I set out to learn Rust, but I didn't have time or really lacked the discipline to keep going. Now, I am firmly committed to this goal for 2025 and here I am taking notes, doing some exercises and starting a project. Regarding these notes, they should be considered personal notes, and well, I cover the basic details to start a project with *cargo*, print to the console, assign variables, understand variable types and use control flow (still without error handling).

The starting point for this post is that you have already [installed Rust in Linux](/en/blog/2024/instalar-rust-en-linux.md).

## Using `cargo`

`cargo new project` to create a new project with its directory. If the directory exists, we use `cargo init` in the directory for its initialization. The initialization includes a `src` directory with an example `main.rs` file, a git exclusion file `.gitignore` (the versioning system can be configured with the `--vcs` option) and the project file `Cargo.toml`. The project name can be different from the directory, and can be passed in the `--name` option. By default, the `--bin` option is used to create a binary, but it can be `--lib` to generate a library. By default, it is the 2021 edition, but it can be configured with `--edition` (for example, use the new edition, `2024`). These options apply both when creating with `new` and initializing with `init`.

The project file is necessary for compilation (`cargo build`) or execution (`cargo run`). You can use projects with multiple binaries if in the {file}`src` directory we add other source files. {program}`cargo` can infer these and create the binaries, and if we want to run them it will be enough to use `cargo run` followed by `--bin` and the name (by default it is the file name without extension).

For general file organization, you can consult [Package Layout](https://doc.rust-lang.org/cargo/guide/project-layout.html) from *The Cargo Book*, and the configuration if we do not want the default names of the binaries in [Cargo Targets](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#configuring-a-target).

You can compile the source code directly without `cargo` using `rustc` followed by the path of the source code.

```{note}
An interesting instruction is `cargo check`, which will allow you to verify if the code is compilable without needing to generate the executable. This is much faster and sometimes we do not need to do the execution test, but only know if it can generate compilation errors.
```

## Hello world in Rust

Executable code in Rust always requires a `main` function. Functions are specified with `fn` followed by the name, parentheses for arguments, and braces for the function body. Statement lines require the `;` terminator.

```{code} rust
fn main(){
    // This is a one-line comment
    println!("Hello, Edward! 🧠");
}
```

`println` is a macro (that's why it ends in `!`) to print, and this helps us with handling the existence of multiple arguments. There are several ways to print and format:

- `format!`: Formats a text string (its output is `String`).
- `print!`: Prints to the console (standard output) without a line break (`io::stdout`).
- `println!`: Prints to the console with a line break.
- The `eprint!` and `eprintln!` versions equivalent to their version without the initial `e` only that they print to the standard error output (`io::stderr`).

If we want to add comments, this is done with `//` for each line.

## Assignment of variables and constants

To assign variables we use `let` followed by the variable name, `:` the data type (although this can be inferred and not always annotated), `=` and the value of the variable (and of course, the line terminator). In Rust, variables are immutable by default, which implies that once the value is assigned, it cannot be modified. If we want the value to be modifiable, we must add `mut` before the variable name.

We can also assign constants with the `const` keyword, and these are always immutable and must always annotate the type. Its structure is `const` followed by the constant name in uppercase (it can contain an underscore), `:`, the data type, the value, and the line terminator. Constants can be assigned with expressions that are calculated at compile time (this helps us with the readability and verification of a value, instead of putting its direct value), and unlike variables they can be of global context, useful for values that are required in multiple parts of our code.

```{code} rust
const ANSWER: i32 = 42;

fn main() {
    let x: i32 = 26;
    let mut y: f32 = 5.6;
    y = 8.;
    let sum = x + ANSWER;
    let flag = true;
    println!("My first variable 'x': {x}");
    println!("My first mutable variable 'y': {y}");
    println!("Adding {sum}")
}
```

The data types that exist are the unsigned and signed integers (`u` and `i`, followed by `8`, `16`, `32`, `64` and `128` according to the size in bits), the floats (`f32` and `f64`), the booleans (`bool`, use 1 *byte*) and the characters (`char`, use 4 *bytes*).

It is also possible to have optional type variables, that is, that admit the value `None`. This is achieved using `Option<type>`, where `type` is the desired variable type. If you want to assign the `None` value it is done directly, but for a different value it is necessary to do it with `Some`.

```{code} rust
fn main(){
  let x : Option<i8> = None;
  let y : Option<i8> = Some(5);
}
```

Rust does not support implicit conversion between data types, and explicit conversion is done using functions like `as`. For custom or composite data, the `into()` or `from()` function can be used, which will have to be defined in *traits* (`Into` and `From`). Other *traits* for this purpose are `TryFrom` and `TryInto`, but there can be very specific cases by types, such as `FromStr` and `ToString`.

There are also composite data types:

- Tuples: It is a grouping of values of different types into a composite type that is conceived as one. To get its values, you can use the notation `x.N` where `N` is the index of the element in the tuple, starting from 0. You can also destructure a tuple using the syntax `let (a, b, c) = tuple;`. Once assigned, tuples cannot change their size or data type. Values are assigned to tuples using the syntax `let tuple = (1, 2.0, 'a');` or by explicitly indicating the type of each element `let tuple: (i32, f64, char) = (1, 2.0, 'a');`.

- Arrays: It is a collection of elements of the same type and fixed size. Values are assigned to arrays using the syntax `let array = [1, 2, 3];` or by explicitly indicating the type of each element `let array: [i32; 3] = [1, 2, 3];`. You can also create an array with repeated values using the syntax `let array = [0; 5];` which creates an array of 5 elements all equal to 0. The elements of an array can be accessed using the notation `array[i]` where `i` is the index of the element in the array, starting from 0. Iteration over the array is supported through the initial value notation followed by `..` (with `..=` indicates that the final value is included) and the final value. And with `step_by` to iterate with a specific step (similar to `range` in Python).

- Vectors: They are collections of elements of the same type and variable size (a comparison with Python lists). Values are assigned to vectors using the syntax `let vector = vec![1, 2, 3];` which is a macro, or `let vector = Vec::new();` (or explicitly indicating the type of each element `let vector: Vec<i32> = Vec::new();`) which is a function and assigning the values using the syntax `vector.push(4);`. The elements of a vector can be accessed using the notation `vector[i]` where `i` is the index of the element in the vector, starting from 0.

- Hash map: It is a collection of key-value pairs where the keys are unique and the values can be of any type (equivalent of Python dictionaries). Values are assigned to hash maps using the syntax `let hash_map = HashMap::new();` which is a function and assigning the values using the syntax `hash_map.insert("key", value);`. You can access the values of a hash map using the notation `hash_map["key"]` where `key` is the key of the value you want to get. It is necessary to import the `std::collections::HashMap` module to use hash maps. A *pythonic* alternative is available using the `maplit` *crate* with the `hashmap!` macro.

  ```{code} rust
  #[macro_use] extern crate maplit;
  fn main(){
    let map = hashmap!{
        "daffy" => 80,
        "bugs" => 79,
        "taz" => 63,
    };
  }
  ```

- Hash set: It is a collection of unique elements without a specific order (equivalent of Python sets). Values are assigned to hash sets using the syntax `let hash_set = HashSet::new();` which is a function and assigning the values using the syntax `hash_set.insert(element);`. It is necessary to import the `std::collections::HashSet` module to use hash sets. A *pythonic* alternative is available using the `maplit` *crate* with the `hashset!` macro.

  ```{code} rust
  #[macro_use] extern crate maplit;
  fn main(){
    let set = hashset!{
        "daffy",
        "bugs",
        "taz",
    };
  }
  ```

- Structs: They are collections of fields that can be of different types. They are defined using the syntax `struct Name { field1: Type, field2: Type, ... }`. Access to the fields is done using the syntax `struct.field`.

- Tuple structs: When the names of the fields are not relevant, tuple structs can be used. They are defined using the syntax `struct Name(Type1, Type2, ...)`. Access to the fields is done using the syntax `struct.0`, `struct.1`, etc. If it is a single field, it is usually known as a `newtype` and can be used to reduce the exposure of the original data and eliminate the confusion of type swapping that can occur with the `type` alias. However, this implies making additional definitions for data handling (for example, defining the *Display* *trait*, since the type access is not reusable). You can also use zero-argument cases (and omit the parentheses) of this type of structs for cases that do not require data per se, and have null returns, and this is known as *ZST* (*Zero Sized Type*).

- Enums: Rust also has support for enumerations, which are composite data types that can have several possible values. They are defined using the syntax `enum Name { Type1, Type2, ... }`. Access to the types has the form `Name::Type1`. The types can not only be simple names, but valid forms of structs and tuple structs.

## Functions in Rust

As mentioned previously, in the "Hello world" example, functions are defined starting with `fn`. In this case, unlike `main`, if a function has parameters and returns, they are defined as follows.

```{code} rust
fn sum(a: i32, b: i32) -> i32 {
    return a + b;
}
```

It is important that in Rust, functions must have an explicitly defined return type. However, `return` is optional, and can be useful for early return, and it is assumed that the last value of the function is the return value.

Here we see how to do the sum, and we can have other operators that you can check in the appendix of the official Rust documentation, [Appendix B: Operators and Symbols](https://doc.rust-lang.org/book/appendix-02-operators.html).

## Control flows

### Conditionals

`if else` is a control structure that allows different blocks of code to be executed depending on whether a condition is true or false. In Rust, the `if` keyword is used followed by a boolean expression and then a block of code that will be executed if the condition is true. If you want to execute an alternative block of code if the condition is false, the `else` keyword is used followed by another block of code.

```{code} rust
fn main() {
    let x = 5;

    if x < 10 {
        println!("x is less than 10");
    } else {
        println!("x is greater than or equal to 10");
    }
}
```

If it is a chained conditional, multiple `if` followed by `else if` can be used to evaluate multiple conditions.

```{code} rust
fn main() {
    let x = 5;

    if x < 10 {
        println!("x is less than 10");
    } else if x == 10 {
        println!("x is equal to 10");
    } else {
        println!("x is greater than 10");
    }
}
```

We also have the `match` control structure, which allows you to compare a value with a series of patterns and execute different blocks of code according to the matching pattern. It is important to consider that `match` must be exhaustive in the generation of cases.

```{code} rust
fn main() {
    let x = 5;

    match x {
        1 => println!("x is equal to 1"),
        2 => println!("x is equal to 2"),
        _ => println!("x is different from 1 and 2"),
    }
}
```

There are cases in which the logic with `match` can be very verbose, and it can be condensed into `if let` or `let else`. The first case allows assigning a matching pattern ignoring the other cases, and the second allows assigning a variable if it matches the pattern and executing a block if it does not match the pattern. You can detail more in [*Concise Control Flow with if let and let else*](https://doc.rust-lang.org/book/ch06-03-if-let.html).

### Loops in Rust

Rust has 3 types of cyclic structures: `loop`, `while` and `for`. `loop` is a control structure that allows executing a block of code indefinitely until a condition is met (a manual exit by keyboard interruption or a `break`). `while` is a control structure that allows executing a block of code as long as a condition is true. `for` is a control structure that allows iterating over a collection of elements.

The general structure of these 3 types of loops is the following:

```{code} rust
loop {
    // Code to execute indefinitely
}

while condition {
    // Code to execute while the condition is true
}

for element in collection {
    // Code to execute for each element of the collection
}
```

Associated with the loops, we have the keywords `continue` and `break`, which allow controlling the execution flow within the loops. `continue` allows jumping to the next iteration of the loop, while `break` allows exiting the loop. Both support the `loop` marking syntax `'NAME` to exit a nested loop. Example:

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

Regarding the collections for the `for` loop, we can form them from the previously explained ranges, but we can also use containers. In the case of containers, we can use the `iter()`, `into_iter()` and `iter_mut()` methods to get iterators over their elements. For example:

```{code} rust
let vec = vec![1, 2, 3];
for i in vec.iter() {
    println!("{}", i);
}
```

The `iter()` option allows iterating over the elements without consuming it, that is, its elements are kept in the original container. This is useful when we need to access the elements multiple times or when we want to preserve the state of the container. The `into_iter()` option allows iterating over the elements and consuming the container, that is, its elements are removed from the original container. This is useful when we need to access the elements only once or when we want to free the space occupied by the container. The `iter_mut()` option allows iterating over the elements and mutating them, that is, its elements are kept in the original container and can be modified. This is useful when we need to access the elements and modify them.

## References

As I study Rust, I have found the following useful resources and they have served for my process, in a strictly non-linear way (many recommend that the first thing is the approach of *The Rust Programming Language* before other readings or even not doing projects and these other readings until overcoming chapter 10 or other similar references). For the purposes of my own tracking, I indicate the approximate content covered of the material and the notes taken in this blog are the key points that I have considered, but could have omissions of elements that others consider important. I do not aspire for this to be an adequate guide for others, but I hope it is useful for those who are starting their journey with Rust.

- [The Rust Programming Language](https://doc.rust-lang.org/book/). Approximate content covered, up to chapter 6, but omitting chapter 4.
- [The Cargo Book](https://doc.rust-lang.org/cargo/index.html). Approximate content covered, up to section 2.3.
- [Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/index.html). Approximate content covered, day 1, but need to explore chapter 9.
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/index.html). Approximate content covered, up to the beginning of chapter 9, and parts of 11 and 12.

### Other resources

Along the way and given that in parallel I am starting a project in Rust that I will soon share, I have been exploring some additional resources that could be useful for my project, or useful information to save for the future and I wish to share with you. This list will potentially be cumulative in future blog posts.

- [py2rs](https://rochacbruno.github.io/py2rs/index.html).
- [Rustlings](https://github.com/rust-lang/rustlings).
- [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/about.html).
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/intro.html).
- [Are we web yet?](https://arewewebyet.com/).
- [A survey of every iterator variant](https://blog.yoshuawuyts.com/a-survey-of-every-iterator-variant/).
- [Scientific Computing in Rust Monthly](https://scientificcomputing.rs/monthly/).
- [Environment Variables & Rust](https://mattrighetti.com/2024/03/07/environment-variables-and-rust).
- [State of the Crates 2025](https://ohadravid.github.io/posts/2024-12-state-of-the-crates/).
- [24daysofrust](https://zsiciarz.github.io/24daysofrust/)
- [Making Python 100x faster with less than 100 lines of Rust](https://ohadravid.github.io/posts/2023-03-rusty-python/).
