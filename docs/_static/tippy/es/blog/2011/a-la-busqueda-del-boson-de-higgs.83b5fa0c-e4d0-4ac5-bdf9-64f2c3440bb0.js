selector_to_html = {"a[href=\"#a-la-busqueda-del-boson-de-higgs\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">A la b\u00fasqueda del bos\u00f3n de Higgs<a class=\"headerlink\" href=\"#a-la-busqueda-del-boson-de-higgs\" title=\"Link to this heading\">#</a></h1><p>Este mes de febrero los investigadores del <a class=\"reference external\" href=\"http://home.cern/topics/large-hadron-collider\">LHC</a> del CERN han renovado su b\u00fasqueda de uno de los misterios mas elusivos del universo, el bos\u00f3n de Higgs.\nEl bos\u00f3n de Higgs es una hipot\u00e9tica part\u00edcula predicha por el modelo est\u00e1ndar de la f\u00edsica de part\u00edculas (la \u00fanica de dicho modelo sin confirmaci\u00f3n experimental) de gran energ\u00eda y que cumple con la funci\u00f3n de dotar de masa a las dem\u00e1s part\u00edculas existentes.</p><p>El bos\u00f3n de Higgs posee asociado un campo escalar que permea todo el universo, que es el campo escalar de Higgs, el cual es el que propiamente dicho, dota la propiedad de masa en el medio, mediante un mecanismo din\u00e1mico de creaci\u00f3n de masa.</p>"}
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
