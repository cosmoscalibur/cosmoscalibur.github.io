selector_to_html = {"a[href=\"#la-antimateria-seria-anti-materia\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">La antimateria ser\u00eda anti-materia<a class=\"headerlink\" href=\"#la-antimateria-seria-anti-materia\" title=\"Link to this heading\">#</a></h1><p>La antimateria ser\u00eda verdaderamente anti-materia.</p>", "a[href=\"#id2\"]": "<figure class=\"align-center\" id=\"id2\">\n<img alt=\"Representaci\u00f3n gr\u00e1fica de la la antimateria y la simetr\u00eda CPT.\" src=\"../../../../_images/antimateria-simetria-cpt.png\"/>\n<figcaption>\n<p><span class=\"caption-text\">Representaci\u00f3n gr\u00e1fica de la la antimateria y la simetr\u00eda CPT</span><a class=\"headerlink\" href=\"#id2\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
