selector_to_html = {"a[href=\"#compute-intersections-and-specific-elements\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Compute intersections and specific elements<a class=\"headerlink\" href=\"#compute-intersections-and-specific-elements\" title=\"Link to this heading\">#</a></h3><p>Now you can compute specific elements of Venn diagram intersections.</p>", "a[href=\"#example\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Example<a class=\"headerlink\" href=\"#example\" title=\"Link to this heading\">#</a></h2><p>Use 3 files in <code class=\"docutils literal notranslate\"><span class=\"pre\">tests</span></code> directory with names <code class=\"docutils literal notranslate\"><span class=\"pre\">primes.txt</span></code>, <code class=\"docutils literal notranslate\"><span class=\"pre\">even.txt</span></code> y\n<code class=\"docutils literal notranslate\"><span class=\"pre\">fibo.txt</span></code> whose content are primes, even and Fibonacci numbers until 20.</p>", "a[href=\"#lectura-de-archivos\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Lectura de archivos<a class=\"headerlink\" href=\"#lectura-de-archivos\" title=\"Link to this heading\">#</a></h3>", "a[href=\"#plot-venn-diagram\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Plot Venn diagram<a class=\"headerlink\" href=\"#plot-venn-diagram\" title=\"Link to this heading\">#</a></h3><p>Finally, if you want to save plot, invoke this function with the same arguments\nas before (internally using\n<a class=\"reference external\" href=\"https://cran.r-project.org/web/packages/VennDiagram/index.html\"><code class=\"docutils literal notranslate\"><span class=\"pre\">VennDiagram</span></code></a>)</p>", "a[href=\"#compute-specific-and-intersection-elements-with-r\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">Compute specific and intersection elements with R<a class=\"headerlink\" href=\"#compute-specific-and-intersection-elements-with-r\" title=\"Link to this heading\">#</a></h1><p>This is my first posts about R language, my first english post and my first R\npackage: <a class=\"reference external\" href=\"https://github.com/cosmoscalibur/venn.compute\"><code class=\"docutils literal notranslate\"><span class=\"pre\">venn.compute</span></code></a>, which\nuse case in bioinformatics is compare list of genes.</p><p>This R package is intended to compute specific elements in intersections of Venn\ndiagram instead of plot.</p>", "a[href=\"#install\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Install<a class=\"headerlink\" href=\"#install\" title=\"Link to this heading\">#</a></h2><p>You can install from GitHub as:</p>", "a[href=\"#how-to-use\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">How to use<a class=\"headerlink\" href=\"#how-to-use\" title=\"Link to this heading\">#</a></h2><p>First, load the package.</p>", "a[href=\"#r-venn-1-en\"]": "<figure class=\"align-center\" id=\"r-venn-1-en\">\n<img alt=\"Venn diagram generate here with VennDiagram.\" src=\"../../../../_images/primes_even_fibo.png\"/>\n<figcaption>\n<p><span class=\"caption-text\">Venn diagram generate here with VennDiagram.</span><a class=\"headerlink\" href=\"#r-venn-1-en\" title=\"Link to this image\">#</a></p>\n</figcaption>\n</figure>", "a[href=\"#read-files\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Read files<a class=\"headerlink\" href=\"#read-files\" title=\"Link to this heading\">#</a></h3><p>This is a custom reader to include multiple files and associate its custom\nnames, returned a named list of character arrays (each element is an element\nline of the file).</p>"}
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
