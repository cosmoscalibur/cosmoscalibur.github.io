ngrok

https://github.com/sts10/rust-command-line-utilities
zellij
zed
dog
eza
bat
hyperfine
diffstatic

ibis
polars
pandas

graphviz

pikepdf
mupdf
pypdf2

weazyprint
pandoc

sympy gamma

vulture django https://adamj.eu/tech/2023/07/12/django-clean-up-unused-code-vulture/

simulación placas
diferencias finitas
mallas gmsh
visualización paraview - vtk

three.js
d3.js

bokeh https://bokeh.org/
seaborn https://seaborn.pydata.org/index.html
matplotlib https://matplotlib.org/
altair vega https://altair-viz.github.io/index.html

gmsh https://gmsh.info/
vtk https://www.kitware.com/

paraview https://www.kitware.com/
mayavi http://docs.enthought.com/mayavi/mayavi/
ipyvolume https://ipyvolume.readthedocs.io/en/latest/
yt https://yt-project.org/
pyvista https://docs.pyvista.org/

bevy
pygame pymunk
rapier
matter.js

vispy https://vispy.org/
holovyz https://holoviz.org/
holoviews https://holoviews.org/

histcite https://support.clarivate.com/ScientificandAcademicResearch/s/article/HistCite-No-longer-in-active-development-or-officially-supported?language=en_US
vosviewer https://www.vosviewer.com/

convertir mi tésis a html
LaTeX a HTML
-> tex4ht https://tug.org/tex4ht/
-> Latexml https://math.nist.gov/~BMiller/LaTeXML/ https://www.universityofgalway.ie/media/accessibility/files/Converting-LaTeX-notes-to-HTML.pdf
-> htlatex https://data-mining.philippe-fournier-viger.com/how-to-convert-latex-to-html/
-> Myst https://mystmd.org/guide/writing-in-latex
-> Pandoc https://medium.com/@hjhuney/how-to-convert-latex-into-html-a4334ffda3f4 https://www.homepages.ucl.ac.uk/~ucahmto/elearning/latex/2019/06/10/pandoc.html




Recomendaciones python

NEP29: versiones soportadas de python y numpy
licencias
ciclo de vida de paquetes
Estructura de paquete recomendada por la PSF: docs, <paquete>, tests. En el paquete se sigue la recomendación de máximo 4 niveles de profundidad para acceder a una función. Toda función, módulo y clase debe contener docstrings.
Linters
- pycodestyle pep8
- pydocstyle pep257
- mccabe: complejidad ciclomática
- pyflakes vs mypy: errores por análisis estático
- radon: métrica de mantenibilidad
- Pylama integra anteriores
- Ruff
- Pylint
- Análisis de acomplamiento pyreverse
- Vulture
- perflint https://github.com/tonybaloney/perflint
- pyinstrument https://pyinstrument.readthedocs.io/en/latest/
Documentación
- Sphinx
Unitarias
- Pytest
Formateo:
- Black
- Yapf
- Ruff
Perfilamiento
- Snakeviz
- Vprof
- flamegraph
- Linux Perf https://docs.python.org/pl/dev/howto/perf_profiling.html
- memray https://github.com/bloomberg/memray

Alternativas a la licencia de Anaconda
- Canal conda-forge
- Prefix_dev
Conda en si mismo no es el problema, es el canal default o anaconda
https://prefix.dev/blog/towards_a_vendor_lock_in_free_conda_experience
https://x.com/wuoulf/status/1821934424021242227
https://x.com/rabernat/status/1826266881415917901


Pixi vs conda vs mamba
https://prefix.dev/blog/pixi_a_fast_conda_alternative
https://prefix.dev/blog/pixi_for_scientists
https://prefix.dev/blog/using_python_projects_with_pixi
https://prefix.dev/blog/introducing_multi_env_pixi
https://prefix.dev/blog/uv_in_pixi
https://x.com/rahuldave/status/1826304830966485178

Crear instaladores de aplicaciones Python en 2024
https://stackoverflow.com/questions/33168229/how-to-create-standalone-executable-file-from-python-3-5-scripts/33174611#33174611
Lo tradicional:
Pyinstaller https://pyinstaller.org/en/stable/
py2exe
bbfreeze
cx_freeze
Lo nuevo
PyApp https://github.com/ofek/pyapp
Pixi Pack https://github.com/Quantco/pixi-pack


uv vs pixi

python en la web
pyodide
pyscript
jupyterlite

sympy https://www.sympy.org/es/
symbolica https://symbolica.io/

igraph https://igraph.org/
networkx https://networkx.org/

octave https://octave.org/
matlab

yaak https://yaak.app/
postman

tauri https://tauri.app/
slint https://slint.dev/