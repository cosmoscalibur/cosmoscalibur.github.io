selector_to_html = {"a[href=\"#aplicacion-de-iot-a-la-cadena-de-suministro\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Aplicaci\u00f3n de IoT a la cadena de suministro<a class=\"headerlink\" href=\"#aplicacion-de-iot-a-la-cadena-de-suministro\" title=\"Link to this heading\">#</a></h1><p>Otra publicaci\u00f3n sobre el curso de transformaci\u00f3n digital. Esta vez, sobre la\naplicaci\u00f3n de <em>IoT</em> (Internet de las Cosas) a la cadena de suministro. Son\nparticipaciones en foros del curso.</p><p>Se debe considerar el importante impacto de la implementaci\u00f3n de IoT en la\ncadena de suministro, lo cual permite seguimiento oportuno a todo el proceso y\ngenerar indicadores para la toma de decisiones. El seguimiento gracias a IoT no\nsolo permite tener indicadores sino la posibilidad de reducir la diferencia de\ntiempo en la consolidaci\u00f3n de la informaci\u00f3n, mejorar la calidad de datos y\ndisminuir la intermediaci\u00f3n o manipulaci\u00f3n de informaci\u00f3n, al crear pasarelas\nde datos directas a los servicios de recepci\u00f3n.</p>", "a[href=\"#\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Aplicaci\u00f3n de IoT a la cadena de suministro<a class=\"headerlink\" href=\"#aplicacion-de-iot-a-la-cadena-de-suministro\" title=\"Link to this heading\">#</a></h1><p>Otra publicaci\u00f3n sobre el curso de transformaci\u00f3n digital. Esta vez, sobre la\naplicaci\u00f3n de <em>IoT</em> (Internet de las Cosas) a la cadena de suministro. Son\nparticipaciones en foros del curso.</p><p>Se debe considerar el importante impacto de la implementaci\u00f3n de IoT en la\ncadena de suministro, lo cual permite seguimiento oportuno a todo el proceso y\ngenerar indicadores para la toma de decisiones. El seguimiento gracias a IoT no\nsolo permite tener indicadores sino la posibilidad de reducir la diferencia de\ntiempo en la consolidaci\u00f3n de la informaci\u00f3n, mejorar la calidad de datos y\ndisminuir la intermediaci\u00f3n o manipulaci\u00f3n de informaci\u00f3n, al crear pasarelas\nde datos directas a los servicios de recepci\u00f3n.</p>"}
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
