---
date: 2025-01-26
tags: python, uv, setuptools
category: tecnología, programación
---

# Módulo `pkg_resources` no encontrado en ambientes UV

Si como muchos, ya has iniciado la migración al gestor de paquetes
{program}`uv`, puede que te hayas encontrado con el problema de
`ModuleNotFoundError: No module named 'pkg_resources'`. No te preocupes, esto no
será un obstáculo para continuar la migración.

## ¿Qué es `pkg_resources`?

El módulo de `pkg_resources` pertenece al paquete de *setuptools* y permite el
acceso a los archivos de recursos y el descubrimiento de extensiones. Sin
embargo, este módulo no es recomendable y ha sido marcado como obsoleto, y en su
lugar se debería usar `importlib.resources` e `importlib.metadata`. Sin embargo,
así esté obsoleto, muchos paquetes lo usan. ¿Qué produce el error?

## ¿Qué es Setuptools?

*Setuptools* es una biblioteca diseñada para ayudar a generar paquetes de
bibliotecas Python, con rutinas complementarias a `distutils`. Sin embargo, esta
biblioteca no es parte del *core* de Python y es realmente un paquete
independiente. La instalación base en los sistemas operativos o la instalación
estándar de Python o de algunos gestores de ambientes como {program}`conda`, la
suelen incluir. Pero la instalación creada con el ambiente de {program}`uv` no
la posee. Aquí se origina el problema, es que muchos paquetes dependen de la
suposición de tener `setuptools` ya instalado por defecto, y {program}`uv` no lo
dispone de esta forma. Python por defecto no dispone de una herramienta de
empaquetado y publicación como parte de su *core* (`setuptools` está bajo el
gobierno de *PyPA*, pero esto no implica que sea *core*).

## Agregar `setuptools` a las dependencias

Con el contexto anterior, nos queda una solución clara. El problema no es de
{program}`uv`, es que los paquetes afectados han olvidado añadir en sus
dependencias el paquete de `setuptools`. Siendo así, nuestra solución al
problema es simple: añadir `setuptools` a las dependencias.

Si tu proyecto usa el archivo `requirements.txt` este es el lugar adecuado para
añadirlo (ver
[](/es/blog/2024/uv-alternativa-rapida-a-pip-y-venv.md#instalaci%C3%B3n-de-paquetes-python)),
pero si usas la
[gestión de proyectos](/es/blog/2025/configuracion-de-proyectos-y-herramientas-python-con-uv.md)
de {program}`uv` puedes usar `uv add setuptools`, y si es una herramienta será
necesario inyectar la dependencia `--with setuptools`.

## Referencias

- [Package Discovery and Resource Access using pkg_resources](https://setuptools.pypa.io/en/latest/pkg_resources.html).
  Setuptools.
- [Guides on backward compatibility & deprecated practice](https://setuptools.pypa.io/en/latest/deprecated/index.html).
  Setuptools.
- [Some tools are installed without pkg_resources](https://github.com/astral-sh/uv/issues/6384).
  GitHub UV.
