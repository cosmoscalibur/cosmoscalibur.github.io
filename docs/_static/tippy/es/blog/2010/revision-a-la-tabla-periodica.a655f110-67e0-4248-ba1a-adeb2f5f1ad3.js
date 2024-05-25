selector_to_html = {"a[href=\"#revision-a-la-tabla-periodica\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Revisi\u00f3n a la tabla peri\u00f3dica<a class=\"headerlink\" href=\"#revision-a-la-tabla-periodica\" title=\"Link to this heading\">#</a></h1><p>Nuestros conocimientos sobre la naturaleza y universo que nos rodean cambian constantemente, y exigen su continua y peri\u00f3dica revisi\u00f3n y actualizaci\u00f3n, por las diversas necesidades para las \u00e1reas acad\u00e9micas, de investigaci\u00f3n e industriales.</p><p>Uno de estos elementos de nuestro conocimiento que ahora sigue a su revisi\u00f3n es la tabla peri\u00f3dica, despu\u00e9s de permanecer inamovible durante mucho tiempo, solo agregando nuevos elementos pero con el mismo esquema de casi un siglo.</p>"}
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
