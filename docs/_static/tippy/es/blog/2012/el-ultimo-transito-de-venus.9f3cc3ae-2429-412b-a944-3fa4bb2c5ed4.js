selector_to_html = {"a[href=\"#id2\"]": "<figure class=\"align-center\" id=\"id2\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/transito-venus-2012-paso-sol.png\"><img alt=\"Paso de Venus por al frente del Sol durante el tr\u00e1nsito de 2012.\" src=\"../../../../_images/transito-venus-2012-paso-sol.png\" style=\"width: 295px; height: 320px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Paso de Venus por al frente del Sol durante el tr\u00e1nsito de 2012.</span><a class=\"headerlink\" href=\"#id2\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/transito-venus-gota-negra.jpg\"><img alt=\"Efecto de gota negra durante el tr\u00e1nsito de venus de 2004.\" src=\"../../../../_images/transito-venus-gota-negra.jpg\" style=\"width: 320px; height: 184px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Efecto de gota negra durante el tr\u00e1nsito de venus de 2004.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#el-ultimo-transito-de-venus\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">El \u00faltimo tr\u00e1nsito de Venus<a class=\"headerlink\" href=\"#el-ultimo-transito-de-venus\" title=\"Link to this heading\">#</a></h1><p>Retomando el blog despu\u00e9s de cierto tiempo de abandono por diversos\nmotivos, volvemos con las cosas que nos gustan, ciencia, tecnolog\u00eda y\notras curiosidades <em>geeks</em>.</p><p>No es que el mundo se acabe el 21 de diciembre de 2012, pero\ndesafortunadamente nuestras vidas son ef\u00edmeras mientras no conozcamos\nel elixir de la vida eterna y nuestro compa\u00f1ero de viaje c\u00f3smico nos\ndeleita con poca frecuencia cruzando el magnifico disco solar.</p>", "a[href=\"#id3\"]": "<figure class=\"align-center\" id=\"id3\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/transito-venus-2012-visibilidad.png\"><img alt=\"Visibilidad global del tr\u00e1nsito de Venus de 2012.\" src=\"../../../../_images/transito-venus-2012-visibilidad.png\" style=\"width: 320px; height: 184px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Visibilidad global del tr\u00e1nsito de Venus de 2012.</span><a class=\"headerlink\" href=\"#id3\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
