selector_to_html = {"a[href=\"#calculan-masa-del-agujero-negro-mas-grande\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Calculan masa del agujero negro m\u00e1s grande<a class=\"headerlink\" href=\"#calculan-masa-del-agujero-negro-mas-grande\" title=\"Link to this heading\">#</a></h1><p>El astr\u00f3nomo Karl Gebhardt de la University of Texas, Austin, presento los resultados de su equipo de investigaci\u00f3n el 12 de enero en el encuentro 217 de la Sociedad Americana de Astronom\u00eda. Su equipo calculo la masa y horizonte de eventos del agujero negro de la galaxia M87 (NGC4486) (galaxia el\u00edptica de magnitud aparente 8.6 ubicada a 55 millones de a\u00f1os luz en la constelaci\u00f3n de virgo).</p><p>El astr\u00f3nomo afirmo que su tama\u00f1o es tal que es 4 veces el tama\u00f1o de la \u00f3rbita de Neptuno, y 3 veces el tama\u00f1o de la \u00f3rbita de Plut\u00f3n, en otras palabras podr\u00eda tragarse nuestro sistema solar completo.</p>"}
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
