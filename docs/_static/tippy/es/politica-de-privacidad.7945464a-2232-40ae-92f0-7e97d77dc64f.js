selector_to_html = {"a[href=\"#informacion-recogida-y-uso\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Informaci\u00f3n recogida y uso<a class=\"headerlink\" href=\"#informacion-recogida-y-uso\" title=\"Link to this heading\">#</a></h2><p>Cosmoscalibur.com recoge a trav\u00e9s de rutinas de javascript de terceros\ninformaci\u00f3n anonimizada para fines de anal\u00edtica del tr\u00e1fico web del sitio.</p><p>Esto incluye el uso de cookies de terceros, correspondientes a Facebook y\nGoogle.</p>", "a[href=\"#politica-de-privacidad\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Pol\u00edtica de privacidad<a class=\"headerlink\" href=\"#politica-de-privacidad\" title=\"Link to this heading\">#</a></h1><p>La presente pol\u00edtica de privacidad establece los t\u00e9rminos en que\ncosmoscalibur.com usa y protege la informaci\u00f3n que es proporcionada por los\nusuarios al momento de utilizar el sitio web.</p><p>Esta pol\u00edtica de privacidad puede cambiar en el tiempo o ser actualizada, por\nlo cual se recomienda revisar continuamente esta p\u00e1gina.</p>", "a[href=\"#enlaces-a-terceros\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Enlaces a terceros<a class=\"headerlink\" href=\"#enlaces-a-terceros\" title=\"Link to this heading\">#</a></h2><p>Este sitio web pudiera contener enlaces a otros sitios que pudieran ser de su\ninter\u00e9s. Una vez que usted de clic en estos enlaces y abandone\ncosmoscalibur.com, ya no tenemos control sobre al sitio al que es redirigido y\npor lo tanto cosmoscalibur.com no es responsable de los t\u00e9rminos o privacidad\nni de la protecci\u00f3n de sus datos en esos otros sitios terceros. Dichos sitios\nest\u00e1n sujetos a sus propias pol\u00edticas de privacidad por lo cual es recomendable\nque los consulte para confirmar que usted est\u00e1 de acuerdo con estas.</p>"}
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
