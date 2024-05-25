selector_to_html = {"a[href=\"#nuestra-nariz-mas-vieja-que-los-pies\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Nuestra nariz m\u00e1s vieja que los pies<a class=\"headerlink\" href=\"#nuestra-nariz-mas-vieja-que-los-pies\" title=\"Link to this heading\">#</a></h1><p>La relatividad de Einstein abri\u00f3 un nuevo cap\u00edtulo en la f\u00edsica desde sus primeros apuntes en un tratado de la electrodin\u00e1mica de la luz. Desde la relatividad especial plantea ya un punto que separa rotundamente la nueva f\u00edsica a la f\u00edsica tradicional de Newton, y es la concepci\u00f3n no absoluta del espacio y el tiempo.</p><p>Ya en la relatividad especial encontramos que a mayor velocidad el tiempo nos transcurre mas lentamente que si estuvi\u00e9semos en reposo, as\u00ed dos gemelos, uno astronauta y otro un civil, el astronauta seria menor que su hermano (claro esta, por nanosegundos). Pero con la relatividad general, la exposici\u00f3n a campos gravitacionales produce el mismo efecto. A mayor campo gravitacional, el tiempo avanza mas lentamente.</p>"}
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
