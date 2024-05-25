selector_to_html = {"a[href=\"#imagenes-de-puntos-cuanticos\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Im\u00e1genes de puntos cu\u00e1nticos<a class=\"headerlink\" href=\"#imagenes-de-puntos-cuanticos\" title=\"Link to this heading\">#</a></h1><p>Por mas de una d\u00e9cada investigadores han intentado crear pantallas de\ntelevisor a partir de puntos cu\u00e1nticos. Te\u00f3ricamente los puntos cu\u00e1nticos\npodr\u00edan ofrecer im\u00e1genes de muy alta resoluci\u00f3n y altos niveles de eficiencia\nenerg\u00e9tica frente a los actuales televisores.</p>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<img alt=\"Pantalla de puntos cu\u00e1nticos.\" src=\"../../../../_images/pantalla-puntos-cuanticos.jpg\"/>\n<figcaption>\n<p><span class=\"caption-text\">Pantalla de puntos cu\u00e1nticos.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
