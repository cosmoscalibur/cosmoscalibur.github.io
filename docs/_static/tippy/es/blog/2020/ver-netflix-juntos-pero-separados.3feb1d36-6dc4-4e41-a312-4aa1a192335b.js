selector_to_html = {"a[href=\"#ver-netflix-juntos-pero-separados\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Ver Netflix juntos pero separados<a class=\"headerlink\" href=\"#ver-netflix-juntos-pero-separados\" title=\"Link to this heading\">#</a></h1><p>Ante la necesidad de cuidarnos en esta cuarentena, hemos perdido los momentos\nde cine o de maratones con familia y amigos, pero hasta en esto hay forma de\ninnovar y buscar opciones para mantener un equivalente de estas actividades\nsin descuidar nuestra salud, cumpliendo cada protocolo requerido gracias a la\ntecnolog\u00eda.</p><p>As\u00ed que usemos algunos trucos para ver Netflix acompa\u00f1ados.</p>", "a[href=\"#id4\"]": "<figure class=\"align-center\" id=\"id4\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/rave-youtube-privacidad.jpg\"><img alt=\"Opci\u00f3n de privacidad y compartir enlace de sesi\u00f3n Rave.\" src=\"../../../../_images/rave-youtube-privacidad.jpg\" style=\"width: 250px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">Opci\u00f3n de privacidad y compartir enlace de sesi\u00f3n Rave. Ejemplo viendo\nMatarife en Youtube.</span><a class=\"headerlink\" href=\"#id4\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#transmisiones-en-vivo\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Transmisiones en vivo<a class=\"headerlink\" href=\"#transmisiones-en-vivo\" title=\"Link to this heading\">#</a></h2><p>Una opci\u00f3n que requiere tal vez un poco de ajustes y no es precisamente legal,\nes aprovechar la opci\u00f3n para crear transmisiones en vivo a trav\u00e9s de\nplataformas como <a class=\"reference external\" href=\"https://studio.youtube.com\">YouTube</a> (requieres canal),\n<a class=\"reference external\" href=\"https://www.facebook.com/live/producer/\">Facebook</a>, Twitch y otras.</p><p>No es legal porque al pagar nuestra suscripci\u00f3n de Netflix solo adquirimos el\nderecho para visualizaci\u00f3n y uso personal, no para retransmisi\u00f3n o\ndistribuci\u00f3n.</p>", "a[href=\"#netflix-party\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Netflix party<a class=\"headerlink\" href=\"#netflix-party\" title=\"Link to this heading\">#</a></h2><p><a class=\"reference external\" href=\"https://www.netflixparty.com/\">Netflix Party</a> es un\n<a class=\"reference external\" href=\"https://chrome.google.com/webstore/detail/netflix-party/oocalimimngaihdkbihfgmpkcpnmlaoa?hl=en\">complemento para Chrome</a>\nque permite sincronizar los controles de Netflix de los usuarios que compartan\nla sesi\u00f3n creada, por lo cual es necesario que cada uno posea acceso a Netflix.\nPor este motivo es legal, pues no es una retransmisi\u00f3n, todos los usuarios usan\nsu suscripci\u00f3n y el complemento solo se encarga de que todos est\u00e9n en la misma\nposici\u00f3n y habilitarles un chat integrado.</p>", "a[href=\"#rave\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Rave<a class=\"headerlink\" href=\"#rave\" title=\"Link to this heading\">#</a></h2><p><a class=\"reference external\" href=\"https://rave.io/\">Rave</a> es una aplicaci\u00f3n para\n<a class=\"reference external\" href=\"https://apps.apple.com/us/app/wemesh/id929775122\">iOS</a> y\n<a class=\"reference external\" href=\"https://play.google.com/store/apps/details?id=com.wemesh.android\">Android</a>\nque permite sincronizar Netflix, Youtube y otras plataformas, e incluso\npermitir la transmisi\u00f3n desde archivos en Google Drive y Dropbox. Adem\u00e1s\nincluye chat y llamada en dicha transmisi\u00f3n.</p><p>Importante al iniciar la transmisi\u00f3n, configurar la privacidad de la sesi\u00f3n\nRave si quieres solo compartirlo con tus amigos, de otra forma cualquier\nusuario Rave puede ingresar (es molesto porque participaran del chat y llamada\ntambi\u00e9n). La opci\u00f3n se encuentra al inicio del chat.</p>", "a[href=\"#id3\"]": "<figure class=\"align-center\" id=\"id3\">\n<a class=\"reference internal image-reference\" href=\"../../../../_images/netflixparty.png\"><img alt=\"Netflix Party y la columna de chat.\" src=\"../../../../_images/netflixparty.png\" style=\"width: 400px;\"/></a>\n<figcaption>\n<p><span class=\"caption-text\">As\u00ed luce Netflix Party y su columna de chat.</span><a class=\"headerlink\" href=\"#id3\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>"}
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
