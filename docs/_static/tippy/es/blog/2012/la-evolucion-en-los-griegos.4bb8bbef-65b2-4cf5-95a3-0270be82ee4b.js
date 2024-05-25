selector_to_html = {"a[href=\"#la-evolucion-en-los-griegos\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">La evoluci\u00f3n en los griegos<a class=\"headerlink\" href=\"#la-evolucion-en-los-griegos\" title=\"Link to this heading\">#</a></h1><p>Hablando un poco de la evoluci\u00f3n biol\u00f3gica el d\u00eda de ayer, dando\ninicio a las actividades del ciclo de astrobiolog\u00eda en el Club Ori\u00f3n,\nse genero la inquietud sobre el origen griego de la evoluci\u00f3n, motivo\npor el cual me di a la tarea de buscar un poco y realizar esta breve\nrese\u00f1a.</p><p>Los primeros conceptos de evoluci\u00f3n (no necesariamente equivalentes a\nlos actuales) de las especies, surgen en la \u00e9poca griega asociados a\nla discusi\u00f3n sobre la sustancia primordial (que quienes ya hallan\npasado por filosof\u00eda en el colegio, recordaran que se trata del arj\u00e9),\na partir de la cual se generar\u00eda todo.</p>"}
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
