selector_to_html = {"a[href=\"#asimov-en-la-ciencia\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Asimov en la ciencia<a class=\"headerlink\" href=\"#asimov-en-la-ciencia\" title=\"Link to this heading\">#</a></h1><p>Isaac Asimov si bien por el com\u00fan de la gente es conocido solo como un\nescritor de ciencia ficci\u00f3n y misterio (esta ultima tem\u00e1tica menos\nconocida por el com\u00fan) y como un gran divulgador de la ciencia, tambi\u00e9n\nfue un cient\u00edfico.</p><p>Isaac Asimov, o en ruso <em>Isaak Yudovich\nOzimov</em>, naci\u00f3 el 2 de enero de 1920 en Petrovichi, Rusia. Asimov obtuv\u00f3\nt\u00edtulo de pregrado, maestr\u00eda y doctorado en qu\u00edmica de la <em>Columbia\nUniversity</em> en la ciudad de Nueva York. Recordando un poco,\nlos t\u00edtulos a nivel de posgrado te confieren las habilidades de\ninvestigador (o lo popularmente conocido como cient\u00edfico).</p>"}
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
