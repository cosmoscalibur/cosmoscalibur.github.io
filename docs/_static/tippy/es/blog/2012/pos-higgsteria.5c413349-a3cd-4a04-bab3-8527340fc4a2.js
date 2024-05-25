selector_to_html = {"a[href=\"#pos-higgsteria\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Pos-higgsteria<a class=\"headerlink\" href=\"#pos-higgsteria\" title=\"Link to this heading\">#</a></h1><p>A pesar del tiempo transcurrido desde el anuncio oficial del CERN, el 4 de Julio de 2012, sobre el descubrimiento de un nuevo bos\u00f3n masivo que ser\u00eda candidato al tan elusivo bos\u00f3n de Higgs, el tema sigue dando de que hablar.</p>"}
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
