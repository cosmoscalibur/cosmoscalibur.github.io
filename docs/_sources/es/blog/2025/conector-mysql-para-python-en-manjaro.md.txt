---
date: 2025-05-04
tags: manjaro, base de datos, mysql, mariadb, python
category: tecnología, linux, programación
---

# Conector MySQL para Python en Manjaro

Ahora que uso
[Manjaro en lugar de Ubuntu](/es/blog/2024/que-hacer-despues-de-instalar-manjaro.md),
uno de los problemas que encontré para adecuar el entorno de desarrollo que uso
en mi trabajo, es que el conector de MySQL para Python *MySQLDb* depende de
`libmysqlclient-dev`, que no está disponible en Manjaro. Te cuento cómo
solucioné el problema.

## Conector MySQL

El conector de bases de datos ofrece una interfaz para interactuar con bases de
datos desde una aplicación. Los fabricantes de bases de datos ofrecen sus
propios conectores para distintos lenguajes de programación, controladores
nativos que permiten a la comunidad interactuar con las bases de datos creando
nuevas extensiones o incluso la definición del estándar de tal modo que existan
implementaciones en diferentes lenguajes y que no posean dependencias con el
sistema operativo.

En el caso del conector MySQL para Python, el conector oficial depende de
`libmysqlclient-dev` (con el paquete python de `mysqlclient`), que no está
disponible en Manjaro.

## Alternativas de conexión Python con MySQL en Manjaro

Podemos tener dos alternativas para conectarnos a MySQL desde Python en Manjaro,
considerando una conexión nativa, pero también una conexión sin dependencias con
el sistema operativo.

### Conector de MariaDB

MariaDB es una base de datos relacional de código abierto que se basa en el
código fuente de MySQL. Es compatible con la mayoría de las características de
MySQL y ofrece mejoras en seguridad, rendimiento y escalabilidad. Esta
compatibilidad ofrece una alternativa a la conexión nativa de MySQL con la que
podremos instalar `mysqlclient` con nuestro gestor de paquetes Python de forma
habitual. Para instalar las dependencias nativas, en Manjaro y derivados de
Arch, procedemos de la siguiente manera:

```bash
pamac install mariadb-libs
```

Ahora podremos instalar el paquete Python `mysqlclient` con nuestro gestor de
paquetes Python de forma habitual
([paquete en el ambiente](/es/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md#instalaci%C3%B3n-de-paquetes-python)
o
[en el proyecto](/es/blog/2025/configuracion-de-proyectos-y-herramientas-python-con-uv.md#crear-un-proyecto-con-uv-init)):

```bash
uv pip install mysqlclient  # Instalación en el ambiente
uv add mysqlclient # Instalación en el proyecto
```

### Conector MySQL en Python Puro

Existe también un conector MySQL en Python puro que cumple también el estándar
de conexiones a base de datos definidas por el PEP 249, tal como el conector
nativo. Esta opción es *PyMySQL*, y es una excelente alternativa si no puedes
instalar las dependencias nativas de MySQL o MariaDB, o simplemente prefieres no
instalarlas.

Para hacer la instalación de PyMySQL, simplemente ejecutamos el siguiente
comando:

```bash
uv pip install PyMySQL  # Instalación en el ambiente
uv add PyMySQL  # Instalación en el proyecto
```

Ahora puedes usar en tus proyectos `pymysql` de forma directa, o usarlo como un
sustituto de `MySQLdb` cuando la dependencia nativa no está disponible, lo cual
se hace de la siguiente manera:

```python
try:
    import MySQLdb
except ImportError:
    import pymysql
    # Reemplaza `MySQLdb` por `pymysql`
    pymysql.install_as_MySQLdb()
```

### Otras alternativas

Para configurar el entorno de desarrollo podrías tener otras opciones, y
comentaré ligeramente dos más. A través de [AUR](#pamac-commands), puedes
instalar las dependencias nativas de MySQL, pero considero que al tener opciones
que no contaminan el sistema, podemos omitir. La otra alternativa es que un
entorno de desarrollo adecuado sería adecuar un contenedor local basado en
Ubuntu, de tal forma de replicar adecuadamente el entorno de producción. Esto
sin duda les comentaré un poco más sobre
[Docker](/es/blog/2025/instalar-docker-en-manjaro.md) más adelante, pero de
momento prefiero la comodidad de tener el entorno directamente en Manjaro sin el
contenedor (la integración de la IDE que uso,
[Zed](/es/blog/2025/zed-un-editor-rapido-y-moderno-de-codigo-abierto.md), no me
parece todavía tan buena).

## Referencias

- [Python mariadb connector](https://forum.manjaro.org/t/python-mariadb-connector/164119).
  Manjaro Linux Forum.
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/). Documentation.
- [install_as_mysqldb](https://github.com/PyMySQL/PyMySQL/blob/e88b729f8f1ddcf0851e0153188b016d0e9ec00c/pymysql/__init__.py#L66).
  GitHub PyMySQL.
