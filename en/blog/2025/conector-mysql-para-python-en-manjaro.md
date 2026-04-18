---
date: 2026-04-18
tags: manjaro, database, mysql, mariadb, python
category: technology, linux, programming
language: en
---

# MySQL Connector for Python on Manjaro

Now that I use [Manjaro instead of Ubuntu](/en/blog/2024/que-hacer-despues-de-instalar-manjaro.md), one of the problems I encountered when adapting the development environment I use for work, is that the MySQL connector for Python *MySQLdb* depends on `libmysqlclient-dev`, which is not available in Manjaro. Here is how I solved the problem.

## MySQL Connector

The database connector provides an interface to interact with databases from an application. Database vendors offer their own connectors for different programming languages, native drivers that allow the community to interact with the databases by creating new extensions or even the definition of the standard so that there are implementations in different languages and that have no dependencies with the operating system.

In the case of the MySQL connector for Python, the official connector depends on `libmysqlclient-dev` (with the `mysqlclient` python package), which is not available in Manjaro.

## Alternatives for Python connection with MySQL on Manjaro

We can have two alternatives to connect to MySQL from Python on Manjaro, considering a native connection, but also a connection without dependencies with the operating system.

### MariaDB Connector

MariaDB is an open source relational database based on the MySQL source code. It is compatible with most MySQL features and offers improvements in security, performance, and scalability. This compatibility offers an alternative to the native MySQL connection with which we can install `mysqlclient` with our Python package manager as usual. To install native dependencies, in Manjaro and Arch derivatives, we proceed as follows:

```bash
pamac install mariadb-libs
```

Now we can install the `mysqlclient` Python package with our Python package manager in the usual way ([package in the environment](/en/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md#installing-python-packages) or [in the project](/en/blog/2025/configuracion-de-proyectos-y-herramientas-python-con-uv.md#creating-a-project-with-uv-init)):

```bash
uv pip install mysqlclient  # Installation in the environment
uv add mysqlclient # Installation in the project
```

### Pure Python MySQL Connector

There is also a pure Python MySQL connector that also meets the standard for database connections defined by PEP 249, just like the native connector. This option is *PyMySQL*, and it is an excellent alternative if you cannot install the native dependencies of MySQL or MariaDB, or simply prefer not to install them.

To install PyMySQL, we simply execute the following command:

```bash
uv pip install PyMySQL  # Installation in the environment
uv add PyMySQL  # Installation in the project
```

Now you can use `pymysql` directly in your projects, or use it as a substitute for `MySQLdb` when the native dependency is not available, which is done as follows:

```python
try:
    import MySQLdb
except ImportError:
    import pymysql
    # Replaces `MySQLdb` with `pymysql`
    pymysql.install_as_MySQLdb()
```

### Other alternatives

To configure the development environment you could have other options, and I will briefly comment on two more. Through [AUR](#pamac-commands), you can install the native MySQL dependencies, but I consider that having options that do not pollute the system, we can omit it. The other alternative is that a suitable development environment would be to adapt a local container based on Ubuntu, in order to properly replicate the production environment. Without a doubt, I will tell you a bit more about [Docker](/en/blog/2025/instalar-docker-en-manjaro.md) later, but for now I prefer the convenience of having the environment directly in Manjaro without the container (the integration of the IDE I use, [Zed](/en/blog/2025/zed-un-editor-rapido-y-moderno-de-codigo-abierto.md), does not seem that good yet).

## References

- [Python mariadb connector](https://forum.manjaro.org/t/python-mariadb-connector/164119). Manjaro Linux Forum.
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/). Documentation.
- [install_as_mysqldb](https://github.com/PyMySQL/PyMySQL/blob/e88b729f8f1ddcf0851e0153188b016d0e9ec00c/pymysql/__init__.py#L66). GitHub PyMySQL.
