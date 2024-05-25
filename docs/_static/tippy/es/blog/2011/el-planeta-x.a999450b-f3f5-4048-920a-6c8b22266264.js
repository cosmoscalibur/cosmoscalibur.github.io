selector_to_html = {"a[href=\"#el-planeta-x\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">El planeta X<a class=\"headerlink\" href=\"#el-planeta-x\" title=\"Link to this heading\">#</a></h1><p>Como sabemos, hace unos a\u00f1os consider\u00e1bamos en nuestro sistema solar 9 planetas e incluso la cuenta llego a aumentar a 10, y dejar como candidatos a otros tantos. Esto motivo a una revisi\u00f3n del concepto planeta por parte de la IAU, que elimino a Plut\u00f3n y al reciente candidato de la categor\u00eda de planetas y quedaron como planetas menores o planetoides.</p><p>Sin embargo, desde hace mucho ha persistido la historia de un planeta mayor en los confines del sistema solar, el hist\u00f3ricamente llamado planeta X que motivo la b\u00fasqueda de estos cuerpos y que en su momento condujo al descubrimiento de Neptuno, Plut\u00f3n, y los planetoide mas all\u00e1 de este.</p>"}
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
