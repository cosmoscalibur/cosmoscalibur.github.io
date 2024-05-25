selector_to_html = {"a[href=\"#referencias\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Referencias<a class=\"headerlink\" href=\"#referencias\" title=\"Link to this heading\">#</a></h2>", "a[href=\"#dockerfile\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Dockerfile<a class=\"headerlink\" href=\"#dockerfile\" title=\"Link to this heading\">#</a></h2><p>Este archivo es el mecanismo mediante el cual se especifican las reglas de\nconstrucci\u00f3n de nuestra imagen. Se define un lenguaje com\u00fan sin importar el\nsistema operativo base y las funciones espec\u00edficas del sistema son usadas con\nuna instrucci\u00f3n que habilita a ejecuci\u00f3n en \u00e9l.</p><p>Los comentarios en el archivo son como tradicionalmente estamos acostumbrados\nen otros lenguajes (entre ellos, bash), con signo n\u00famero <code class=\"code docutils literal notranslate\"><span class=\"pre\">#</span></code>. Esto posee\nuna excepci\u00f3n, y es el caso donde existe una directriz despu\u00e9s como el caso que\nse ejemplificara.</p>", "a[href=\"#construir-imagen-docker\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Construir imagen Docker<a class=\"headerlink\" href=\"#construir-imagen-docker\" title=\"Link to this heading\">#</a></h2><p>La construcci\u00f3n la realizamos con la opci\u00f3n <code class=\"code docutils literal notranslate\"><span class=\"pre\">build</span></code>. Se usa el argumento\n<code class=\"code docutils literal notranslate\"><span class=\"pre\">-t</span></code> para indicar la etiqueta que asignaremos a la imagen y <code class=\"code docutils literal notranslate\"><span class=\"pre\">-f</span></code>\npara relacionar la ruta del archivo dockerfile que se usar\u00e1. El siguiente\nargumento no posee marca para indicarlo y corresponde al contexto, que viene a\nser la ruta donde se encuentran los archivos que usaremos (que puede ser\nreemplazado por un archivo de contexto con la ruta a los distintos archivos).</p>", "a[href=\"#instalar-docker\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Instalar Docker<a class=\"headerlink\" href=\"#instalar-docker\" title=\"Link to this heading\">#</a></h2><p>Recomiendo en Linux instalar docker con snap.</p>", "a[href=\"#crear-contenedor-docker-aplicacion-gui-ealite\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Crear contenedor Docker aplicaci\u00f3n GUI - EALite<a class=\"headerlink\" href=\"#crear-contenedor-docker-aplicacion-gui-ealite\" title=\"Link to this heading\">#</a></h1><p>Dando continuidad al uso de contenedores que inicie en la publicaci\u00f3n anterior,\n<a class=\"reference internal\" href=\"../crear-contenedor-lxc-para-aplicacion-gui-ealite/\"><span class=\"doc\">Crear contenedor LXC para aplicaci\u00f3n GUI - EALite</span></a>, reproducir\u00e9 la\ninstalaci\u00f3n de Enterprise Architect Viewer (EALite) con Docker (y por supuesto,\nWine). Si deseas reproducir el ejemplo de este caso, requieres reproducir la\nel art\u00edculo mencionado para extraer el directorio de Wine.</p><p>A diferencia de LXC, Docker est\u00e1 m\u00e1s orientado al aislamiento de aplicaciones y\nno de sistema operativo (LXC cumple una funci\u00f3n m\u00e1s cercana a una m\u00e1quina\nvirtual) lo cual ayuda a un mejor despliegue de aplicaciones y la\nestandarizaci\u00f3n de las etapas de desarrollo y de pruebas.</p>", "a[href=\"#ejecutar-contenedor\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Ejecutar contenedor<a class=\"headerlink\" href=\"#ejecutar-contenedor\" title=\"Link to this heading\">#</a></h2><p>Ahora puedes lanzar un contenedor gr\u00e1fico basado en la imagen construida con la\nsiguiente instrucci\u00f3n.</p>"}
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
