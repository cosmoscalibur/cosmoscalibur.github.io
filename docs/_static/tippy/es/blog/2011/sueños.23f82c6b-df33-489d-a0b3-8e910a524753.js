selector_to_html = {"a[href=\"#suenos\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Sue\u00f1os<a class=\"headerlink\" href=\"#suenos\" title=\"Link to this heading\">#</a></h1><p>Son los sue\u00f1os una realidad inimaginable, llena de grandes momentos de\nfrenes\u00ed y \u00e9xtasis. Realidades nacidas de la manifestaci\u00f3n de necesidad\nde estas o de rebeld\u00eda ante la realidad cl\u00e1sica que se nos ha condenado\na vivir. Se\u00f1ales de advertencia, estados de reminiscencia de momentos de\ninconsciencia, escape desesperado de la realidad y sus problemas, en una\nb\u00fasqueda aguda de soluciones o viajes inconcebibles en el espacio-tiempo\nsin barreras f\u00edsicas.</p><p>Ser\u00eda m\u00e1s f\u00e1cil vivir eternamente en un mundo de ensue\u00f1o lleno de\nfantas\u00edas y no de duros golpes a tu coraz\u00f3n.</p>"}
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
