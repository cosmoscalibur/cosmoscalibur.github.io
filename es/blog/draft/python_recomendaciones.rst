Recomendaciones usadas
======================

NEP29: versiones soportadas de python y numpy licencias ciclo de vida de
paquetes Estructura de paquete recomendada por la PSF: docs, <paquete>, tests.
En el paquete se sigue la recomendación de máximo 4 niveles de profundidad para
acceder a una función. Toda función, módulo y clase debe contener docstrings.
Linters

* pycodestyle pep8
* pydocstyle pep257
* mccabe: complejidad ciclomática
* pyflakes vs mypy: errores por análisis estático
* radon: métrica de mantenibilidad
* Pylama integra anteriores
* Ruff
* Pylint
* Análisis de acomplamiento pyreverse
* Vulture
* perflint https://github.com/tonybaloney/perflint
* pyinstrument https://pyinstrument.readthedocs.io/en/latest/ Documentación
* Sphinx Unitarias
* Pytest Formateo:
* Black
* Yapf
* Ruff Perfilamiento
* Snakeviz
* Vprof
* flamegraph
* Linux Perf https://docs.python.org/pl/dev/howto/perf_profiling.html
* memray https://github.com/bloomberg/memray


+ `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_: estilo de código.
+ `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_: estilo de
  *docstrings*.
+ `NEP 29 <https://numpy.org/neps/nep-0029-deprecation_policy.html>`_:
   versiones soportadas de Python y Numpy (se deriva de allí las versiones de
   otros paquetes del ecosistema científico).
+ Ambientes de producción, pruebas y desarrollo mediante ambientes conda, los
  cuales son especificados con archivos YML.
+ Las dependencias de los proyectos se prefieren obtener de las siguintes
  maneras en orden: paquetes anaconda (default y conda-forge), pip, paquete de
  sistema, compilado.
+ Preferencia por paquetes python cuyo desarrollo no haya sido abandonado.
+ Validación de las licencias de los paquetes para no tener conflictos futuros.
+ Estructura de paquete recomendada por la PSF: docs, <paquete>, tests. En el
  paquete se sigue la recomendación de máximo 4 niveles de profundidad.
+ Toda función, módulo y clase debe contener *docstrings*.

Hacemos uso de las siguientes herramientas:

+ `Pylama <https://pylama.readthedocs.io/en/latest/>`_ integrado con las
   dependencias:

   + `pycodestyle <https://github.com/PyCQA/pycodestyle>`_: Valida PEP8.
   + `pydocstyle <https://github.com/PyCQA/pydocstyle/>`_: Valida PEP257.
   + `Mccabe <http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html>`_: Métrica Mccabe de complejidad ciclomática.
   + `PyFlakes <https://github.com/PyCQA/pyflakes>`_: Detección de errores mediante análisis estático.
   + `Radon <https://github.com/rubik/radon>`_: Métrica de `índice de mantenibilidad <https://docs.microsoft.com/es-es/archive/blogs/zainnab/code-metrics-maintainability-index>`_.

+ `Sphinx <https://www.sphinx-doc.org/en/master/>`_: Generación automática de documentación a partir de docstrings (por eso docs lo usamos en el mismo repo).

+ `PyTest <https://docs.pytest.org/en/latest/>`_: Para pruebas unitarias.

+ `Black <https://github.com/psf/black>`_ como formateador. Permite ajustar el
   código de forma automática a PEP8. Usamos este por ser la herramienta
   recomendada por la PSF.

+ `SnakeViz <https://jiffyclub.github.io/snakeviz/>`_: Perfilamiento tiempos de ejecución.
+ `VProf <https://github.com/nvdv/vprof>`_: perfilamiento memoria.


pylint

pyreverse
pyan3
isort
ruff
