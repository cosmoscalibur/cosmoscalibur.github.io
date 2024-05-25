selector_to_html = {"a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/ofion-y-eurinome.png\"><img alt=\"../../../../_images/ofion-y-eurinome.png\" src=\"../../../../_images/ofion-y-eurinome.png\" style=\"width: 105px; height: 200px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Ofi\u00f3n calentando el huevo depositado por Eur\u00ednome.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#cosmogonia-griega\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Cosmogon\u00eda griega<a class=\"headerlink\" href=\"#cosmogonia-griega\" title=\"Link to this heading\">#</a></h1><p>La cosmogon\u00eda y cosmolog\u00eda de los antiguos griegos se encuentra\nprofundamente vinculada. Sus elementos cosmol\u00f3gicos si bien prescinden\nde la mitolog\u00eda desde los razonamientos del primer fil\u00f3sofo griego,\n<a class=\"reference external\" href=\"http://es.wikipedia.org/wiki/Tales_de_Mileto\">Tales de Mileto</a>, se\npuede rastrear el origen de algunos de estos en ella.\nLos relatos de la cosmogon\u00eda griega pueden ubicarse en los textos de\n<a class=\"reference external\" href=\"http://es.wikipedia.org/wiki/Homero\">Homero</a> y la\n<a class=\"reference external\" href=\"http://es.wikipedia.org/wiki/Teogon%C3%ADa\">Teogon\u00eda</a> de\n<a class=\"reference external\" href=\"http://es.wikipedia.org/wiki/Hesiodo\">Hes\u00edodo</a>, en los que se\nilustra la estructura de su universo y sus dioses.</p>", "a[href=\"#id2\"]": "<figure class=\"align-center\" id=\"id2\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/urano-y-gea.jpg\"><img alt=\"../../../../_images/urano-y-gea.jpg\" src=\"../../../../_images/urano-y-gea.jpg\" style=\"width: 200px; height: 146px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Urano y Gea, primera generaci\u00f3n de dioses de la teogon\u00eda griega.</span><a class=\"headerlink\" href=\"#id2\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#id3\"]": "<figure class=\"align-center\" id=\"id3\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/cosmologia-mesopotamica-tierra-plana.jpg\"><img alt=\"../../../../_images/cosmologia-mesopotamica-tierra-plana.jpg\" src=\"../../../../_images/cosmologia-mesopotamica-tierra-plana.jpg\" style=\"width: 320px; height: 212px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Cosmolog\u00eda mesopot\u00e1mica con una Tierra plana, extendida en las primeras cosmogon\u00edas. Adaptaci\u00f3n de <em>New American Bible</em>.</span><a class=\"headerlink\" href=\"#id3\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
