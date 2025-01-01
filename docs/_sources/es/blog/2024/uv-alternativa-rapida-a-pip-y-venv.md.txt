---
date: 2024-06-30
tags: gestor de paquetes, gestor de ambientes virtuales, utilidades en rust, python, uv, pip, venv
category: tecnología
---

# UV, alternativa rápida a PIP y VENV

UV es un gestor de paquetes y entornos virtuales alternativo para _Python_,
desarrollado en _Rust_ y que nos promete ser muy rápido en los procesos que
pretende reemplazar de PIP y VENV. En este sentido, solo es añadir `uv` antes de
las instrucciones habituales y debe funcionar (salvo algunos casos particulares
de compatibilidad o de no existir implementación).

Esta es una de tantas herramientas que vienen en la era _Rust_ a permear el
ecosistema de _Python_ generando un nuevo valor, como lo es la mejora de
rendimiento. Y es que del mismo creador, tenemos también _Ruff_ como un
reemplazo eficiente de _linters_, y también hay otras herramientas como _PyO3_
para crear bibliotecas Python en Rust, Polars como un reemplazo a Pandas o Robyn
como alternativa a Flask.

Este proyecto, [UV](https://astral.sh/blog/uv), pretende ser el equivalente de
un _cargo_ (el gestor de _Rust_) para Python, integrando en un único binario,
múltiples utilidades.

## Instalación de UV

Si tenemos en nuestro sistema más de una versión Python, la forma recomendada
para instalar será a partir del _script_ de instalación que provee, ya que de
esta forma queda disponible para todas nuestras instalaciones sin depender de un
ambiente Python en particular. Esto es porque el binario evalúa la instalación
de Python correspondiente a través de las variables de entorno y soporta las
funciones de gestión para el ambiente detectado.

Si estamos en Linux, podemos proceder como

```{code} bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

La primera línea, descarga el _script_ de instalación y lo ejecuta. En la
segunda línea, se configura el entorno (en mi caso uso _bash_) y con esto queda
disponible de forma inmediata (también si abres una nueva consola estará
disponible).

También se encuentra como un paquete Python, por lo que podrás usar _pip_ para
instalarlo. Si necesitas validar otro método o sistema operativo, puedes revisar
el
[repositorio oficial](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started).

```{code} bash
pip install uv
```

Como veremos adelante, tendremos unas buenas mejoras en los tiempos de
instalación de paquetes y de creación de ambientes, pero es importante que si
piensas esta herramienta para reducir el tiempo de ejecución de GitHub Actions,
el tiempo de instalación de UV o de su
[gestión de caché](https://github.com/actions/setup-python/issues/822) puede no
ser una alternativa de momento, salvo que el tiempo de resolución efectivamente
lo valga. En mi caso, el método directo tomó 7.8 s, mientras que la instalación
con PIP tomó 5.8 s.

```{note}
La manera como mediremos los tiempos de los procesos, será mediante la
utilidad `time`. Esta se puede anteceder a las instrucciones que usaremos y nos
permitirá evaluar el tiempo total (_real_), así como el tiempo en espacio de
usuario y de sistema.
```

Para actualizar _UV_ desde el binario, podemos usar `uv self update` (disponible
desde la versión 0.1.23).

### Desinstalar UV

Esto no es algo bien documentado, pero se encuentra disponible en un
[reporte al repositorio](https://github.com/astral-sh/uv/issues/1696#issuecomment-2031776112),
considerando que es simplemente un binario. Así que nos interesa borrar la caché
de UV y el binario.

```{code} bash
rm -rf $HOME/.cache/uv
rm $HOME/.cargo/bin/uv
```

## Creación de ambientes virtuales

Igual que con la utilidad de _venv_, el ambiente creado depende de la
instalación Python usada (detectado por las variables de entorno), y tendremos
opción de manejarlo con el nombre por defecto o asignando uno.

```{code} bash
python3 -m venv testvenv  # VENV: Toma 2.5 s
uv venv testuv  # UV: Toma 0.01 s
```

La opción de _UV_ es bastante rápida en la creación del ambiente virtual.

## Instalación de paquetes Python

En general, es buena práctica usar ambientes, y UV lo espera por defecto. Pero
en caso de una instalación global, podemos pasar `--system` como argumento
(adecuado para CI o contenedores).

En mi caso, igual para poder hacer las pruebas, activaré los ambientes para
comparar la instalación de _pip_ y _UV_. El caso de uso para la prueba, será la
instalación de las dependencias usadas en el
[repositorio del blog](./crear-un-blog-con-sphinx.md#dependencias).

```{code} bash
source testenv/bin/activate
python3 -m pip install -r requirements.txt -r requirements-dev.txt
```

```{code} bash
source testuv/bin/activate
uv pip install -r requirements.txt -r requirements-dev.txt
```

Mientras que la versión _pip_ tomó 25.5 s, la versión _UV_ tomó 5.9 s. Aquí
notamos ya diferencias importantes que en un flujo de CI (ejemplo, GitHub
Actions), puede representar ahorros interesantes.

Este mismo ejercicio lo realicé para el repositorio principal en mi trabajo,
toma 6 s con UV sin caché e instalando UV, mientras que usando PIP toma
típicamente 32 s sin caché y 24 s con caché. En este caso, es importante pasar
la opción de sistema para usarlo en GitHub Actions.

```{code} bash
pip install uv
uv pip install --system -r requirements.txt -r requirements-dev.txt
```

Es importante tener presente el cambio de sintaxis cuando se instala un paquete
desde un repositorio, y es el uso de `"paquete @ url_repo"`, y en particular si
posee credenciales considerar el soporte acorde a las
[indicaciones](https://github.com/astral-sh/uv?tab=readme-ov-file#git-authentication).
