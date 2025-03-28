---
date: 2025-03-27
tags: zed, linux, ide
category: tecnologia, programación
---

# Zed: un editor rápido y moderno de código abierto

{program}`zed` es un editor de código y texto de código abierto, diseñado para
ser rápido y fácil de usar. Está construido en Rust y utiliza una interfaz de
usuario moderna e intuitiva. De momento es soportado de forma oficial en Linux y
macOS, pero se está trabajando en su implementación para Windows (aunque existen
versiones experimentales). Te contaré cómo instalarlo y algunas de sus
características.

## Instalación en Linux de Zed

Si bien lo puedes instalar desde los repositorios de algunos gestores de
paquetes, como sucede en mi caso que uso Manjaro, que puedo obtenerlo a través
del AUR, mi método recomendado es usar el script de instalación oficial.

```{bash}
curl -f https://zed.dev/install.sh | sh
```

Respecto a las actualizaciones, si usas la versión instalada desde el script
oficial, este se actualiza automáticamente.

Si como yo dispones de un GPU híbrida, te recomiendo seguir la entrada
[Problemas con Wayland y NVIDIA](/es/blog/2024/problema-de-wayland-y-graficos-hibridos-en-linux.md)
para solucionar los problemas que puedas tener. El uso de la GPU es lo que
permite un rápido renderizado de Zed.

## Características nativas de Zed

Recientemente, Zed agregó el soporte nativo de Git, lo que permite equiparar
contra VSCode en una de las características que podía ser un bloqueo para muchos
desarrolladores. No es solo un soporte en la visualización de los cambios,
historias o dirección a la versión web del cambio, sino también el soporte para
la ejecución de acciones git con la interfaz de Zed.

También debo destacar como una parte vital de Zed, el algoritmo _tree sitter_,
que es el analizador sintáctico usado en Zed de forma nativa con soporte
incremental, lo que permite un mejor rendimiento posterior a la carga inicial.

El _multibuffer_ es una característica que permite la edición de múltiples
archivos al mismo tiempo, lo que permite una mayor eficiencia en la edición de
código y se encuentra soportada de forma nativa. Para esto puedes hacer búsqueda
general con {kbd}`Ctrl+Shift+F` y hacer uso de la edición múltiple con
{kbd}`Ctrl+Shift+L` (desconozco si es un error, pero solo me funciona si tengo
seleccionada la coincidencia de mayúsculas) o si deseamos en puntos específicos
con {kbd}`Alt+Click` (no es requerido que el punto seleccionado corresponda a la
coincidencia de búsqueda).

También nos encontramos en Zed el soporte nativo de modelos LLM para la
asistencia por chat, permitiendo el paso de archivos de contextos, y en edición
directa en archivo. Mediante esta forma es posible usar distintos modelos de
LLM, incluyendo invocaciones a través de
[Ollama](/es/blog/2025/instala-tu-asistente-local-de-ia.md) y
[LM Studio](https://lmstudio.ai) (lo que permite usar modelos locales como
`qwen2.5:7b`, `qwen2.5-coder:7b` o `gemma3:4b`) o el soporte nativo de Claude,
Copilot y Gemini. También se puede usar la predicción en línea nativa con el
modelo Zeta que es un ajuste fino de `qwen2.5-coder:7b` por Zed.

Por último, quiero destacar su soporte nativo de
[Notebook](https://zed.dev/docs/repl#repl) (soporte limitado a algunos
lenguajes, pero incluye Python) a través de los *kernels* de Jupyter.

## Extensiones recomendadas en Zed

El sistema de extensiones de Zed se basa en elementos _core_ en Rust y la
componente de interfaz con Zed en WASM (compilado con Rust). El directorio de
extensiones instaladas localmente se encuentra en
{file}`~/.local/share/zed/extensions`, y en caso de querer hacer pruebas de
versiones locales dispones para esto del directorio {file}`work` (si poseen
componente _core_ en Rust) o solo {file}`installed` si es a nivel de interfaz y
WASM (esto lo revisé porque estaba probando cambios en el archivo de diccionario
de Codebook).

Si deseas instalar una extensión de Zed puedes usar el menú general con
{kbd}`Ctrl+Shift+P` y buscar _zed: extensions_, o directamente el atajo
{kbd}`Ctrl+Shift+X`.

Típicamente las extensiones se pueden configurar de forma global y por proyecto,
con la gestión de configuración de Zed, pero algunas soportan archivos de
configuración propios.

### Extensiones de ortografía y gramática

- [Codebook](https://github.com/blopker/codebook) Spell checker: Ofrece LSP de
  corrección de ortografía basada en diccionarios _hunspell_ a través de la
  implementación Rust de [spellbook](https://github.com/helix-editor/spellbook).
  Actualmente soporta inglés y español (tras un reporte que realicé), pero
  pronto soportará otros idiomas basados en los diccionarios de LibreOffice.
  Similar a
  [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright),
  la corrección puede ser en archivos de texto o de código. Está planeado el
  soporte de diccionarios locales. Posee configuración global y por proyecto
  ({file}`codebook.toml`), pero es independiente de la configuración de Zed.
- [LTex](https://github.com/vitallium/zed-ltex): Ofrece LSP de corrección
  gramatical basada en LanguageTool. La corrección se ofrece solo para archivos
  de texto. El modelo es instalado localmente.
- [Harper](https://github.com/stef16robbe/harper_zed): Ofrece LSP de corrección
  gramatical en inglés tanto en archivos de texto como de código. Es una
  alternativa a LTex.

### Extensiones para lenguajes de marcado

- [Marksman](https://github.com/vitallium/zed-marksman): LSP para Markdown.
  Ofrece autocompletado de enlaces de Markdown, detección de enlaces rotos y
  direccionado a definiciones. Recomiendo complementarlo con
  [mdformat](https://github.com/executablebooks/mdformat) como formateador. El
  formateado debe instalarse de forma independiente y configurarse en las
  opciones de Markdown.
- [Typst](https://github.com/weethet/typst.zed): LSP y gestión de compilado para
  Typst.
- [LaTeX](https://github.com/rzukic/zed-latex): LSP y gestión de compilado para
  LaTeX.
- [reST](https://github.com/elmarco/zed-rst): Soporte de resaltado de sintaxis.
  Se recomienda complementarlo con
  [docstrfmt](https://github.com/LilSpazJoekp/docstrfmt) como formateador.
  Existe un LSP para reST, [Esbonio](https://github.com/swyddfa/esbonio), pero
  no es soportado por Zed.
- [Jinja2 Template Support](https://github.com/ArcherHume/jinja2-support):
  Resaltado de sintaxis y el LSP está en planeación.
- [XML](https://github.com/sweetppro/zed-xml): Soporte de resaltado de sintaxis.
  Se recomienda complementar con
  [XML Pretty](https://github.com/xmlem/xml-pretty) como formateador.
- [TOML](https://zed.dev/docs/languages/toml): Soporte de resaltado y LSP.

### Extensiones para lenguajes de programación

Por defecto se incluye el soporte de LSP de algunos lenguajes de programación,
mientras que otros pueden ser instalados por el usuario. También es posible
mezclar LSP en un mismo lenguaje.

En mis casos de interés, Rust es soportado de forma nativa e incluye
[Rust Analyzer](https://rust-analyzer.github.io/), y en el caso de Python por
defecto se incluye el soporte de LSP con
[Pyright](https://github.com/microsoft/pyright).

- [Ruff](https://docs.astral.sh/ruff/): LSP de Ruff, es un linter y formateador
  para Python en Rust.
- SQL: Ofrece resaltado de sintaxis de SQL.
- [Sqruff](https://github.com/gvozdvmozgu/sqruff-zed/): Ofrece LSP y formateador
  para múltiples dialectos de SQL (de mi interés, incluye MySQL, PostgreSQL,
  SQLite y BigQuery).

### Extensiones de infraestructura

- [Justfile](https://github.com/jackTabsCode/zed-just): Ofrece resaltado de
  sintaxis y opción de ejecución de pasos.
- [env](https://github.com/zarifpour/zed-env): Resaltado de sintaxis para
  archivos de entorno.
- [Dockerfile](https://github.com/d1y/dockerfile.zed): Ofrece resaltado de
  sintaxis y LSP para archivos Dockerfile.
- Docker Compose: resaltado de sintaxis.
- [Make](https://github.com/caius/zed-make): resaltado de sintaxis de Makefile.

## Configuración de Zed

Para ilustrar la configuración de Zed y su integración con herramientas de
formateo y extensiones, vamos a instalar las herramientas necesarias para el
formateo de MarkDown, reST y XML.

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

También vamos a
[instalar Ollama](/es/blog/2025/instala-tu-asistente-local-de-ia.md#instalaci%C3%B3n-de-ollama)
y podemos disponer de un modelo local como `qwen2.5:7b` (para efecto del ejemplo
del archivo de configuración).

Es importante que para la activación de la predicción de Zed, es necesario hacer
*login* en Zed con nuestra cuenta de GitHub.

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

Para la configuración del corrector hunspell de Codebook se dispone de un
archivo `codebook.toml` en el directorio raíz del proyecto.

```{code} toml
dictionaries = ["es"]
use_global = false
```

Para las herramientas de los lenguajes o externas que son estructuradas con sus
archivos de configuración ya conocidos, nos encontramos con el archivo de
`ruff.toml`, `pyproject.toml` o `Cargo.toml` por poner un ejemplo. De estos no
voy a ilustrar por ser bien conocidos si requieres de estos lenguajes o
*linters*.
