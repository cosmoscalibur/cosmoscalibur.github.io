selector_to_html = {"a[href=\"#ano-internacional-de-la-quimica\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">2011: A\u00f1o Internacional de la Qu\u00edmica<a class=\"headerlink\" href=\"#ano-internacional-de-la-quimica\" title=\"Link to this heading\">#</a></h1><p>En 2008, Naciones Unidas declaro que el a\u00f1o 2011 ser\u00eda reconocido como\nel A\u00f1o Internacional de la Qu\u00edmica (IYC 2011), conmemorando los logros\nalcanzados en la qu\u00edmica, y sus contribuci\u00f3n a la humanidad.</p><p>Diferentes actividades para este a\u00f1o han sido planeadas, coordinadas por\nla IUPAC, UNESCO y las distintas sociedades nacionales de qu\u00edmica y\nfederaciones. El lema del IYC2011 es \u00abChemistry - our life, our future\u00bb /\n\u00abQu\u00edmica, nuestra vida, nuestro futuro\u00bb.</p>"}
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
