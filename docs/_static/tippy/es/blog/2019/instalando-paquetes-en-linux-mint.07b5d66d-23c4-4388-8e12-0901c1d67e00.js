selector_to_html = {"a[href=\"#flatpak\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Flatpak<a class=\"headerlink\" href=\"#flatpak\" title=\"Link to this heading\">#</a></h3><p>El caso de flatpak no es muy c\u00f3modo, tiene cierta centralizaci\u00f3n como snap,\npero con fines de indexaci\u00f3n. Un desarrollador puede crear su propio\nrepositorio flatpak. Y al igual que AppImage, no requiere permisos de\nadministrador.</p><p>En Linux Mint viene preconfigurado a partir de la versi\u00f3n 18.3, pero si usas\nUbuntu necesitas instalarlo. Desde la 18.10 se encuentra en los repositorios\noficiales.</p>", "a[href=\"#referencias\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Referencias<a class=\"headerlink\" href=\"#referencias\" title=\"Link to this heading\">#</a></h2>", "a[href=\"#instalando-paquetes-en-linux-mint\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Instalando paquetes en Linux (Mint)<a class=\"headerlink\" href=\"#instalando-paquetes-en-linux-mint\" title=\"Link to this heading\">#</a></h1><p>En Linux ahora tenemos muchas m\u00e1s opciones para instalar nuestros programas\nfavoritos y de uso diario, seg\u00fan los intereses personales en reducir espacio\nen disco, aumentar estabilidad, mejorar seguridad, disponer siempre de la\n\u00faltima versi\u00f3n, tener muy buena integraci\u00f3n con el sistema operativo o no\nrequerir permisos de administrador. Algunas de las estrategias, incluso\nfacilitan que el mismo mecanismo podemos usarlo en m\u00e1s de una distribuci\u00f3n\nLinux y as\u00ed disponer de una transici\u00f3n m\u00e1s simple.</p><p>Este art\u00edculo es algo superficial sobre cada gestor, pero m\u00e1s adelante\npublicar\u00e9 art\u00edculos dedicados a cada uno de ellos con el fin de contarles m\u00e1s\nopciones y trucos.</p>", "a[href=\"#rutinas-de-instalacion\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Rutinas de instalaci\u00f3n<a class=\"headerlink\" href=\"#rutinas-de-instalacion\" title=\"Link to this heading\">#</a></h3><p>En ocasiones encontraremos archivos <code class=\"code docutils literal notranslate\"><span class=\"pre\">.run</span></code> o <code class=\"code docutils literal notranslate\"><span class=\"pre\">.sh</span></code> que asisten la\ninstalaci\u00f3n, descargando componentes o codificando los distintos archivos en\nun solo archivo.</p><p>Para este caso, es necesario conferir permiso de ejecuci\u00f3n al archivo y\nproceder a ejecutarlo. Este procedimiento, es el mismo expuesto en las\n<a class=\"reference external\" href=\"#appimagecode\">primeras dos l\u00edneas de AppImage</a>.</p>", "a[href=\"#snap\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Snap<a class=\"headerlink\" href=\"#snap\" title=\"Link to this heading\">#</a></h3><p>Los snap son el mecanismo de instalaci\u00f3n promovido por Canonical\n(desarrolladores de Ubuntu). Sigue siendo un mecanismo centralizado, que\nrequiere aprobaci\u00f3n de Canonical para ser admitido el paquete y requiere ser\nadministrador para la instalaci\u00f3n.</p><p>En Ubuntu viene preinstalado pero en Linux Mint es necesario instalarlo.</p>", "a[href=\"#compilacion-y-binarios\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Compilaci\u00f3n y binarios<a class=\"headerlink\" href=\"#compilacion-y-binarios\" title=\"Link to this heading\">#</a></h3><p>Estas opciones, no son parte de la historia. La compilaci\u00f3n sigue siendo\nfundamental para la optimizaci\u00f3n de c\u00f3digo cr\u00edtico o de alto rendimiento\ncomo es necesario en la computaci\u00f3n cient\u00edfica. La compilaci\u00f3n saca provecho de\nla arquitectura del procesador usado.</p><p>En este caso, ser\u00e1 t\u00edpico el uso de <code class=\"code docutils literal notranslate\"><span class=\"pre\">configure</span></code> y <code class=\"code docutils literal notranslate\"><span class=\"pre\">make</span></code>. Para m\u00e1s\ninformaci\u00f3n, es necesario leer el archivo <code class=\"code docutils literal notranslate\"><span class=\"pre\">README</span></code> que deber\u00edas\nencontrar, el cual explicar\u00e1 el detalle del proceso de instalaci\u00f3n.</p>", "a[href=\"#gestor-de-la-distribucion\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Gestor de la distribuci\u00f3n<a class=\"headerlink\" href=\"#gestor-de-la-distribucion\" title=\"Link to this heading\">#</a></h3><p>La mayor parte de distribuciones Linux disponen de gestores de paquetes de\n<em>software</em>, que son herramientas para la b\u00fasqueda, descarga, instalaci\u00f3n y\nconfiguraci\u00f3n de estos. Los gestores se conectan a repositorios de paquetes\noficiales que son mantenidos por los desarrollados de la distribuci\u00f3n,\nasegurando que cumplan con est\u00e1ndares m\u00ednimos de compatibilidad y estabilidad.</p><p>Tambi\u00e9n, algunos gestores pueden conectar a repositorios mantenidos por la\ncomunidad, dando la opci\u00f3n de extender el <em>software</em> disponible para\ninstalaci\u00f3n por los usuarios de una manera simple, pero a riesgo de\ninestabilidad o conflictos por la interacci\u00f3n con paquetes de los repositorios\noficiales (no es general, pero suele ocurrir). Estos repositorios de comunidad\nlos recomiendo como \u00faltima opci\u00f3n.</p>", "a[href=\"#appimage\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">AppImage<a class=\"headerlink\" href=\"#appimage\" title=\"Link to this heading\">#</a></h3><p>Me parece la mejor de las opciones entre las nuevas estrategias. Permite la\nejecuci\u00f3n inmediata del programa (no requiere instalaci\u00f3n), gestiona\nactualizaci\u00f3n y no es necesario permisos de administrador al no requerir\ninstalar. En teor\u00eda, ejecuta en cualquier distribuci\u00f3n Linux moderna.</p><p>Como el archivo ejecuta directamente, se pueden tener m\u00faltiples versiones del\nmismo programa. Esto, es por el aislamiento que posee, es un tipo de\ncontenedor, tal como lo son las opciones de snap y flatpak, lo cual tambi\u00e9n\nevita conflictos en el sistema (programas que puedan requerir la misma\ndependencia pero en versiones diferentes, la dependencia no pueda gestionar\nm\u00faltiples instancias o exponga una brecha de seguridad).</p>", "a[href=\"#appimagecode\"]": "<p id=\"appimagecode\">Descargamos el <a class=\"reference external\" href=\"https://stellarium.org/\">AppImage de Stellarium</a> del sitio\noficial del software (el segundo ping\u00fcino).</p>", "a[href=\"#programas-generales\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Programas generales<a class=\"headerlink\" href=\"#programas-generales\" title=\"Link to this heading\">#</a></h2><p>Aunque no es una clasificaci\u00f3n estricta, es la forma que veo para hablar de\nestos paquetes de <em>software</em>. Son paquetes de uso general, lo suficiente para\nser de inter\u00e9s para disponer a trav\u00e9s de medios de distribuci\u00f3n para p\u00fablico\ngeneral. En ocasiones, esto puede incluir paquetes de uso cient\u00edfico o propio\nde desarrollo, o de alguna disciplina particular.</p>"}
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
