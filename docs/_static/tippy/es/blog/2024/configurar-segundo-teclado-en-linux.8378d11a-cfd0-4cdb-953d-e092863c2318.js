selector_to_html = {"a[href=\"#configuracion-de-lenguaje\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Configuraci\u00f3n de lenguaje<a class=\"headerlink\" href=\"#configuracion-de-lenguaje\" title=\"Link to this heading\">#</a></h2><p>Ya que sabemos el identificador del teclado, podemos asignarle una configuraci\u00f3n\nespec\u00edfica al teclado. Para este fin, usamos <code class=\"docutils literal notranslate\"><span class=\"pre\">setxkbmap</span></code>, que es la utilidad para\nconfiguraci\u00f3n del teclado.</p><p>El identificador previo, corresponde al argumento de <code class=\"docutils literal notranslate\"><span class=\"pre\">-device</span></code>, y el lenguaje\ndel teclado corresponde al argumento <code class=\"docutils literal notranslate\"><span class=\"pre\">-layout</span></code>. Es necesario que validemos muy\nbien esto, porque para un mismo lenguaje existen variantes (<code class=\"docutils literal notranslate\"><span class=\"pre\">-variant</span></code>).\nEjemplo, en espa\u00f1ol podemos encontrar con variantes como latinoam\u00e9rica, dvorak\ny teclas muertas.</p>", "a[href=\"#configurar-segundo-teclado-en-linux\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Configurar segundo teclado en Linux<a class=\"headerlink\" href=\"#configurar-segundo-teclado-en-linux\" title=\"Link to this heading\">#</a></h1><p>Si tienes un segundo teclado para conectar a tu equipo Linux, pero su distribuci\u00f3n\nde lenguaje es diferente, te explico como configurar aqu\u00ed.</p><p>Resulta que, cuando ingres\u00e9 a mi empleo actual, me entregaron como dotaci\u00f3n un\nequipo con teclado ingl\u00e9s. Y bueno, que problema acostumbrarme a la\nconfiguraci\u00f3n de teclado internacional para poder escribir con tildes o con \u201c\u00f1\u201d.\nAs\u00ed que decid\u00ed comprar un teclado USB.</p>", "a[href=\"#metodo-de-entrada\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">M\u00e9todo de entrada<a class=\"headerlink\" href=\"#metodo-de-entrada\" title=\"Link to this heading\">#</a></h2><p>Necesitamos conocer el m\u00e9todo de entrada asociado, es decir, nuestros\ndispositivos conectados para ingresar informaci\u00f3n, como el teclado,\nel rat\u00f3n o controles.</p><p>Para este fin usamos <code class=\"docutils literal notranslate\"><span class=\"pre\">xinput</span></code>. Es una utilidad para configurar y probar los\nm\u00e9todos de entrada.</p>"}
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
