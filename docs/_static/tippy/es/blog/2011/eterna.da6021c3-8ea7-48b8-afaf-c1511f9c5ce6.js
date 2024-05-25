selector_to_html = {"a[href=\"#eterna\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">EteRNA<a class=\"headerlink\" href=\"#eterna\" title=\"Link to this heading\">#</a></h1><p>Ya \u00faltimamente nos encontramos con una gran cantidad de actividades, servicios\ny contenidos en internet. Ya somos parte de la red, as\u00ed no estemos en su\ninterior como sucede en la pel\u00edcula TRON, pero si nos absorbe una parte\nconsiderable de nuestro tiempo.</p><p>Bajo este, no esta dem\u00e1s que ideemos estrategias para pasar el rato en \u00e9l, de\nforma divertida y al mismo tiempo haciendo algo provechoso (aprendiendo). A\nprincipios de esta semana me encontr\u00e9 con EteRNA <a class=\"footnote-reference brackets\" href=\"#id2\" id=\"id1\" role=\"doc-noteref\"><span class=\"fn-bracket\">[</span>1<span class=\"fn-bracket\">]</span></a>, un juego en l\u00ednea\nideado por investigadores Carnegie Mellon University y Stanford University.</p>", "a[href=\"#id2\"]": "<aside class=\"footnote brackets\" id=\"id2\" role=\"doc-footnote\">\n<span class=\"label\"><span class=\"fn-bracket\">[</span><a href=\"#id1\" role=\"doc-backlink\">1</a><span class=\"fn-bracket\">]</span></span>\n<p><a class=\"reference external\" href=\"http://www.eternagame.org/web/\">EteRNA Game web</a>.</p>\n</aside>", "a[href=\"#id3\"]": "<figure class=\"align-center\" id=\"id3\">\n<img alt=\"Logo del juego Eterna.\" src=\"../../../../_images/eterna-juego-logo.png\"/>\n<figcaption>\n<p><span class=\"caption-text\">Juego Eterna para dise\u00f1o de ARN.</span><a class=\"headerlink\" href=\"#id3\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
