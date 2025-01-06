---
date: 2025-01-06
tags: gestor de paquetes, pyproject, python, uv
category: tecnología, programación, blog con sphinx
---

# Configuración de proyectos y herramientas Python con UV

Crearemos un proyecto Python con {program}`uv`, el cual usa el formato
{file}`pyproject.toml` para su configuración, facilitando la portabilidad del
mismo. Adicional, este formato ya es un formato común con otros gestores de
paquetes de Python, y usado para la configuración de utilidades.

Para fines de ilustración, migraré la gestión del blog a UV, del cual ya les
había contado un poco de su beneficio como
[alternativa a PIP y VENV](/es/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md).

## Crear un proyecto con `uv init`

Si lo creamos desde cero, el nombre del proyecto será el nombre del directorio,
pero si estamos dentro y usamos el directorio este se asigna como nombre del
proyecto. En mi caso, el directorio ya existente es mi repo de GitHub de
{file}`cosmoscalibur.github.io`, y este será el nombre del proyecto.

No siempre requerimos la misma versión de Python, y en Linux tenemos instalado
por defecto típicamente, pero no todos poseen la misma versión. Por lo que es
conveniente usar la especificación de la versión en lugar de la versión del
sistema. Esto genera los archivos de {file}`.python-version` que indica la
versión de Python a usar, el archivo de configuración de proyecto
{file}`pyproject.toml` y un archivo de ejemplo {file}`hello.py`.

```{code} bash
uv init . -p 3.12
```

Al estar dentro del directorio, podemos ejecutar `uv run hello.py`, y usará la
versión Python especificada y construye el ambiente necesario para funcionar. El
ambiente quedará en el directorio {file}`.venv`. Ya que hicimos la prueba,
puedes borrar el archivo de ejemplo.

Para agregar las dependencias en el proyecto, usamos `uv add`. Lo podemos
agregar de forma individual o una lista.

```{code} bash
uv add sphinx
uv add ablog
uv add pydata-sphinx-theme
uv add sphinx-design sphinx-copybutton sphinxcontrib-youtube sphinxext-rediraffe
uv add sphinxext-opengraph matplotlib
uv add myst-parser jupytext myst-nb
```

Estas adiciones se van añadiendo al campo de dependencias el archivo de
proyecto.

Al no indicar explícitamente una restricción se usará como restricción que sea
mayor o igual que la versión más alta disponible compatible con el ambiente. Si
requieres una restricción explícita, puedes hacerlo con la misma notación que en
{program}`pip`, pero debe añadirse entre comillas.

Las dependencias opcionales también tienen su mecanismo de adición, y aquí
aprovecho a agregar una que estoy reemplazando por un manejo propio, pero que me
interesa estar comparando. Esto se logra añadiendo `--optional` seguido del
nombre de un grupo para este opcional.

```{code} bash
uv add sphinx-sitemap --optional sitemap
```

También podemos añadir de forma explícita cuáles son las dependencias de
desarrollo, mediante `uv add --dev`, o si queremos indicar un grupo explícito de
desarrollo, `uv add --group` seguido del nombre del grupo y al final los
paquetes.

```{code} bash
uv add --dev jupyterlab jupyterlab_myst
uv add --group rest rstcheck doc8 docstrfmt "esbonio>=1.0.0b8"
uv add --group markdown mdformat mdformat-gfm mdformat-frontmatter \
  mdformat-footnote mdformat-gfm-alerts mdformat-myst
```

Es importante notar que la opción `--dev` es una forma corta para `--group dev`,
siendo así este un grupo por defecto.

### Ejecutar puntos de entrada y rutinas del ambiente con `uv run`

Como cualquier ambiente virtual, este puede ser activado y una vez esto, puedes
ejecutar de forma habitual los puntos de entrada (la utilidad ejecutable) o la
rutina invocando {program}`python`. Podemos usar:

```{code} bash
source .venv/bin/activate # Forma 1
pipenv shell # Forma 2 con pipenv instalado
```

Si no tienes {program}`pipenv`, puedes instalarlo como herramienta,
`uv tool install pipenv`.

Pero {program}`uv` ofrece una facilidad de ejecutar sin activar explícitamente
el ambiente, lo que resulta muy conveniente en muchos casos, ejemplo, cuando se
hace un {file}`justfile` (más adelante tendremos una publicación al respecto).
Del ejemplo inicial, ya sabemos como ejecutar una rutina, pero si necesitamos
una utilidad ejecutable del ambiente, tenemos una forma similar iniciando por
`uv run --`.

```{code} bash
uv run hello.py  # Ejecutar rutinas Python
uv run -- ablog clean  # Ejecutar utilidades en el ambiente
```

Si el ambiente no ha sido creado, este paso lo crea en {file}`.venv` o asegura
que el ambiente esté actualizado. También en este punto se crea {file}`uv.lock`
(también se puede crear con `uv sync` y `uv lock`), que es un formato que
permite asegurar la reproducibilidad exacta de los ambientes.

## Instalar herramientas con `uv tool`

En el ejemplo anterior, los paquetes añadidos con grupos no requieren
explícitamente ser dependencias del proyecto y pueden ser instaladas de forma
global. Este tipo de uso corresponde al concepto de herramientas, y con
{program}`uv` lo podemos gestionar de dos maneras:

- Temporal: Se almacenan en caché y siempre usan el prefijo {program}`uvx`. Si
  no está instalada, se instala y ejecuta, en caso de estar instalada, pasa a
  ejecución.
- Permanente: Se vincula para visibilidad a lo largo del sistema operativo con
  la invocación directa del punto de acceso de la aplicación. En este caso se
  requiere la instalación como primer paso, y luego se invoca de forma
  tradicional. Yo prefiero este caso, porque suelo usarlas en otros proyectos,
  pero como una solución a nivel de nube o proyectos aislados, la opción
  anterior es adecuada. Esto lo hacemos con `uv tool install`.

Para los paquetes relacionados con ReST, cada uno es una herramienta separada,
por lo cual procedemos con la instalación de cada uno por separado.

```{code} bash
uv tool install rstcheck
uv tool install doc8
uv tool install docstrfmt
uv tool install esbonio --prerelease=allow
```

Igual que en la adición de dependencias, cuando no se indica explícitamente la
versión se usa la más alta. En el caso de {program}`esbonio` se evidencia un
parámetro `--prerelease=allow`, el cual nos permite usar versiones previas a
liberación (alfa, beta, candidatas), pero podemos hacer explícita la versión.

Para el caso de los paquetes del grupo Markdown, estos realmente son extensiones
de un paquete principal, {program}`mdformat`. Para inyectar dependencias
adicionales, lo hacemos con el parámetro `--with`.

```{code} bash
uv tool install mdformat \
  --with mdformat-gfm \
  --with mdformat-frontmatter \
  --with mdformat-footnote \
  --with mdformat-gfm-alerts \
  --with mdformat-myst
```

## Referencias

- [{menuselection}`uv-->Concepts-->Projects`](https://docs.astral.sh/uv/concepts/projects/).
- [{menuselection}`uv-->Guides-->Working on projects`](https://docs.astral.sh/uv/guides/projects/).
- [{menuselection}`uv-->Concepts-->Tools`](https://docs.astral.sh/uv/concepts/tools/#the-path).
