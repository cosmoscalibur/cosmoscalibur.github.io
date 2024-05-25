selector_to_html = {"a[href=\"#santa-cuantico\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Santa cu\u00e1ntico<a class=\"headerlink\" href=\"#santa-cuantico\" title=\"Link to this heading\">#</a></h1><p>Lo mejor de todo cuando crecemos es no olvidar algo fundamental, que tambi\u00e9n\nfuimos ni\u00f1os alguna vez. Tal vez pienso esto ahora porque algunas veces sin\ndarnos de cuenta podemos destruir las ilusiones que los ni\u00f1os tejen alrededor\nde historias fant\u00e1sticas, que son el alimento para su capacidad creativa, y\nnosotros por ser mayores y \u00absaber\u00bb como son las cosas derribamos ese m\u00e1gico\nmundo con dos palabras \u00abNO EXISTE\u00bb.</p><p>Pero, de verdad no existen estos mundos y personajes de la imaginaci\u00f3n de\nnuestros ni\u00f1os\u2026 la respuesta es \u00abNo lo sabemos. Que no los hallamos visto, no\nquiere decir que no existan.\u00bb Y la f\u00edsica nos puede ayudar un poco con esto.</p>"}
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
