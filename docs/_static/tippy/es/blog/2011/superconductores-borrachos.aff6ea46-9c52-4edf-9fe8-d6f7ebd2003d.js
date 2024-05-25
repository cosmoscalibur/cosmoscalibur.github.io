selector_to_html = {"a[href=\"#superconductores-borrachos\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Superconductores borrachos<a class=\"headerlink\" href=\"#superconductores-borrachos\" title=\"Link to this heading\">#</a></h1><p>Como muchos de los descubrimientos de la ciencia, algunos suelen ocurrir por mero accidente, algunos bastante inveros\u00edmiles de car\u00e1cter meramente figurativo y de leyenda urbana para no mas decir que es un golpe de suerte.</p><p>Una de estas historias, es la que ronda al trabajo presentado por el equipo de Yoshihiko Takano del National Institute for Materials Science en Jap\u00f3n. Trabajando en el desarrollo de un cierto tipo de superconductores basados en hierro sumergiendo estos en agua caliente, en una mezcla de agua y etanol.</p>", "a[href=\"#id2\"]": "<aside class=\"footnote brackets\" id=\"id2\" role=\"doc-footnote\">\n<span class=\"label\"><span class=\"fn-bracket\">[</span><a href=\"#id1\" role=\"doc-backlink\">1</a><span class=\"fn-bracket\">]</span></span>\n<p><em>Superconductivity in</em> <span class=\"math notranslate nohighlight\">\\(FeTe_{1-x}S_x\\)</span> <em>induced by alcohol</em>. Deguchi y otros. 4 de febrero de 2011. <a class=\"reference external\" href=\"https://arxiv.org/abs/1008.0666\">arXiv:1008.0666 [cond-mat.supr-con]</a>. <strong>DOI:</strong> 10.1088/0953-2048/24/5/055008.</p>\n</aside>"}
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
