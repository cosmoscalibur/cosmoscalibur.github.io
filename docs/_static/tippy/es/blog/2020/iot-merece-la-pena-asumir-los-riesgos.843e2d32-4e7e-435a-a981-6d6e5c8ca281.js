selector_to_html = {"a[href=\"#iot-merece-la-pena-asumir-los-riesgos\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">IoT \u00bfMerece la pena asumir los riesgos?<a class=\"headerlink\" href=\"#iot-merece-la-pena-asumir-los-riesgos\" title=\"Link to this heading\">#</a></h1><p>Sigo con algunas publicaciones asociadas a participaciones en foro y ensayos\nque he realizado para el curso de transformaci\u00f3n digital que estoy realizando\npor estas semanas. Esta vez, el tema es sobre si amerita asumir los riesgos\nasociados a la implementaci\u00f3n de tecnolog\u00edas <em>IoT</em> (Internet de las Cosas).</p><p>Se debe tener en cuenta que todo desarrollo siempre implica riesgos, pero estos\nno deben ser barreras para iniciarlos. Es importante afrontarlos de manera\nmetodol\u00f3gica, con la respectiva identificaci\u00f3n de los riesgos al inicio de los\nproyectos y planear las medidas de administraci\u00f3n para estos. Igualmente, se\ndebe evaluar respecto a una regla emp\u00edrica que normalmente nos encontramos, y\nes que a mayor riesgo existe la posibilidad de un mayor retorno.</p>", "a[href=\"#\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">IoT \u00bfMerece la pena asumir los riesgos?<a class=\"headerlink\" href=\"#iot-merece-la-pena-asumir-los-riesgos\" title=\"Link to this heading\">#</a></h1><p>Sigo con algunas publicaciones asociadas a participaciones en foro y ensayos\nque he realizado para el curso de transformaci\u00f3n digital que estoy realizando\npor estas semanas. Esta vez, el tema es sobre si amerita asumir los riesgos\nasociados a la implementaci\u00f3n de tecnolog\u00edas <em>IoT</em> (Internet de las Cosas).</p><p>Se debe tener en cuenta que todo desarrollo siempre implica riesgos, pero estos\nno deben ser barreras para iniciarlos. Es importante afrontarlos de manera\nmetodol\u00f3gica, con la respectiva identificaci\u00f3n de los riesgos al inicio de los\nproyectos y planear las medidas de administraci\u00f3n para estos. Igualmente, se\ndebe evaluar respecto a una regla emp\u00edrica que normalmente nos encontramos, y\nes que a mayor riesgo existe la posibilidad de un mayor retorno.</p>"}
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
