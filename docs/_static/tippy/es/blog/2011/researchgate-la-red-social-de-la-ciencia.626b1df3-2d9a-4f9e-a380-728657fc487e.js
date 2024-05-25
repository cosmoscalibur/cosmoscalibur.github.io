selector_to_html = {"a[href=\"https://en.wikipedia.org/wiki/ResearchGate\"]": "<p><b>ResearchGate</b> is a European commercial social networking site for scientists and researchers to share papers, ask and answer questions, and find collaborators. According to a 2014 study by <i>Nature</i> and a 2016 article in <i>Times Higher Education</i>, it is the largest academic social network in terms of active users, although other services have more registered users, and a 2015\u20132016 survey suggests that almost as many academics have Google Scholar profiles.</p>", "a[href^=\"https://en.wikipedia.org/wiki/ResearchGate#\"]": "<p><b>ResearchGate</b> is a European commercial social networking site for scientists and researchers to share papers, ask and answer questions, and find collaborators. According to a 2014 study by <i>Nature</i> and a 2016 article in <i>Times Higher Education</i>, it is the largest academic social network in terms of active users, although other services have more registered users, and a 2015\u20132016 survey suggests that almost as many academics have Google Scholar profiles.</p>", "a[href=\"#id1\"]": "<figure class=\"align-center\" id=\"id1\">\n<img alt=\"Logotipo de ResearchGate\" src=\"../../../../_images/research-gate-logo.png\"/>\n<figcaption>\n<p><span class=\"caption-text\">Logotipo de ResearchGate.</span><a class=\"headerlink\" href=\"#id1\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#researchgate-la-red-social-de-la-ciencia\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">ResearchGate, la red social de la ciencia<a class=\"headerlink\" href=\"#researchgate-la-red-social-de-la-ciencia\" title=\"Link to this heading\">#</a></h1><p>Con el aumento del uso de la internet en nuestra vida diaria, constantemente hemos migrado todo tipo de actividades pertenecientes a esta al mundo virtual, convierti\u00e9ndonos de alguna manera en una nueva raza humana\u2026 un humano 2.0 llevando vidas 2.0.</p><p>En esa inmersi\u00f3n en la web donde la vida social y laboral ha sufrido cambios para adaptarse a las nuevas condiciones, la ciencia, como parte de la vida diaria y labor de muchos, tambi\u00e9n ha sufrido transformaciones.</p>"}
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
