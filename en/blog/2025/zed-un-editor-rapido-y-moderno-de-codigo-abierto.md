---
date: 2025-03-27
tags: zed, linux, ide
category: technology, programming
---

# Zed: A fast and modern open source editor

{program}`zed` is an open-source code and text editor, designed to be fast and
easy to use. It is built in Rust and uses a modern and intuitive user interface.
It is currently officially supported on Linux and macOS, but work is underway
for Windows implementation (although experimental versions exist). I will tell
you how to install it and some of its features.

## Installing Zed on Linux

Although you can install it from the repositories of some package managers, as
is my case using Manjaro where I can get it through AUR, my recommended method
is to use the official installation script.

```{bash}
curl -f https://zed.dev/install.sh | sh
```

Regarding updates, if you use the version installed from the official script, it
updates automatically.

Si como yo dispones de un GPU híbrida, te recomiendo seguir la entrada
[Problemas con Wayland y NVIDIA](/en/blog/2024/problema-de-wayland-y-graficos-hibridos-en-linux.md)
para solucionar los problemas que puedas tener. El uso de la GPU es lo que
permite un rápido renderizado de Zed.

If, like me, you have a hybrid GPU, I recommend following the post
[Issues with Wayland and NVIDIA](/en/blog/2024/problema-de-wayland-y-graficos-hibridos-en-linux.md)
to solve any problems you may have. GPU usage is what allows Zed's fast
rendering.

## Native features of Zed

Recently, Zed added native Git support, allowing it to match VSCode in one of
the features that could be a blocker for many developers. It is not just support
for visualizing changes, history, or directing to the web version of the change,
but also support for executing git actions with the Zed interface.

I must also highlight as a vital part of Zed, the _tree sitter_ algorithm, which
is the parser used in Zed natively with incremental support, allowing better
performance after initial load.

The _multibuffer_ is a feature that allows editing multiple files at the same
time, allowing greater efficiency in code editing and is supported natively. For
this you can do general search with {kbd}`Ctrl+Shift+F` and make use of multiple
editing with {kbd}`Ctrl+Shift+L` (I don't know if it's a bug, but it only works
for me if I have match case selected) or if we want specific points with
{kbd}`Alt+Click` (it is not required that the selected point corresponds to the
search match).

We also find in Zed native support for LLM models for chat assistance, allowing
context files to be passed, and direct editing in file. Through this way it is
possible to use different LLM models, including invocations through
[Ollama](../2025/instala-tu-asistente-local-de-ia.md) and
[LM Studio](https://lmstudio.ai) (which allows using local models like
`qwen2.5:7b`, `qwen2.5-coder:7b` or `gemma3:4b`) or native support for Claude,
Copilot and Gemini. You can also use native inline prediction with the Zeta
model which is a fine-tune of `qwen2.5-coder:7b` by Zed.

Finally, I want to highlight its native
[Notebook](https://zed.dev/docs/repl#repl) support (support limited to some
languages, but includes Python) through Jupyter *kernels*.

## Recommended extensions in Zed

The Zed extension system is based on _core_ elements in Rust and the interface
component with Zed in WASM (compiled with Rust). The directory of locally
installed extensions is found in {file}`~/.local/share/zed/extensions`, and in
case you want to test local versions you have the {file}`work` directory (if
they possess _core_ component in Rust) or just {file}`installed` if it is at the
interface and WASM level (I checked this because I was testing changes in the
Codebook dictionary file).

If you want to install a Zed extension you can use the general menu with
{kbd}`Ctrl+Shift+P` and search _zed: extensions_, or directly the shortcut
{kbd}`Ctrl+Shift+X`.

Typically extensions can be configured globally and per project, with Zed
configuration management, but some support their own configuration files.

### Spelling and grammar extensions

- [Codebook](https://github.com/blopker/codebook) Spell checker: Offers spelling
  correction LSP based on _hunspell_ dictionaries through the Rust
  implementation of [spellbook](https://github.com/helix-editor/spellbook).
  Currently supports English and Spanish (after a report I made), but will soon
  support other languages based on LibreOffice dictionaries. Similar to
  [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright),
  correction can be in text or code files. Local dictionary support is planned.
  Possesses global and per-project configuration ({file}`codebook.toml`), but is
  independent of Zed configuration.
- [LTex](https://github.com/vitallium/zed-ltex): Offers grammar correction LSP
  based on LanguageTool. Correction is offered only for text files. The model is
  installed locally.
- [Harper](https://github.com/stef16robbe/harper_zed): Offers grammar correction
  LSP in English in both text and code files. It is an alternative to LTex.

### Extensions for markup languages

In the case of JSON, this is supported natively in Zed. For other cases the
following extensions are recommended:

- [Marksman](https://github.com/vitallium/zed-marksman): LSP for Markdown.
  Offers autocomplete of Markdown links, detection of broken links and
  addressing to definitions. I recommend complementing it with
  [mdformat](https://github.com/executablebooks/mdformat) as a formatter. The
  formatter must be installed independently and configured in Markdown options.
- [Typst](https://github.com/weethet/typst.zed): LSP and compilation management
  for Typst.
- [LaTeX](https://github.com/rzukic/zed-latex): LSP and compilation management
  for LaTeX.
- [reST](https://github.com/elmarco/zed-rst): Syntax highlighting support. It is
  recommended to complement it with
  [docstrfmt](https://github.com/LilSpazJoekp/docstrfmt) as a formatter. There
  is an LSP for reST, [Esbonio](https://github.com/swyddfa/esbonio), but it is
  not supported by Zed.
- [Jinja2 Template Support](https://github.com/ArcherHume/jinja2-support):
  Syntax highlighting and LSP is in planning.
- [XML](https://github.com/sweetppro/zed-xml): Syntax highlighting support. It
  is recommended to complement with
  [XML Pretty](https://github.com/xmlem/xml-pretty) as a formatter.
- [TOML](https://zed.dev/docs/languages/toml): Highlighting and LSP support.
- [Pest](https://github.com/pest-parser/zed-pest): Highlighting and LSP support
  for the Pest grammar specification language (*PEG grammar* in Rust).

### Extensions for programming languages

By default, LSP support for some programming languages is included, while others
can be installed by the user. It is also possible to mix LSP in the same
language.

In my cases of interest, Rust is supported natively and includes
[Rust Analyzer](https://rust-analyzer.github.io/), and in the case of Python by
default LSP support is included with
[Pyright](https://github.com/microsoft/pyright).

- [Ruff](https://docs.astral.sh/ruff/): Ruff LSP, is a linter and formatter for
  Python in Rust.
- SQL: Offers SQL syntax highlighting.
- [Sqruff](https://github.com/gvozdvmozgu/sqruff-zed/): Offers LSP and formatter
  for multiple SQL dialects (of my interest, includes MySQL, PostgreSQL, SQLite
  and BigQuery).

### Infrastructure extensions

- [Justfile](https://github.com/jackTabsCode/zed-just): Offers syntax
  highlighting and step execution option.
- [env](https://github.com/zarifpour/zed-env): Syntax highlighting for
  environment files.
- [Dockerfile](https://github.com/d1y/dockerfile.zed): Offers syntax
  highlighting and LSP for Dockerfile files.
- Docker Compose: syntax highlighting.
- [Make](https://github.com/caius/zed-make): Makefile syntax highlighting.

## Zed Configuration

To illustrate Zed configuration and its integration with formatting tools and
extensions, we are going to install the necessary tools for formatting MarkDown,
reST and XML.

```{code} bash
uv tool install mdformat \
  --with mdformat-gfm \
  --with mdformat-frontmatter \
  --with mdformat-footnote \
  --with mdformat-gfm-alerts \
  --with mdformat-myst \
  --with mdformat-admon
uv tool install docstrfmt --with sphinx
cargo install xml-pretty
```

We are also going to
[install Ollama](../2025/instala-tu-asistente-local-de-ia.md#installing-ollama)
and we can have a local model like `qwen2.5:7b` (for the purpose of the
configuration file example).

It is important that for the activation of Zed prediction, it is necessary to
*login* to Zed with our GitHub account.

```{code} json
{
  "assistant": {
    "default_model": {
      "provider": "ollama",
      "model": "qwen2.5:7b"
    },
    "version": "2"
  },
  "features": {
    "edit_prediction_provider": "zed"
  },
  "ui_font_size": 16,
  "buffer_font_size": 16,
  "theme": {
    "mode": "system",
    "light": "One Light",
    "dark": "One Dark"
  },
  "languages": {
    "Markdown": {
      "format_on_save": "on",
      "formatter": {
        "external": {
          "command": "mdformat",
          "arguments": ["--number", "--wrap", "80", "--extensions", "myst", "-"]
        }
      }
    },
    "XML": {
      "format_on_save": "on",
      "formatter": {
        "external": {
          "command": "xml-pretty",
          "arguments": ["-i", "2"]
        }
      }
    },
    "reST": {
      "format_on_save": "on",
      "formatter": {
        "external": {
          "command": "docstrfmt",
          "arguments": ["-"]
        }
      }
    },
    "Python": {
      "language_servers": ["pyright", "ruff"],
      "format_on_save": "on",
      "formatter": [
        {
          "code_actions": {
            "source.organizeImports.ruff": true,
            "source.fixAll.ruff": true
          }
        },
        {
          "language_server": {
            "name": "ruff"
          }
        }
      ]
    }
  },
  "lsp": {
    "ltex": {
      "settings": {
        "ltex": {
          "language": "es", // en-us
          "enabled": true,
          "completionEnabled": false
        }
      }
    }
  }
}
```

For the configuration of the Codebook hunspell corrector, a `codebook.toml` file
is available in the project root directory.

```{code} toml
dictionaries = ["es"]
use_global = false
```

For language or external tools that are structured with their already known
configuration files, we find the `ruff.toml`, `pyproject.toml` or `Cargo.toml`
file to give an example. I am not going to illustrate these because they are
well known if you require these languages or *linters*.
