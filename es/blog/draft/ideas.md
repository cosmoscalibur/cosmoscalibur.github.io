ngrok

https://github.com/sts10/rust-command-line-utilities



apt update -q && apt dist-upgrade -y

Instalar manual (web)
    Dropbox
    Google Chrome

Common dependencies to compile

sudo apt install -y build-essential cmake curl pkg-config git ca-certificates
sudo apt install -y libfreetype6-dev libfontconfig1-dev libxcb-xfixes0-dev libxkbcommon-dev

sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

Activar teclado numérico desde booteo
https://wiki.archlinux.org/title/Activating_numlock_on_bootup#KDE_Plasma

rust
    # Viene 1.79 a 1.81. Defecto 1.80. Ahora es 1.82
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Linux utilities
    # bat: cat
    # bottom (btm): top
    # du-dust (dust): du
    # eza: ls
    # fd-find: find
    # ripgrep: grep
    # bottom: top/htop
    # procs: ps
    cargo install --locked bat bottom du-dust eza fd-find procs ripgrep
    sudo apt install -y fzf

alacritty: terminal emulator (rs)
    sudo apt install -y alacritty  # man pages, logo, desktop entry
    sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator $(which alacritty) 70
    # sudo update-alternatives --config x-terminal-emulator ## check

    # Atajo de teclado
    # Aplicaciones por defecto

zellij: multiplexer (rs)
    cargo install --locked zellij
    # Ejecutar zellij en alacritty
    mkdir -p ~/.config/alacritty
    cat << EOF >  ~/.config/alacritty/alacritty.toml
    [shell]
    args = ["-l", "-c", "zellij attach --index 0 || zellij"]
    program = "/usr/bin/bash"
    EOF

starship: prompt (rs)
    curl -sS https://starship.rs/install.sh | sh
    echo 'eval "$(starship init bash)"' >> ~/.bashrc


Development (rs)
    cargo install --locked difftastic just hyperfine

    curl -f https://zed.dev/install.sh | sh
    echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc
    # https://github.com/zed-industries/zed/issues/10943

    sudo snap install --classic helix
    cargo install --locked evcxr_jupyter  # Rust jupyter kernel
    cargo install --locked shellharden  # shellcheck
    sudo apt install -y shellcheck shfmt

    curl -LsSf https://astral.sh/uv/install.sh | sh  # Python


https://github.com/vitallium/zed-ltex


cargo install --locked yazi-fm yazi-cli  # file manager terminal

code: IDE
    sudo snap install --classic code
    extensions:
        timonwong.shellcheck
        mads-hartmann.bash-ide-vscode
        eamodio.gitlens
        executablebookproject.myst-highlight
        ms-python.python
        rust-lang.rust-analyzer
        swyddfa.esbonio
        ms-azuretools.vscode-docker
        ban.spellright
    ln -s /usr/share/hunspell/* ~/.config/Code/Dictionaries

sudo apt install -y imagemagick ffmpeg
sudo apt install -y gimp inkscape
flatpak install -y flathub com.obsproject.Studio

sudo apt install -y steam-installer
flatpak install -y flathub com.stremio.Stremio
sudo snap install spotify

sudo snap install telegram-desktop discord slack


git config --global user.email "cosmoscalibur@gmail.com"
git config --global user.name "Edward Villegas-Pulgarin"
git config --global pull.rebase true

# https://ollama.com/download
# https://ollama.com/library/llama3.1:8b
# https://ollama.com/blog/continue-code-assistant

curl -fsSL https://ollama.com/install.sh | sh  # Puede tomar un buen rato 14m30s
ollama run llama3.1:8b
ollama run llama3.2:3b
#>>> The Ollama API is now available at 127.0.0.1:11434.
#>>> Install complete. Run "ollama" from the command line.
#>>> AMD GPU ready.


Defecto
- krita (3rd package - 2d)
- libreoffice
- haruna (video, en lugar de vlc)
- elisa (música)
- okular (pdf)
- dolphin (gestor de directorios/archivos)
- spectacle (captura de pantalla, en lugar de flameshot)
- 7zip 7zip-rar (compressión, línea de comandos)
- kwallet (contraseña)

hunspell es
rla-es
spellchecker vscode

Se produjo un error mientras se accedía a «EdDisk», el sistema respondió: La operación solicitada ha fallado: Error mounting /dev/sda1 at /media/cosmoscalibur/EdDisk: wrong fs type, bad option, bad superblock on /dev/sda1, missing codepage or helper program, or other error







https://deno.com/
https://voidzero.dev/

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


matomo en vez de analytics
https://matomo.org/plausible-vs-matomo/

multiple kernel en un notebook
https://vatlab.github.io/sos-docs/

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


Problema de actualización posiblemente por internet era
sudo rm /usr/share/keyrings/cloud.google.gpg~
sudo rm /usr/share/keyrings/cloud.google.gpg~
sudo rm /etc/apt/sources.list.d/google-cloud-sdk.list


cosmoscalibur@edgamer:~$ sudo do-release-upgrade
[sudo] contraseña para cosmoscalibur:
Comprobar si hay una nueva versión de Ubuntu
No hay una versión de desarrollo de una LTS disponible.
Para actualizar al último lanzamiento de desarrollo sin LTS
defina «Prompt=normal» en /etc/update-manager/release-upgrades.
el valor cuando es lts es lts y solo salta a lts

Comprobar si hay una nueva versión de Ubuntu
Instale todas las actualizaciones disponibles de su versión antes de actualizar la distribución.

sudo apt update && sudo apt full-upgrade -y

sudo do-release-upgrade

No te voy a mentir, es algo irresponsable, pero la respuesta a casi todo es "Sí" (`s`).
Salvo que realmente entiendas a que se refiere la pregunta y seas consciente de la necesidad
de responder "No" (`n`), indica `s`. La primera pregunta es si realmente deseas actualizar la
versión de la distribución, pero las siguientes son sobre actualización de configuración de paquetes específicos que probablemente ni sabes que existen
y que su configuración cambió por el mismo desarrollador y no por un cambio tuyo. Igualmente tendremos
pasos de única opción en los cuales la pantalla completa solo nos permite dar _enter_ a un "Aceptar".
Y sobre desinstalación (que puede tomar horas). Finalmente, es sobre aceptar el reinicio.
