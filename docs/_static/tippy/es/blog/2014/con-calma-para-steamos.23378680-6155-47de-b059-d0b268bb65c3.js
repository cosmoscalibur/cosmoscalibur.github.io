selector_to_html = {"a[href=\"#con-calma-para-steamos\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Con calma para SteamOS<a class=\"headerlink\" href=\"#con-calma-para-steamos\" title=\"Link to this heading\">#</a></h1><p>Bueno, es un poco raro que sin escribir hace mucho, lo primero que\nescriba sea del mundo linux que del mundo de la ciencia y\nparticularmente de la f\u00edsica que es mi especialidad. Pero resulta que a\nveces es un poco m\u00e1s f\u00e1cil escribir sobre cosas que no toque justificar\ntanto.</p><p>Soy usuario Linux desde 2009, usando la distro Ubuntu con escritorio\ngnome. Pero hace alg\u00fan tiempo empece a comprar juegos en <a class=\"reference external\" href=\"https://www.humblebundle.com/\">Humble\nBundle</a>. Muy buenos titulos,\nexcelentes gr\u00e1ficos y en otros excelentes historias, multiplataforma,\nmejor dicho un para\u00edso <em>gamer</em> y al mejor precio (cr\u00e9anme! m\u00e1ximo he\npagado 15 dolares por 10 t\u00edtulos en varias plataformas y sus audios).\nParte de estos t\u00edtulos son de la corporaci\u00f3n\n<a class=\"reference external\" href=\"http://www.valvesoftware.com/\">Valve</a>, desarrolladora de la\nplataforma de videojuegos <a class=\"reference external\" href=\"http://store.steampowered.com/\">Steam</a>.</p>"}
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
