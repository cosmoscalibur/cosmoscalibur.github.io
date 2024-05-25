selector_to_html = {"a[href=\"#el-doble-cumpleanos-de-newton-y-el-calendario-gregoriano\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">El doble cumplea\u00f1os de Newton y el calendario gregoriano<a class=\"headerlink\" href=\"#el-doble-cumpleanos-de-newton-y-el-calendario-gregoriano\" title=\"Link to this heading\">#</a></h1><p>Hoy es una nota de tipo curiosa, ya que algunos recordaran que hace 10\nd\u00edas muchos conmemoramos el cumplea\u00f1os de Sir Isaac Newton, quien\nhab\u00eda nacido el 25 de diciembre de 1642. Sin embargo, hoy 4 de enero\nencontramos como en distintos perfiles sociales, publicaciones y blogs\nvuelven a conmemorar la fecha que recibi\u00f3 a uno de los revolucionarios\nde la f\u00edsica de su tiempo y a quien debemos gran parte de lo que nos\nense\u00f1an en las clases de f\u00edsica de colegio y de primeros semestres de\nuniversidad.</p><p>Esta curiosidad de la doble celebraci\u00f3n se debe al cambio de\ncalendario ocurrido a ra\u00edz de la bula papal de Gregorio XIII <em>Inter\nGravissimas</em>, que revoco el calendario juliano usado desde la\ninstauraci\u00f3n por Julio Cesar, y promovi\u00f3 el uso del calendario\ngregoriano. Este cambio de calendario buscaba ajustar el desfase del\ncalendario del calendario juliano respecto a la fecha de celebraci\u00f3n\nde la pascua, la cual desde el concilio de Nicea en el a\u00f1o 325 se fijo\ncomo el domingo siguiente al plenilunio (luna llena) posterior del\nequinoccio de primavera. En ese momento, el equinoccio de\nprimavera ocurri\u00f3 el 21 de marzo, pero con el paso de algo m\u00e1s de un\nmilenio, dicha fecha se hab\u00eda acumulado un atraso de 10 (ocurr\u00eda ya el\n11 de marzo).</p>"}
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
