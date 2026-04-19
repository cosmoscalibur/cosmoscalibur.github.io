---
date: 2026-04-18
tags: python, rust, rendimiento, ruff, uv, polars, pyo3, maturin, pydantic, cpython
category: programación, tecnología
---

# Ecosistema Rust en Python

Durante años, el ecosistema de Python ha lidiado con el "problema de los dos
lenguajes": escribimos código en Python por su ergonomía, pero cuando el
rendimiento es crítico, bajamos a C o C++. Esta transición siempre ha sido
dolorosa, introduciendo riesgos de seguridad de memoria y una complejidad de
mantenimiento considerable. Sin embargo, estamos presenciando un cambio de
paradigma. **Rust se ha convertido en el nuevo estándar para construir la
infraestructura de Python.**

Este fenómeno no es casualidad. Rust ofrece lo que C++ nunca pudo: seguridad de
memoria garantizada en tiempo de compilación y un modelo de concurrencia que nos
permite ignorar el temido *Global Interpreter Lock* (GIL) de forma segura.

## Infraestructura crítica: El motor invisible

A menudo no nos damos cuenta, pero muchas de las bibliotecas que usamos a diario
han sido reconstruidas silenciosamente en Rust para optimizar procesos críticos.

- **{program}`pydantic-core`**: Con la llegada de Pydantic V2, el motor de
  validación se reescribió totalmente en Rust. El resultado es una mejora de
  rendimiento de entre 5x y 50x. Dado que Pydantic es la base de frameworks como
  {program}`FastAPI`, este cambio ha acelerado miles de aplicaciones sin que los
  desarrolladores tuvieran que cambiar una sola línea de sus modelos.
- **{program}`cryptography`**: Uno de los paquetes más descargados de PyPI
  ahora utiliza Rust para partes críticas de su lógica. Esto no solo mejora la
  velocidad, sino que reduce drásticamente la superficie de ataque para errores
  de memoria en un área donde la seguridad es primordial.

## Herramientas de desarrollo y gestión: La era de Astral

Si hay una empresa que ejemplifica esta revolución es *Astral*. Su enfoque no ha
sido solo "hacerlo más rápido", sino consolidar herramientas fragmentadas.

- **{program}`ruff`**: Ha reemplazado a *flake8*, *isort*, *black* y otros en un
  solo binario. La diferencia no es solo marginal; es instantáneo incluso en
  monorepos de millones de líneas.
- **{program}`uv`**: No es solo un instalador de paquetes. Es una gestión
  completa de Python, entornos virtuales y dependencias. Como ya les conté en mi
  [artículo sobre uv](/es/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md),
  su velocidad se debe al uso intensivo de paralelismo y una gestión de *cache*
  extremadamente agresiva.
- **{program}`ty`**: El nuevo comprobador de tipos que busca jubilar a *Mypy* y
  *Pyright*. Al realizar el análisis estático en Rust, ofrece *feedback* en
  tiempo real en el editor, algo que antes era prohibitivo en proyectos grandes.

## Bibliotecas para procesamiento y servicios

Más allá de las herramientas, el procesamiento de datos ha visto un salto
cuantitativo gracias a la adopción de estándares modernos y la optimización nativa.

- **{program}`polars`**: A diferencia de *Pandas*, {program}`polars` utiliza un
  motor de ejecución totalmente vectorial y perezoso escrito en Rust, basado
  internamente en el estándar de memoria **Apache Arrow**. Esto permite un
  diseño de memoria eficiente y operaciones *zero-copy* que maximizan el
  rendimiento del hardware moderno.
- **{program}`connectorx`**: Es la forma más rápida de cargar datos desde bases
  de datos SQL. Su integración nativa con {program}`polars` (vía el comando
  `pl.read_database` usando `engine="connectorx"`) permite mover millones de
  filas desde la base de datos al DataFrame aprovechando conexiones paralelas
  sin los cuellos de botella habituales de Python.
- **{program}`tiktoken`**: La biblioteca de *tokenización* de OpenAI. En el
  mundo de los LLMs, convertir texto en tokens es una tarea constante y pesada;
  hacerlo en Rust permite procesar miles de documentos por segundo sin bloquear
  el bucle principal de Python.

En cuanto a servidores, mientras {program}`robyn` intenta ser una alternativa
completa a {program}`FastAPI`, proyectos como **{program}`granian`** están
demostrando que se puede construir un servidor HTTP de alto rendimiento en Rust
que sea más estable y rápido que los tradicionales basados en *Uvicorn*.

## Casos de uso y utilidades específicas

Incluso en tareas más cotidianas, Rust está ganando terreno como herramienta de
optimización directa:

- **{program}`fastexcel`**: Basado en la biblioteca **Calamine** de Rust, es
  increíblemente veloz para leer archivos Excel pesados. De hecho, sirve como el
  motor de lectura de archivos Excel por defecto y más eficiente para
  {program}`polars`.
- **{program}`rensa`**: Se posiciona como una alternativa moderna a
  `datasketch` o `pyminhash` para tareas de similitud de textos mediante
  *MinHash*. En mi experiencia, ha sido fundamental para la **detección
  automática de plantillas en conversaciones**, permitiendo deduplicar grandes
  conjuntos de datos de forma casi instantánea.
- **{program}`orjson`**: Sigue siendo el estándar de oro para la serialización
  JSON. Es posible integrarlo como serializador en **Django** (por ejemplo, a
  través de *Django REST Framework*) para mejorar drásticamente la velocidad de
  respuesta de las APIs.

## Desarrollo de extensiones nativas: PyO3 y Maturin

Este auge no sería posible sin el ecosistema de creación de extensiones nativas.
**{program}`PyO3`** es el *framework* que permite exponer código Rust a Python
con una fricción mínima. Ha desplazado a *Cython* y al uso directo de la API de C
de *CPython* por su capacidad de prevenir *segfaults* y permitir el uso de
abstracciones modernas como *generics* y *traits*.

Su gran ventaja es la **conversión automática de tipos de datos estándar**, lo
que reduce enormemente el trabajo manual en la interfaz entre ambos lenguajes.
Sin embargo, para que una extensión sea realmente efectiva y aproveche todo el
potencial de Rust, es vital seguir prácticas de diseño recomendadas:

1.  **Gestión del GIL**: La verdadera potencia de Rust se libera al usar
    `py.allow_threads` para liberar el *Global Interpreter Lock* en cálculos
    intensivos, permitiendo paralelismo real.
2.  **Mapeo de errores**: Es fundamental transformar los `Result` de Rust en
    excepciones de Python adecuadas (`PyValueError`, `PyTypeError`) para que la
    experiencia del usuario final sea consistente.
3.  **Desacoplamiento**: Una práctica clave es mantener la lógica pura de Rust
    en un *crate* independiente de los *bindings* de Python, lo que facilita las
    pruebas unitarias y la reutilización del código.

Finalmente, con **{program}`maturin`**, distribuir binarios (*wheels*) para
múltiples plataformas es ahora un proceso trivial en comparación con las
complejidades tradicionales de *setuptools*.

## Rust en el núcleo: El futuro de CPython

Quizás la noticia más impactante es que la relación entre ambos lenguajes ya no
es solo de "vecindad", sino de integración profunda. Existe una iniciativa
oficial, conocida como **"Rust for CPython"**, que busca introducir Rust en el
propio árbol de fuentes del intérprete.

El objetivo es permitir que partes críticas de CPython —especialmente aquellas
difíciles de mantener o propensas a errores en C— puedan reescribirse en Rust. Se
espera que **Python 3.16** sea la primera versión que incluya componentes en
Rust de forma oficial, marcando el inicio de una era donde el núcleo del
lenguaje será más seguro y fácil de evolucionar.

## Revisión crítica: ¿Es siempre la solución?

A pesar de los beneficios, esta "Rustificación" tiene un coste. La barrera de
contribución se eleva: un desarrollador de Python que quiera arreglar un bug en
el núcleo de {program}`ruff` ahora debe saber Rust. Además, la compilación de
binarios introduce una capa de complejidad en sistemas de CI/CD que no siempre
se justifica para herramientas pequeñas.

Sin embargo, para la infraestructura base, el veredicto es claro: Python es el
lenguaje de la interfaz, pero Rust es, cada vez más, el lenguaje del motor.

## Referencias

- [Rust for CPython: Discussion and Roadmap](https://discuss.python.org/t/rust-for-cpython/). Python Discourse.
- [Py2RS: Guía de Python a Rust](https://rochacbruno.github.io/py2rs/index.html). Bruno Rocha.
- [Rusty Python: Cómo usamos Rust para acelerar Python](https://ohadravid.github.io/posts/2023-03-rusty-python/). Ohad Ravid.
- [Nueve reglas para escribir extensiones de Python en Rust](https://medium.com/data-science/nine-rules-for-writing-python-extensions-in-rust-d35ea3a4ec29). Medium.
- [PyO3: Rust bindings for Python](https://pyo3.rs/).
- [Maturin: Build and publish crates with pyo3](https://www.maturin.rs/).
- [Pydantic-core: The engine of Pydantic V2](https://github.com/pydantic/pydantic-core).
- [Polars: Blazingly fast DataFrames with Apache Arrow](https://pola.rs/).
- [ConnectorX: Fast SQL to DataFrame library](https://github.com/sfu-db/connector-x).
- [Fastexcel: Fast Excel reader based on Calamine](https://github.com/ToucanToco/fastexcel).
- [Rensa: High-performance MinHash library](https://github.com/beowolx/rensa).
- [Orjson: Fast JSON library for Python](https://github.com/ijl/orjson).
- [Tiktoken: OpenAI's fast tokenizer](https://github.com/openai/tiktoken).
- [Robyn: A high-performance web framework](https://robyn.tech/).
- [Granian: A Rust HTTP server for Python](https://github.com/emmett-framework/granian).
- [Astral: The future of Python tooling](https://astral.sh/).
