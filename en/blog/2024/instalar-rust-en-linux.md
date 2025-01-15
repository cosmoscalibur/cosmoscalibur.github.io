---
date: 2024-06-15
tags: rustlang, vscode, notebook, evcxr, rust-analyzer
category: technology
language: en
---

# Install Rust on Linux

During my journey to learn Rust, I will be sharing some steps with you. This
time, let's cover how to install Rust on Linux and prepare ourselves to use it
in VSCode and Notebook.

[Rust](https://www.rust-lang.org/) is a low-level language developed with
Mozilla's support, focused on performance and security, with excellent
compile-time checks that help prevent some runtime errors. By design, it aims
for better ergonomics than a low-level language while still allowing for greater
control.

## Install with Rustup

The [recommended installation](https://www.rust-lang.org/tools/install) is via
the tool {program}`rustup`, for this we proceed with

```{code} bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

This downloads _rustup_, and initiates the installation process for Rust and
other utilities. There, we can accept the default option by pressing _enter_.

Thus, we will have installed [`cargo`](https://doc.rust-lang.org/cargo/) (the
package manager of Rust), [`clippy`](https://doc.rust-lang.org/clippy/) (the
integrated linter for Rust), `rust-docs` (Rust documentation),
[`rust-std`](https://doc.rust-lang.org/std/) (the standard library of Rust),
[`rustc`](https://doc.rust-lang.org/rustc/what-is-rustc.html) (the Rust
compiler), and [`rustfmt`](https://github.com/rust-lang/rustfmt) (the code
formatter for Rust). And of course, the same
[`rustup`](https://rust-lang.github.io/rustup/) that allows us to manage the
_toolchain_ of Rust.

Regarding {program}`cargo`, there is something interesting to mention: it
integrates the execution of tests (`cargo test`), which is also an option of the
compiler, and the generation of documentation (`cargo doc`) with
[`rustdoc`](https://doc.rust-lang.org/rustdoc/index.html).

Now we conclude with

```{code} bash
source "$HOME/.cargo/env"
```

This allows us to associate the necessary environment variables in the current
console.

If now we execute `rustc --version`, we should see the compiler version. If you
don't see it, you may have skipped the previous step for associating the
environment variable.

When we want to update the compiler version, we will use `rustup update`.

## Configure VSCode

To have the necessary help in our IDE, VSCode, while programming in Rust, we are
going to install the extension [rust-analyzer](https://rust-analyzer.github.io).
This extension provides options for autocompletion, go to definition, find
references, access documentation, semantic highlighting, assistance, and
suggestions. All of this is a benefit thanks to the implementation of the LSP
(_Language Server Protocol_) for Rust.

_Rust Analyzer_ is also available for other editors.

We can start with a small default project to see the extension in action, as
well as our base installation. To create a new one, we use

```{code} bash
cargo new miniproject
```

This creates a basic Rust application project template, including Cargo
dependency files and a source directory with a "hello world" example. We can use
some basic erroneous code to see it in action.

```{figure} /images/instalar-rust-en-linux/rust-analyzer.png
---
alt: Diagnostic of rust-analyzer suggesting the use of `let` to assign a variable
align: center
width: 800px
height: 400px
---
  Diagnostic of rust-analyzer suggesting the use of `let` to assign a variable.
```

## Rust Notebook

Now, we have the option to add a Rust _kernel_ to Jupyter Notebook for an
interactive Rust experience combined with the benefit of naturally documenting
code. This can be achieved thanks to the _kernel_
[Evcxr](https://github.com/evcxr/evcxr).

First, we install the necessary dependency with _cargo_.

```{code} bash
cargo install --locked evcxr_jupyter
```

Once installed, we should ensure that our Jupyter Notebook environment is active
(in case it's in a specific environment). If Jupyter Notebook is not already
installed, on Ubuntu we can proceed as follows:

```{code} bash
sudo apt install -y jupyter-notebook
```

Or with the Python package manager (installing `notebook` and `jupyterlab`),
like so:

```{code} bash
pip install notebook jupyterlab # With PIP
uv pip install notebook jupyterlab # With UV
```

Now, let's add the _Kernel_ to Notebook.

```{code} bash
evcxr_jupyter --install
```

Once added, we can open Notebook or JupyterLab, and we will see the option to
use Rust.

```{code} bash
jupyter notebook  # Open notebook
jupyter lab  # Open Jupyterlab (recommended)
```

```{figure} /images/instalar-rust-en-linux/jupyter-evcxr.png
---
alt: Availability of Rust as a Kernel in Jupyter Notebook
align: center
width: 800px
height: 400px
---
   Availability of Rust as a Kernel in Jupyter Notebook
```

```{figure} /images/instalar-rust-en-linux/jupyter-cells-rust.png
---
alt: Basic example of a variable assignment in Rust in Notebook
align: center
width: 800px
height: 400px
---
   Basic example of a variable assignment in Rust in Notebook
```
