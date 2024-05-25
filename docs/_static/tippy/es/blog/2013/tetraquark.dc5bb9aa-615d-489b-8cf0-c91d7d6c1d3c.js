selector_to_html = {"a[href=\"#tetracuark\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">\u00bfTetracuark?<a class=\"headerlink\" href=\"#tetracuark\" title=\"Link to this heading\">#</a></h1><p>Bueno, resulta que el mundo de la f\u00edsica de part\u00edculas viene en un\ncontinuo agitar, y nuevos datos y modelos surgen a partir de los\nexperimentos realizados en los grandes aceleradores de part\u00edculas (esos\nt\u00faneles enormes en los cuales se hace que part\u00edculas a muy alta\nvelocidad colisionen).</p><p>Lo \u00faltimo en este revuelo, concierne a una nueva part\u00edcula que apoya el\nmodelo molecular de cuarks, en el cual se pueden presentar mesones\nh\u00edbridos, que son part\u00edculas constituidas por combinaci\u00f3n de mesones,\nsiendo as\u00ed part\u00edculas constituidas por 4 cuarks.</p>"}
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
