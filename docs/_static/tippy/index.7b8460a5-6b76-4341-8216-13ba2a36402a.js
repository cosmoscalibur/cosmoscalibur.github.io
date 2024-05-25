selector_to_html = {"a[href=\"#blog-cosmoscalibur\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Blog Cosmoscalibur<a class=\"headerlink\" href=\"#blog-cosmoscalibur\" title=\"Link to this heading\">#</a></h1><p>Bienvenidos a mi blog, Cosmoscalibur.</p><p>Este es un espacio para compartir sobre distintos temas, no solo\ncontenido divulgativo. Principalmente, hay publicaciones de ciencia,\ntecnolog\u00eda y poemas propios, pero con el tiempo esto puede cambiar\nsiguiendo un patr\u00f3n de elementos curiosos que quiera compartir o notas\npersonales que me sirven de recordatorio.</p>"}
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
