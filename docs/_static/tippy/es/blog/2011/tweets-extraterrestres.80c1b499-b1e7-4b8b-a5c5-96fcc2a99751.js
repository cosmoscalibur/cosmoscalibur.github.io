selector_to_html = {"a[href=\"#tweets-extraterrestres\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Tweets extraterrestres<a class=\"headerlink\" href=\"#tweets-extraterrestres\" title=\"Link to this heading\">#</a></h1><p>Hace casi 2 semanas estaba mirando tuits en el Twitter oficial de NASA\ny me pareci\u00f3 curioso ver un tuit de uno de los astronautas que estaba\nen la \u00faltima misi\u00f3n del transbordador Atlantis.</p><p>Los primeros tuits espaciales eran enviados por los tripulantes de la\nISS a NASA, quienes a trav\u00e9s de una cuenta de Twitter gen\u00e9rica para los\nastronautas, lo tuiteaban desde tierra. As\u00ed fue el caso de los primeros\nastronautas en establecer comunicaci\u00f3n en las redes sociales: Michael J.\nMassimino (@Astro_Mike), especialista de la misi\u00f3n STS-125 y Mark L.\nPolansky (@Astro_127), comandante de la misi\u00f3n STS-127.</p>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/primer-tuit-extraterrestre.jpg\"><img alt=\"Primer tuit desde el espacio, por Timothy Creamer.\" src=\"../../../../_images/primer-tuit-extraterrestre.jpg\" style=\"width: 320px; height: 208px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Primer tuit desde el espacio, por Timothy Creamer.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
