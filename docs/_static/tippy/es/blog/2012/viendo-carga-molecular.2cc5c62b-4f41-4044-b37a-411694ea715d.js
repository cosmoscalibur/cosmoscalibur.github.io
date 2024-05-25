selector_to_html = {"a[href=\"#viendo-carga-molecular\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Viendo carga molecular<a class=\"headerlink\" href=\"#viendo-carga-molecular\" title=\"Link to this heading\">#</a></h1><p>Cient\u00edficos de IBM fueron capaz de medir por primera vez la distribuci\u00f3n\nde carga de una mol\u00e9cula individual. Este logro permitir\u00e1 dar nuevas\nluces acerca de la formaci\u00f3n de enlaces\nentre \u00e1tomos y mol\u00e9culas, as\u00ed como el estudio de\ndistribuci\u00f3n electr\u00f3nicas con estructuras moleculares funcionales.</p><p>Esta observaci\u00f3n se logro mediante el uso de una modificaci\u00f3n de la\nt\u00e9cnica de microscopia de fuerza at\u00f3mica (AFM por sus siglas en ingles).\nEsta t\u00e9cnica usa una muy peque\u00f1a punta (cuya terminaci\u00f3n es de\ntama\u00f1o at\u00f3mico) que interact\u00faa con las nubes de carga de la superficie\nde inter\u00e9s experimentando repulsi\u00f3n/atracci\u00f3n conforme nos acercamos.</p>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/stm-esquematico.png\"><img alt=\"../../../../_images/stm-esquematico.png\" src=\"../../../../_images/stm-esquematico.png\" style=\"width: 320px; height: 257px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Esquem\u00e1tico de un STM.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#id2\"]": "<figure class=\"align-center\" id=\"id2\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/micrografia-naftalocianina.jpg\"><img alt=\"../../../../_images/micrografia-naftalocianina.jpg\" src=\"../../../../_images/micrografia-naftalocianina.jpg\" style=\"width: 320px; height: 257px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Micrograf\u00eda de naftalocianina.</span><a class=\"headerlink\" href=\"#id2\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
