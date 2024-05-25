selector_to_html = {"a[href=\"#bio\"]": "<aside class=\"footnote brackets\" id=\"bio\" role=\"doc-footnote\">\n<span class=\"label\"><span class=\"fn-bracket\">[</span><a href=\"#id2\" role=\"doc-backlink\">2</a><span class=\"fn-bracket\">]</span></span>\n<p><a class=\"reference external\" href=\"http://multimedia.mcb.harvard.edu/\">BioVisions</a>.</p>\n</aside>", "a[href=\"#recorrido-por-la-celula\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Recorrido por la c\u00e9lula<a class=\"headerlink\" href=\"#recorrido-por-la-celula\" title=\"Link to this heading\">#</a></h1><p>Creo que el mundo vivo a cualquier escala puede exhibir una majestuosa belleza, y que esta es inspiraci\u00f3n para que el arte cree una copia de la misma y la transmita.\nParte de esta belleza de la vida no solo esta en sus formas (reconstruidas por curvas matem\u00e1ticas, muchas de naturaleza fractal) sino tambi\u00e9n por su din\u00e1mica, compleja y precisa.</p>", "a[href=\"#ted\"]": "<aside class=\"footnote brackets\" id=\"ted\" role=\"doc-footnote\">\n<span class=\"label\"><span class=\"fn-bracket\">[</span><a href=\"#id3\" role=\"doc-backlink\">3</a><span class=\"fn-bracket\">]</span></span>\n<p><a class=\"reference external\" href=\"https://www.ted.com/talks/david_bolinsky_animates_a_cell\">Visualizing the wonder of a living cell</a> (Marzo de 2007).</p>\n</aside>", "a[href=\"#news\"]": "<aside class=\"footnote brackets\" id=\"news\" role=\"doc-footnote\">\n<span class=\"label\"><span class=\"fn-bracket\">[</span><a href=\"#id1\" role=\"doc-backlink\">1</a><span class=\"fn-bracket\">]</span></span>\n<p><a class=\"reference external\" href=\"http://www.studiodaily.com/2006/07/cellular-visions-the-inner-life-of-a-cell/\">StudioDaily</a> Cellular Visions: The Inner Life of a Cell (July 20, 2006).</p>\n</aside>"}
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
