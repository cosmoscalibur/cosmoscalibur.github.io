selector_to_html = {"a[href=\"#posibilidad-de-agua-salada-en-marte\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Posibilidad de Agua Salada en Marte<a class=\"headerlink\" href=\"#posibilidad-de-agua-salada-en-marte\" title=\"Link to this heading\">#</a></h1><p>Despu\u00e9s de un largo periodo de ausencia en el blog, vuelvo por estos\nlados a seguir publicando sobre los temas de la ciencia que tanto nos\napasiona aprovechando la imagen que expuse en la sesiones del <a class=\"reference external\" href=\"http://www.facebook.com/groups/376416784920/\">Club\nOri\u00f3n del Parque\nExplora</a>.</p><p>En el mes de Mayo, la sonda <em>Mars Reconnaissance Orbiter</em> (MRO) tomo una\nserie de im\u00e1genes sobre el sector del Cr\u00e1ter Newton en el hemisferio sur\ndel planeta Marte que tras un an\u00e1lisis de im\u00e1genes para la composici\u00f3n\ndel sector a partir de los m\u00faltiples sectores obtenidos en el proceso de\nmapeo de la superficie marciana (misi\u00f3n principal del MRO m\u00faltiples) y\nla detecci\u00f3n de posibles cuerpos como rocas, dunas o sedimentos que\nhallan cambiado de posici\u00f3n, se encuentran con algo realmente\nsorprendente.</p>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/crater-newton-marte.png\"><img alt=\"Ubicaci\u00f3n del cr\u00e1ter Newton en Marte con Google Mars.\" src=\"../../../../_images/crater-newton-marte.png\" style=\"width: 320px; height: 171px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Ubicaci\u00f3n del cr\u00e1ter Newton en Marte con\n<a class=\"reference external\" href=\"https://www.google.com/mars/#lat=-8.997377&amp;lon=-101.234765&amp;q=newton\">Google Mars</a>.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
