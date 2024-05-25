selector_to_html = {"a[href=\"#nostalgia\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Nostalgia<a class=\"headerlink\" href=\"#nostalgia\" title=\"Link to this heading\">#</a></h1><p>Es el inevitable y fijo paso del tiempo, una maquinaria de evoluci\u00f3n,\nrecuerdos y olvidos.</p><p>Con precisi\u00f3n nos revele una naturaleza inevitable, un destino com\u00fan\nque no tiene m\u00e1s raz\u00f3n que una ley f\u00edsica, una rifa segura por un\npremio de entrop\u00eda.</p>"}
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
