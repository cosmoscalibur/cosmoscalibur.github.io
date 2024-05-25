selector_to_html = {"a[href=\"#la-flecha-temporal\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">La flecha temporal<a class=\"headerlink\" href=\"#la-flecha-temporal\" title=\"Link to this heading\">#</a></h1><p>La flecha temporal es la designaci\u00f3n al flujo irreversible del tiempo,\nla representaci\u00f3n de la asimetr\u00eda del tiempo. Lo que se hizo, hecho\nesta y no hay vuelta atr\u00e1s. Solo podemos realizar acciones que\namortig\u00fcen los efectos producidos por el acontecimiento mas nunca\ncambiarlo o evitar haberlo hecho, o al menos por ahora a cuerpos\nmacrosc\u00f3picos como nosotros nos es imposible hacerlo.</p><p>Por esto pensaba yo, tambi\u00e9n que en ese transcurrir inexorable del\ntiempo, debemos preocuparnos por dejar algo trazado en el tiempo, en la\nhistoria, que no sea una simple flecha volando en el espacio vaci\u00f3 sin\nning\u00fan mensaje.</p>"}
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
