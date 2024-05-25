selector_to_html = {"a[href=\"#el-planeta-de-einstein\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">El planeta de Einstein<a class=\"headerlink\" href=\"#el-planeta-de-einstein\" title=\"Link to this heading\">#</a></h1><p><em>El planeta de Einstein</em> como ha sido llamado el exoplaneta\n<a class=\"reference external\" href=\"http://en.wikipedia.org/wiki/Kepler-76b\">Kepler-76b</a> es la muestra\nde la reutilizaci\u00f3n de los datos del proyecto\n<a class=\"reference external\" href=\"http://www.blogger.com/\">Kepler</a> para la b\u00fasqueda de nuevos\nexoplanetas.</p><p>Se trata de un gigante gaseoso caliente (un j\u00fapiter caliente) a 2200 K\nde dos masas de j\u00fapiter y periodo orbital de 1.5 d\u00edas. Se encuentra en\nla constelaci\u00f3n de Cygnus a 2000 a\u00f1os luz.</p>", "a[href=\"#id2\"]": "<figure class=\"align-center\" id=\"id2\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/kepler-76b.jpg\"><img alt=\"Concepto art\u00edstico del planeta Kepler-76b.\" src=\"../../../../_images/kepler-76b.jpg\" style=\"width: 320px; height: 182px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Concepto art\u00edstico del planeta de Einstein, formalmente conocido como\nKepler-76b. (Image: \u00a9 David A. Aguilar (CfA))</span><a class=\"headerlink\" href=\"#id2\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
