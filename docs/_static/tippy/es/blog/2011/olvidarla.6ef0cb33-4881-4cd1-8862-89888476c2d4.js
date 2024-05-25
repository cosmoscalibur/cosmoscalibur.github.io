selector_to_html = {"a[href=\"#olvidarla\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Olvidarla<a class=\"headerlink\" href=\"#olvidarla\" title=\"Link to this heading\">#</a></h1><p>De las tit\u00e1nicas fuerzas que esculpieron su imagen en la solida roca\ns\u00fabita e inesperadamente, solo espero que tambi\u00e9n se encarguen de su\nr\u00e1pida y fugaz erosi\u00f3n y no quede rastro alguno de su monumento en las\ntierras del valle de mis sue\u00f1os, as\u00ed de esto quede un muro de lamentos\nque pronto cubrir\u00e1 un volumen de agua salada.</p><p>De mi en un futuro, espero ser la des\u00e9rtica y fr\u00eda estepa siberiana,\ncon sus lagos glaciales por doquier y de frialdad inigualable, y que\nla luz de sol no toque. Vivir en la oscuridad invernal y estar\nunicamente bajo la luz estelar podr\u00eda ser mejor.</p>"}
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
