selector_to_html = {"a[href=\"#resignacion\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Resignaci\u00f3n<a class=\"headerlink\" href=\"#resignacion\" title=\"Link to this heading\">#</a></h1><p>No s\u00e9 qu\u00e9 sucede, con el tiempo algo extra\u00f1o ocurre y no encuentro\nexactamente qu\u00e9 es.</p><p>Esto no lo puedo describir, solo est\u00e1 sucediendo, y yo soy su v\u00edctima.\nUna v\u00edctima que no puede escapar.</p>"}
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
