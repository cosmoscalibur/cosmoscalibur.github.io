selector_to_html = {"a[href=\"#pensando-en-el-grafeno\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Pensando en el grafeno<a class=\"headerlink\" href=\"#pensando-en-el-grafeno\" title=\"Link to this heading\">#</a></h1><p>Aunque este material fue noticia ya hace un rato, vengo a pensar ahora en el porque sera mi tema de trabajo de grado.\nEste material fue noticia ya que por estudios de este material fue concedido el premio nobel de f\u00edsica a 2 f\u00edsicos rusos que trabajan en la Universidad de Manchester.</p><p>Este material tiene muchas caracter\u00edsticas muy peculiares, que atraen el inter\u00e9s no solo de la comunidad cient\u00edfica sino tambi\u00e9n ingenieril/industrial. Desde la industria resulta bastante interesante que sea un material extremadamente resistente y al mismo tiempo muy liviano (son capas formadas por estructuras de carbono hexagonal, estructuralmente con gran similaridad al grafito, de lo que esta hecho la mina de los lapices).</p>"}
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
