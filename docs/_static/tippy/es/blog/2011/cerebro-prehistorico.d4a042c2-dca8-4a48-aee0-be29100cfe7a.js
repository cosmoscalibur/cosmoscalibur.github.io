selector_to_html = {"a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/tomografia-computacional-cerebro.jpg\"><img alt=\"../../../../_images/tomografia-computacional-cerebro.jpg\" src=\"../../../../_images/tomografia-computacional-cerebro.jpg\" style=\"width: 320px; height: 214px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Tomograf\u00eda computacional del cr\u00e1neo hallado.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#cerebro-prehistorico\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Cerebro prehist\u00f3rico<a class=\"headerlink\" href=\"#cerebro-prehistorico\" title=\"Link to this heading\">#</a></h1><p>El cerebro, uno de los \u00f3rganos tal vez de mayor importancia no solo por\nsus funciones sino por el inter\u00e9s por su compleja estructura, es\nun \u00f3rgano de tejido bastante delicado. Sin embargo, hasta nuestros d\u00edas\nse conocen algunos casos de cerebros bien preservados desde tiempos\nremotos.</p><p>El caso mas reciente, y tal vez considerado el mejor conservado,\ncorresponde a un cerebro aun en su cr\u00e1neo, de alg\u00fan desafortunado\npersonaje que perdi\u00f3 literalmente su cabeza, pero no su cerebro.\nEl cr\u00e1neo en cuesti\u00f3n fue hallado en un pozo libre de ox\u00edgeno en\nHeslington Yorkshire, en una zona donde se realizo una excavaci\u00f3n con\nfines arqueol\u00f3gicos previ\u00f3 a iniciar una construcci\u00f3n. El caso data de\n2008, pero su bum en la red (encontraran muchas notas de este a\u00f1o en\ninternet, que no refieren a la fecha del hallazgo) se debe a su reciente\npublicaci\u00f3n en Journal of Archaeologist Science (all\u00ed encontraran\nreferencia a otros hallazgos realizados desde 1960 de \u00f3rganos blandos\nconservados).</p>", "a[href=\"#id2\"]": "<figure class=\"align-center\" id=\"id2\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/porcion-cerebro.jpg\"><img alt=\"../../../../_images/porcion-cerebro.jpg\" src=\"../../../../_images/porcion-cerebro.jpg\" style=\"width: 320px; height: 249px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Porci\u00f3n del cerebro recuperado de aproximadamente 2600 a\u00f1os de antig\u00fcedad.</span><a class=\"headerlink\" href=\"#id2\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
