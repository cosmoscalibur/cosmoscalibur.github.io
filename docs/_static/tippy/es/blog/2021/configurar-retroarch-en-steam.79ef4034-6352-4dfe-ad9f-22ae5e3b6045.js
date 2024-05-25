selector_to_html = {"a[href=\"#configurar-retroarch-en-steam\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Configurar RetroArch en Steam<a class=\"headerlink\" href=\"#configurar-retroarch-en-steam\" title=\"Link to this heading\">#</a></h1><p><a class=\"reference external\" href=\"https://www.retroarch.com/\">RetroArch</a> es un agregador de emuladores y\nvideojuegos para estos, multiplataforma\n(<a class=\"reference external\" href=\"https://www.retroarch.com/?page=platforms\">descargas de plataformas soportadas</a>)\ny de c\u00f3digo abierto. Es posible instalar RetroArch de forma directa en el\nsistema operativo o a trav\u00e9s de Steam, teniendo este algunas ventajas\nadicionales de unir las caracter\u015bticas de Steam Play y el almacenamiento de\nestado en Steam Cloud. Adicional a esto, sin duda es una ventaja para el\ndesarrollo de la comunidad alrededor de este medio adicional de distribuci\u00f3n.</p><p>Si prefieres la versi\u00f3n en video, puedes continuar en Youtube.</p>"}
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
