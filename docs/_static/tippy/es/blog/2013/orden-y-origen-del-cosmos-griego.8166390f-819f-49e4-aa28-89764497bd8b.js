selector_to_html = {"a[href=\"#orden-y-origen-del-cosmos-griego\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Orden y origen del cosmos griego<a class=\"headerlink\" href=\"#orden-y-origen-del-cosmos-griego\" title=\"Link to this heading\">#</a></h1><p>Segundo art\u00edculo basado en mi charla de \u00abCosmogon\u00eda y cosmolog\u00eda griega\u00bb\nde astronom\u00eda en el Parque de los Deseos del 14 de mayo de 2013 (el primero\nfue <a class=\"reference internal\" href=\"../cosmogonia-griega/\"><span class=\"doc\">Cosmogon\u00eda griega</span></a>).</p><p>Tales de Mileto, el primer filosofo griego, incorpor\u00f3 las primeras\nnociones no mitol\u00f3gicas a la descripci\u00f3n y explicaci\u00f3n del mundo, he\nintento aclarar el misterio de la sustancia primera, consider\u00e1ndola el\nagua. El mundo para Tales era un disco circular flotando en el oc\u00e9ano.\nAnaximandro (segundo filosofo j\u00f3nico) abandonar\u00eda la visi\u00f3n de Tales y\ndel arj\u00e9, y asignar\u00eda como principio el infinito o lo indefinido. Por\nsimetr\u00eda, la Tierra deber\u00eda ser plana o una forma convexa, y en\nequilibrio con el centro del universo. La naturaleza de los cielos es el\nfuego y es esf\u00e9rico en forma. Los cuerpos del cielo ubicados a\ndiferentes distancias, siendo el sol m\u00e1s distante que la esfera de\nestrellas fijas. Los cuerpos celestes son agujeros que permiten ver el\nfuego del cielo.</p>"}
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
