selector_to_html = {"a[href=\"#marte-nos-trasnocha\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Marte nos trasnocha<a class=\"headerlink\" href=\"#marte-nos-trasnocha\" title=\"Link to this heading\">#</a></h1><p>Con este lema\n(<a class=\"reference external\" href=\"https://twitter.com/#!/search/martenostrasnocha?q=martenostrasnocha\">#MarteNosTrasnocha</a>\npopularizado como hashtag en las redes twitter y google+), el\n<a class=\"reference external\" href=\"http://www.planetariomedellin.org/planetario/29088_pasemos-la-noche-en-el-planetario.html\">Planetario Jesus Emilio\nRamirez</a>\nde la ciudad de Medell\u00edn nos convoca a participar hoy de uno de los\neventos m\u00e1s esperados por la comunidad astron\u00f3mica mundial.\nAficionados y profesionales de la astronom\u00eda se reunir\u00e1n hoy desde las\n8pm en el planetario a ver la transmisi\u00f3n en directo de <a class=\"reference external\" href=\"http://www.ustream.tv/nasajpl\">NASA\nJPL</a> (si deseas ver la transmisi\u00f3n,\npuedes dar click en el link) de la llegada del Mars Curiosity a marte.</p><p>\u00bfPor que es tan esperado este evento? M\u00faltiples aspectos hacen de esta\nuna misi\u00f3n \u00fanica para la recolecci\u00f3n de datos de intereses no\nsolo cient\u00edficos sino tambi\u00e9n ingenieriles. El\n<a class=\"reference external\" href=\"http://mars.jpl.nasa.gov/msl/\">MSL</a> (Mars Science Laboratory) esta\nequipado con una instrumentaci\u00f3n cient\u00edfica muy variada destinada\nal an\u00e1lisis de tipo f\u00edsico, qu\u00edmico, geol\u00f3gico y biol\u00f3gico,\ntotalizando 10 instrumentos. La selecci\u00f3n del sitio de aterrizaje, el\ncr\u00e1ter Galera, corresponde al tipo de suelo observado en la regi\u00f3n,\nque corresponde a formaciones sedimentarias, que hacen del sitio un\ncandidato para la b\u00fasqueda de mol\u00e9culas org\u00e1nicas.</p>"}
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
