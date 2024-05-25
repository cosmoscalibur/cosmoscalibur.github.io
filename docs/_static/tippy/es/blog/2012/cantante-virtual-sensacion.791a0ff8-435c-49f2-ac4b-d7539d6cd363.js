selector_to_html = {"a[href=\"#cantante-virtual-sensacion\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Cantante virtual sensaci\u00f3n<a class=\"headerlink\" href=\"#cantante-virtual-sensacion\" title=\"Link to this heading\">#</a></h1><p>Como toda una historia futurista y ciencia ficci\u00f3n, como la de William\nGibson es su obra <em>Idoru</em> que en japones significa \u00ab\u00eddolo\u00bb, una\ncantante totalmente virtual se encuentra en el top de ventas de las\nlistas japonesas, y ademas da incre\u00edbles conciertos a sus seguidores.</p>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/hatsune-miku.jpg\"><img alt=\"Hatsune Miku.\" src=\"../../../../_images/hatsune-miku.jpg\" style=\"width: 320px; height: 240px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Versi\u00f3n animada de Hatsune Miku.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
