selector_to_html = {"a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/piezoelectrico-esquema-voltaje.gif\"><img alt=\"Esquema de piezoel\u00e9ctrico.\" src=\"../../../../_images/piezoelectrico-esquema-voltaje.gif\" style=\"width: 200px; height: 200px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">La deformaci\u00f3n del piezoel\u00e9ctrico produce una diferencia de potencial (voltaje).</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#energia-alternativa-para-dispositivos-moviles\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Energ\u00eda alternativa para dispositivos m\u00f3viles<a class=\"headerlink\" href=\"#energia-alternativa-para-dispositivos-moviles\" title=\"Link to this heading\">#</a></h1><p>Las fuentes de energ\u00eda son parte vital de los sistemas que actualmente\nnos rodean\u2026 que si no la hay, bueno, desde las grandes estructuras\nhechas por hombre hasta las complejas formas de vida se degradar\u00edan,\ndejar\u00edan de funcionar y simplemente sucumben.</p><p>Pero particularmente nos interesa la energ\u00eda para nuestros dise\u00f1os, la\n\u00abvida artificial\u00bb, los sistemas el\u00e9ctricos y electr\u00f3nicos. A diario\ncargamos (tanto de portar como de suministrar energ\u00eda) toda clase de\ndispositivos m\u00f3viles, pero es algo que bajo circunstancias de una vida\nde total movilidad tal vez pueda caer en algo incluso olvidemos\ny despu\u00e9s lamentamos llevar una simple pantalla negra.</p>"}
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
