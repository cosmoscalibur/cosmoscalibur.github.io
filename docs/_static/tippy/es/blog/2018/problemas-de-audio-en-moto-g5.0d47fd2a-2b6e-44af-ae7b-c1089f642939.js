selector_to_html = {"a[href=\"#problemas-de-audio-en-moto-g5\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Problemas de audio en Moto G5<a class=\"headerlink\" href=\"#problemas-de-audio-en-moto-g5\" title=\"Link to this heading\">#</a></h1><p>Reci\u00e9n cambi\u00e9 mi celular Moto G3 por un Moto G5 y vaya susto el que me llev\u00e9\ninicialmente. La verdad, como el cambio fue m\u00e1s bien un asunto de af\u00e1n no\nrevis\u00e9 foros previamente\n(<a class=\"reference internal\" href=\"../comprando-celular-para-personalizar/\"><span class=\"doc\">ver recomendaciones a la hora de comprar</span></a>)\nsobre los problemas y me confi\u00e9 de los conocidos que tienen este celular y que\nnunca les he escuchado de problemas.</p><p>El susto comenz\u00f3 con la primera llamada (cuando lo compr\u00e9 no se hizo prueba de\nllamada) y la sorpresa de encontrarme sin audio. Hice dos intentos adicionales\npensando que pod\u00eda ser alg\u00fan problema de se\u00f1al pero persist\u00eda hasta que algo\nse escucho cuando iba a cortar la llamada. Nuevamente prob\u00e9, y el audio\nempezaba 5 segundos despu\u00e9s de conectarse la llamada.</p>", "a[href=\"#solucion\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Soluci\u00f3n<a class=\"headerlink\" href=\"#solucion\" title=\"Link to this heading\">#</a></h2><p>Bueno, sabiendo que la soluci\u00f3n se encuentra en internet y no es dif\u00edcil\nencontrarla, decid\u00ed publicarla porque no siempre quien la necesita sabe ingl\u00e9s\nas\u00ed que esta es una forma de contribuir (al igual que las publicaciones de\nciencia) y bueno, a veces puedo dar detalles adicionales.</p><p>Necesitamos entrar a <cite>Configuraci\u00f3n</cite> y en la secci\u00f3n de \u00abConexiones\ninal\u00e1mbricas y redes\u00bb seleccionamos <cite>\u2026 M\u00e1s</cite>. Ahora nos dirigimos a\n<cite>Redes m\u00f3viles</cite> y deshabilitamos la opci\u00f3n <cite>Modo 4G LTE mejorado</cite>. Aunque nos\nindica que se recomienda usarlo ya sabemos por experiencia que es el origen de\nnuestro problema de audio.</p>", "a[href=\"#problema-y-origen\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Problema y origen<a class=\"headerlink\" href=\"#problema-y-origen\" title=\"Link to this heading\">#</a></h2><p>Del mes de mayo de 2017 (3 meses despu\u00e9s de la fecha de lanzamiento) se\nobservan en esta b\u00fasqueda los primeros reportes de problemas de audio como\nausencia de sonido durante el inicio de las llamadas, mala calidad del audio e\nincluso la apreciaci\u00f3n de voz digitalizada. En algunos foros se encuentra\nreportado como problemas espec\u00edficos de algunos operadores m\u00f3viles pero\nrealmente no es as\u00ed, y ya entenderemos por que.</p><p>La raz\u00f3n de este error es que por defecto el Moto G5 viene habilitado con una\nopci\u00f3n de mejora de audio a trav\u00e9s de recursos LTE pero bueno, \u00bfes una mejora?</p>"}
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
