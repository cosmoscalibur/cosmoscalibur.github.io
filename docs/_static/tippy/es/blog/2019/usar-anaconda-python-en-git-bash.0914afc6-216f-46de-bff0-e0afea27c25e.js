selector_to_html = {"a[href=\"#git-bash\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Git Bash<a class=\"headerlink\" href=\"#git-bash\" title=\"Link to this heading\">#</a></h2><p>Si bien puedes descargarlo desde el sitio del proyecto, aprovecharemos el\ngestor Conda para facilitar la tarea de descarga, instalaci\u00f3n y configuraci\u00f3n.</p><p>Abriremos Anaconda PowerShell o Anaconda Prompt, y ejecutaremos lo siguiente:</p>", "a[href=\"#usar-anaconda-python-en-git-bash\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Usar Anaconda Python en Git Bash<a class=\"headerlink\" href=\"#usar-anaconda-python-en-git-bash\" title=\"Link to this heading\">#</a></h1><p>Recientemente, por motivos laborales he tenido que trabajar en Windows y es\npor esto que tuve la necesidad de buscar una opci\u00f3n c\u00f3moda de usar <a class=\"reference external\" href=\"https://git-scm.com/\">Git</a>\nen Windows, con soporte de <a class=\"reference external\" href=\"https://www.gnu.org/software/bash/\">Bash</a> a lo\nque estoy acostumbrado en Linux y con Python Anaconda reconocido. De alguna\nmanera, la versi\u00f3n m\u00ednima de como usar Windows sin morir en el intento.</p>", "a[href=\"#anaconda-python\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Anaconda Python<a class=\"headerlink\" href=\"#anaconda-python\" title=\"Link to this heading\">#</a></h2><p>Lo primero es proceder a instalar Anaconda Python desde su sitio oficial, pero\nrecomiendo revisar primero la necesidad real de tener todo lo incluido en\nAnaconda o usar algo minimalista como Miniconda. Anaconda representar\u00e1 una\ninstalaci\u00f3n y descarga de casi 500 MB, y por ende un mayor tiempo en ambos\npasos. Por otro lado, Miniconda solo instala lo m\u00ednimo requerido para tener\nPython y el gestor de paquetes Conda. Esta \u00faltima opci\u00f3n es recomendable si\nposees poco espacio en disco, deseas instalar r\u00e1pidamente, solo deseas probar\nlo b\u00e1sico de Python o el equipo es de bajas caracter\u00edsticas (recuerdo casos en\nlos cuales mis estudiantes -\u00e9pocas de docente- la sola instalaci\u00f3n de Anaconda\nbloqueaba el equipo y lo reiniciaba).</p><p>Si usas Anaconda para tus proyectos de desarrollo y usando buenas pr\u00e1cticas,\nseguramente estar\u00e1s acostumbrado a usar ambientes y en ese caso no necesitas\ntener tantas cosas en el base, siendo buena opci\u00f3n Miniconda tambi\u00e9n.</p>"}
skip_classes = ["headerlink", "sd-stretched-link"]

window.onload = function () {
    for (const [select, tip_html] of Object.entries(selector_to_html)) {
        const links = document.querySelectorAll(`article.bd-article ${select}`);
        for (const link of links) {
            if (skip_classes.some(c => link.classList.contains(c))) {
                continue;
            }

            tippy(link, {
                content: tip_html,
                allowHTML: true,
                arrow: true,
                placement: 'auto-start', maxWidth: 500, interactive: false,

            });
        };
    };
    console.log("tippy tips loaded!");
};
