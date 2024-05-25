selector_to_html = {"a[href=\"#filtraciones-de-datos-en-el-siglo-xxi\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Filtraciones de datos en el siglo XXI<a class=\"headerlink\" href=\"#filtraciones-de-datos-en-el-siglo-xxi\" title=\"Link to this heading\">#</a></h1><p>Otra publicaci\u00f3n sobre el curso de transformaci\u00f3n digital. Esta vez, sobre la\nprecauciones respecto a las filtraciones de datos. Son participaciones en foros\ndel curso.</p><p>Respecto a la seguridad de los datos de los clientes, es necesario dejar claro\nque esto debe ser una prioridad para toda empresa. Y esto debe reforzarse con\nlas medidas acorde al tipo de informaci\u00f3n que pueda exponerse para asegurar la\ntranquilidad de los clientes.</p>", "a[href=\"#\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Filtraciones de datos en el siglo XXI<a class=\"headerlink\" href=\"#filtraciones-de-datos-en-el-siglo-xxi\" title=\"Link to this heading\">#</a></h1><p>Otra publicaci\u00f3n sobre el curso de transformaci\u00f3n digital. Esta vez, sobre la\nprecauciones respecto a las filtraciones de datos. Son participaciones en foros\ndel curso.</p><p>Respecto a la seguridad de los datos de los clientes, es necesario dejar claro\nque esto debe ser una prioridad para toda empresa. Y esto debe reforzarse con\nlas medidas acorde al tipo de informaci\u00f3n que pueda exponerse para asegurar la\ntranquilidad de los clientes.</p>"}
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
