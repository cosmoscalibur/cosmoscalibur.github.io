selector_to_html = {"a[href=\"#edward-villegas\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Edward Villegas<a class=\"headerlink\" href=\"#edward-villegas\" title=\"Link to this heading\">#</a></h1><p>Desarrollador backend python y divulgador cient\u00edfico. Ingeniero f\u00edsico.\nOcasionalmente poeta y bloguero.</p><p>Astronom\u00eda \ud83c\udf0c\ud83c\udfd5\ufe0f Linux \ud83d\udc27\ud83d\udcbb Juegos \ud83c\udfae\u265f\ufe0f Ajedrez</p>"}
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
