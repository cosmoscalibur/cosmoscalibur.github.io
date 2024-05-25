selector_to_html = {"a[href=\"#referencias\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Referencias<a class=\"headerlink\" href=\"#referencias\" title=\"Link to this heading\">#</a></h2>", "a[href=\"#instalar-paquetes-snap-en-linux-mint-20\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Instalar paquetes snap en Linux Mint 20<a class=\"headerlink\" href=\"#instalar-paquetes-snap-en-linux-mint-20\" title=\"Link to this heading\">#</a></h1><p>\u00bfYa tienes Linux Mint 20 y deseas\n<a class=\"reference internal\" href=\"../../2019/instalando-paquetes-en-linux-mint/#instalando-paquetes-en-linux-mint-snap\"><span class=\"std std-ref\">instalar paquetes Snap</span></a>? Mint ha\ndecidido deshabilitar la instalaci\u00f3n de Snap por defecto y es necesario cambiar\nla configuraci\u00f3n de apt para poderlo hacer.</p><p>Si prefieres la versi\u00f3n en video:</p>", "a[href=\"#el-problema\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">El problema<a class=\"headerlink\" href=\"#el-problema\" title=\"Link to this heading\">#</a></h2><p>Si ya cuentas con Linux Mint 20 observar\u00e1s que al intentar instalar el paquete\n<code class=\"code docutils literal notranslate\"><span class=\"pre\">snapd</span></code> (el gestor snap), nos llevaremos la sorpresa de no poderlo\ninstalar. Encontraremos un mensaje como el siguiente:</p>", "a[href=\"#la-solucion\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">La soluci\u00f3n<a class=\"headerlink\" href=\"#la-solucion\" title=\"Link to this heading\">#</a></h2><p>Para solventar este problema, basta con eliminar o comentar las l\u00edneas de un\narchivo: <code class=\"code docutils literal notranslate\"><span class=\"pre\">/etc/apt/preferences.d/nosnap.pref</span></code>. En mi caso, no veo raz\u00f3n\nde mantenerlo, as\u00ed que procedo a eliminarlo y posteriormente a instalar el\ngestor de snaps. Si te sientes m\u00e1s c\u00f3modo, puedes comentar las l\u00edneas y una vez\ninstalado el gestor volver a descomentarlas <a class=\"reference internal\" href=\"#snap-install\" id=\"id2\"><span>[snap-install]</span></a>.</p>", "a[href=\"#la-razon\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">La raz\u00f3n<a class=\"headerlink\" href=\"#la-razon\" title=\"Link to this heading\">#</a></h2><p>Este problema es originado por una modificaci\u00f3n en las preferencias de\n<code class=\"code docutils literal notranslate\"><span class=\"pre\">apt</span></code> que lo enga\u00f1a haciendo creer que no hay un paquete disponible que\ncumpla la solicitud. Esto es provocado por el comportamiento asociado al\ninstalador de <em>Chromium</em>, el cual, para su f\u00e1cil mantenimiento por parte del\nequipo de Ubuntu, han decidido usar un paquete DEB cuya \u00fanica funci\u00f3n es\ninvocar la instalaci\u00f3n desde snap (instalando snap si este no lo est\u00e1).</p><p>En lo personal no lo veo problem\u00e1tico, para mi el caso ideal es tener ojal\u00e1\ngestores de paquetes que terminen de instalar componentes desde otro gestor de\nforma autom\u00e1tica en lugar de yo encargarme del trabajo sucio. Pero el equipo de\nMint encuentra una falta de transparencia con sus usuarios que no son\nadvertidos de esto e incluso considerar como una falla de seguridad <a class=\"reference internal\" href=\"#snap-mint\" id=\"id1\"><span>[snap-mint]</span></a>.</p>"}
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
