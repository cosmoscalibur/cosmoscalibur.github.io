selector_to_html = {"a[href=\"#la-tierra-cambio-despues-del-terremoto-de-japon\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">La Tierra cambio despu\u00e9s del terremoto de Jap\u00f3n<a class=\"headerlink\" href=\"#la-tierra-cambio-despues-del-terremoto-de-japon\" title=\"Link to this heading\">#</a></h1><p>Tal vez el t\u00edtulo de la publicaci\u00f3n dice poco, porque la Tierra siempre esta en\nun cambio continuo as\u00ed no lo percibamos. Constantemente la masa de la Tierra\naumenta por la deposici\u00f3n sobre ella de toneladas de material c\u00f3smico, como por\nejemplo, el material de meteoros, meteoritos, aerolitos y otros durante las\nlluvias de estrellas. As\u00ed mismo, las interacciones gravitacionales con la luna\ny el sol deforman (despreciable) la superficie terrestre y frenan la rotaci\u00f3n\nterrestre. Las placas tect\u00f3nicas se desplazan, hunden y alzan continuamente.\nPero bajo ciertos fen\u00f3menos, estos cambios son mas apreciables.</p><p>El d\u00eda viernes 11 de Marzo observamos como Jap\u00f3n era sacudida por un terremoto\nde magnitud 9.1 (la magnitud fue actualizada en una revisi\u00f3n del 11 de julio\nde 2016, respecto a los 8.9 inicialmente publicados) en la escala de Richter a\nlas 2:46 PM hora local en el epicentro (0:46 AM hora colombiana). El epicentro\nse ubico cerca de la costa este de Honshu (130 km de Sendai, 373 Km de Tokio),\na una profundidad de 24.4 Km.</p>"}
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
