selector_to_html = {"a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/gravity-b-confirmacion-gravitomagnetismo.jpg\"><img alt=\"Esquema sonda Gravity B y las relaciones del gravitomagnetismo.\" src=\"../../../../_images/gravity-b-confirmacion-gravitomagnetismo.jpg\" style=\"width: 320px; height: 204px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Esquema sonda Gravity B y las relaciones del gravitomagnetismo.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#gravitomagnetismo-y-gravity-probe-b\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Gravitomagnetismo y Gravity Probe B<a class=\"headerlink\" href=\"#gravitomagnetismo-y-gravity-probe-b\" title=\"Link to this heading\">#</a></h1><p>Una de las teor\u00edas de mayor impacto, no solo a\nnivel cient\u00edfico sino tambi\u00e9n del \u00absaber popular\u00bb ha sido la teor\u00eda de\nla relatividad de Einstein, que por cierto, su nombre el cu\u00e1l no fue del\nagrado de su autor que consideraba la existencia de los absolutos, fue\nasignado por Max Planck.</p><p>La teor\u00eda de la relatividad parte de reformular\nel car\u00e1cter independiente y absoluto de las entidades del tiempo y el\nespacio, en un nuevo concepto que corresponde al espacio-tiempo.\nRealmente ambos hacen parte de una misma entidad insoluble, creando una\nbase del absoluto ya no sobre el lugar donde suceden los fen\u00f3menos sino\nsobre los efectos de los fen\u00f3menos (sin importar las condiciones del\nobservador, los efectos de un fen\u00f3meno ser\u00e1n los mismos para todos).  Y\nla base para este nuevo absoluto fue la luz, la cual al medir su\nvelocidad era independiente del marco de referencia derrocando la\nanterior hip\u00f3tesis de la existencia del \u00e9ter (un medio fluido de\npeculiares caracter\u00edsticas sobre el cual se desplazar\u00eda la luz).</p>"}
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
