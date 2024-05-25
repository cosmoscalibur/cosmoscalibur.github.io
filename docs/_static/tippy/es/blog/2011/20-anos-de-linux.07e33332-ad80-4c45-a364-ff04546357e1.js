selector_to_html = {"a[href=\"#anos-de-linux\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">20 a\u00f1os de Linux<a class=\"headerlink\" href=\"#anos-de-linux\" title=\"Link to this heading\">#</a></h1><p>Hace 20 a\u00f1os, Linus Torvalds tomo la decisi\u00f3n de compartir su sistema operativo con el mundo. No mucho despu\u00e9s, decidi\u00f3 licenciar este bajo <em>General Public Licence</em> (GPL). Este momento hist\u00f3rico cambio todo en el mundo en la historia de la computaci\u00f3n.</p><p>Hoy, Linux es el proyecto colaborativo mas grande en la historia de la computaci\u00f3n, lo cual significa que el aniversario n\u00famero 20 de Linux es una oportunidad para que la comunidad llegue a unirse en la celebraci\u00f3n de este gran acontecimiento y contribuir a definir como ser\u00e1n los pr\u00f3ximos 20 a\u00f1os de linux.</p>"}
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
