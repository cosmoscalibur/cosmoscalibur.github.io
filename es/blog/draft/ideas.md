```
sudo dd bs=4M if=manjaro-kde-24.1.2-241104-linux610.iso of=/dev/sda status=progress oflag=sync
```

(sin número, solo letra) lsblk/lsusb - mount

- script oficial (con opciones de actualización): rust, uv, zed, ollama

- PIP/UV/Pixi (uv tool install): ruff, python-lsp-analyzer, sphinx, mdformat

- Cargo (requiere descargar muchas dependencias y tiempo de compilación, acumula
  caché): rust-analyzer

- snap (algunos casos privativos): vscode

- manjaro repo: flameshot, dbeaver

- Flatpak (viene preinstalado y con la configuración del repositorio. Instalar
  solo si el autor es verificado): dbgate, stremio, stellarium

- AUR (no hay verificación, de manera responsable requiere inspección o al menos
  validar popularidad y votos de confianza, leer comentarios y trazabilidad, y
  suele requerir compilación o pasos intermedios de transformaciones. Puede que
  se omitan componentes privativas si es un tercero el empaquetador):
  wps-office-bin, google-chrome, dropbox, slack-desktop

- Gmail

  - Slack
  - Notion
  - Sentry

- GitHub

  - Extensión de ZenHub

- 1Password (tech@tributi.com)

  - Loom
  - Airtable
  - Wompi

```{code}
pamac install python-lsp-server rust-analyzer
```

https://deno.com/ https://voidzero.dev/

ibis polars pandas fireducks probar que pasa entre pandas y fireducs si hay una
tabla con columna sin consistencia de datos y subtabla muy pequeña que deja
muchos vacíos

graphviz

pikepdf mupdf pypdf2

weazyprint pandoc

sympy gamma

vulture django
https://adamj.eu/tech/2023/07/12/django-clean-up-unused-code-vulture/

simulación placas diferencias finitas mallas gmsh visualización paraview - vtk

three.js d3.js

bokeh https://bokeh.org/ seaborn https://seaborn.pydata.org/index.html
matplotlib https://matplotlib.org/ altair vega
https://altair-viz.github.io/index.html

gmsh https://gmsh.info/ vtk https://www.kitware.com/

paraview https://www.kitware.com/ mayavi
http://docs.enthought.com/mayavi/mayavi/ ipyvolume
https://ipyvolume.readthedocs.io/en/latest/ yt https://yt-project.org/ pyvista
https://docs.pyvista.org/

bevy pygame pymunk rapier matter.js

vispy https://vispy.org/ holovyz https://holoviz.org/ holoviews
https://holoviews.org/

histcite
https://support.clarivate.com/ScientificandAcademicResearch/s/article/HistCite-No-longer-in-active-development-or-officially-supported?language=en_US
vosviewer https://www.vosviewer.com/

convertir mi tésis a html LaTeX a HTML -> tex4ht https://tug.org/tex4ht/ ->
Latexml https://math.nist.gov/~BMiller/LaTeXML/
https://www.universityofgalway.ie/media/accessibility/files/Converting-LaTeX-notes-to-HTML.pdf
-> htlatex
https://data-mining.philippe-fournier-viger.com/how-to-convert-latex-to-html/ ->
Myst https://mystmd.org/guide/writing-in-latex -> Pandoc
https://medium.com/@hjhuney/how-to-convert-latex-into-html-a4334ffda3f4
https://www.homepages.ucl.ac.uk/~ucahmto/elearning/latex/2019/06/10/pandoc.html

matomo en vez de analytics https://matomo.org/plausible-vs-matomo/

Alternativas a la licencia de Anaconda

- Canal conda-forge
- Prefix_dev Conda en si mismo no es el problema, es el canal default o anaconda
  https://prefix.dev/blog/towards_a_vendor_lock_in_free_conda_experience
  https://x.com/wuoulf/status/1821934424021242227
  https://x.com/rabernat/status/1826266881415917901

Pixi vs conda vs mamba https://prefix.dev/blog/pixi_a_fast_conda_alternative
https://prefix.dev/blog/pixi_for_scientists
https://prefix.dev/blog/using_python_projects_with_pixi
https://prefix.dev/blog/introducing_multi_env_pixi
https://prefix.dev/blog/uv_in_pixi
https://x.com/rahuldave/status/1826304830966485178

Crear instaladores de aplicaciones Python en 2024
https://stackoverflow.com/questions/33168229/how-to-create-standalone-executable-file-from-python-3-5-scripts/33174611#33174611
Lo tradicional: Pyinstaller https://pyinstaller.org/en/stable/ py2exe bbfreeze
cx_freeze Lo nuevo PyApp https://github.com/ofek/pyapp Pixi Pack
https://github.com/Quantco/pixi-pack

uv vs pixi

python en la web pyodide pyscript jupyterlite

sympy https://www.sympy.org/es/ symbolica https://symbolica.io/

igraph https://igraph.org/ networkx https://networkx.org/

octave https://octave.org/ matlab

yaak https://yaak.app/ postman

tauri https://tauri.app/ slint https://slint.dev/

https://github.com/executablebooks/mdformat
