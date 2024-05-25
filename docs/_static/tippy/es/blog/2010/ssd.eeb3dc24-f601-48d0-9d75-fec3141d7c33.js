selector_to_html = {"a[href=\"#ssd\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">SSD<a class=\"headerlink\" href=\"#ssd\" title=\"Link to this heading\">#</a></h1><p>Como todo en la tecnolog\u00eda, los pasos en la evoluci\u00f3n de un sistema son agigantados.</p><p>Los discos duros de nuestros computadores son precisamente uno de esos elementos tecnol\u00f3gicos que gracias a la investigaci\u00f3n aplicada en \u00e1reas como la mec\u00e1nica cu\u00e1ntica y el estado solido, a logrado cada vez almacenar una mayor cantidad de informaci\u00f3n, con mejores tasas de transferencia de esta en un espacio f\u00edsico reducido, con tendencia a disminuir cada vez mas.</p>"}
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
