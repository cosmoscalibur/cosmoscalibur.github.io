---
redirect: blog/determinar-intersecciones-en-el-diagrama-de-venn-con-r
date: 2020-06-13
tags: r language, bioinformatics, venn diagram
category: technology
author: Edward Villegas-Pulgarin
---

# Compute specific and intersection elements with R

This is my first posts about R language, my first english post and my first R
package: [`venn.compute`](https://github.com/cosmoscalibur/venn.compute), which
use case in bioinformatics is compare list of genes.

This R package is intended to compute specific elements in intersections of Venn
diagram instead of plot.

- Custom reader of files to create list of character arrays (such requiered for
  this package and VennDiagram).
- Compute specific elements in intersections of Venn diagram in memory or write
  to files.
- Plot with VennDiagram.
  

## Example

Use 3 files in `tests` directory with names `primes.txt`, `even.txt` y
`fibo.txt` whose content are primes, even and Fibonacci numbers until 20.

## Install

You can install from GitHub as:

```R
devtools::install_github("cosmoscalibur/venn.compute")
```

   Downloading GitHub repo cosmoscalibur/venn.compute@master


    formatR (1.6 -> 1.7) [CRAN]


    Installing 1 packages: formatR
    Updating HTML index of packages in '.Library'
    Making 'packages.html' ... done


    ✔  checking for file ‘/tmp/RtmpT7UVx3/remotes61d65fec5ae1/cosmoscalibur-venn.compute-6f4fb43/DESCRIPTION’ ...
    ─  preparing ‘venn.compute’:
    ✔  checking DESCRIPTION meta-information
    ─  checking for LF line-endings in source and make files and shell scripts
    ─  checking for empty or unneeded directories
    ─  building ‘venn.compute_1.1.0.tar.gz’


If an error about TAR executable is showed (common in Linux with Anaconda,
`sh: 1: /bin/gtar: not found`), you need to setup your TAR path.

```R
Sys.setenv(TAR = "/bin/tar")
```


 
## How to use


First, load the package.

```r
library(venn.compute)
```

### Lectura de archivos

### Read files

This is a custom reader to include multiple files and associate its custom
names, returned a named list of character arrays (each element is an element
line of the file).

```R
sets <- read.lists_from_files(c(file.path("tests", "primes.txt"),
                                file.path("tests", "even.txt"),
                                file.path("tests", "fibo.txt")),
                              c("primes", "even", "fibo"))
print(sets)
```

    $primes
    [1] "1"  "2"  "3"  "5"  "7"  "11" "13" "17"
    
    $even
     [1] "0"  "2"  "4"  "6"  "8"  "10" "12" "14" "16" "18"
    
    $fibo
    [1] "1"  "2"  "3"  "5"  "8"  "13"
    


### Compute intersections and specific elements

Now you can compute specific elements of Venn diagram intersections.

```R
venn.compute_specific(sets)
```

<dl>
	<dt>$primes_even_fibo</dt>
		<dd>'2'</dd>
	<dt>$primes_even</dt>
		<dd></dd>
	<dt>$primes_fibo</dt>
		<dd><ol class=list-inline>
	<li>'1'</li>
	<li>'3'</li>
	<li>'5'</li>
	<li>'13'</li>
</ol>
</dd>
	<dt>$even_fibo</dt>
		<dd>'8'</dd>
	<dt>$primes</dt>
		<dd><ol class=list-inline>
	<li>'7'</li>
	<li>'11'</li>
	<li>'17'</li>
</ol>
</dd>
	<dt>$even</dt>
		<dd><ol class=list-inline>
	<li>'0'</li>
	<li>'4'</li>
	<li>'6'</li>
	<li>'10'</li>
	<li>'12'</li>
	<li>'14'</li>
	<li>'16'</li>
	<li>'18'</li>
</ol>
</dd>
	<dt>$fibo</dt>
		<dd></dd>
</dl>

If you need to write sets in files, add an output path. Files are written
using convention of join sets name with underscore.

```R
venn.compute_specific(sets, output_dir = file.path("tests", "output"))
```

We can verify written files.


```R
dir(file.path("tests", "output"))
```


<ol class=list-inline>
	<li>'even_fibo.txt'</li>
	<li>'even.txt'</li>
	<li>'fibo.txt'</li>
	<li>'primes_even_fibo.txt'</li>
	<li>'primes_even.txt'</li>
	<li>'primes_fibo.txt'</li>
	<li>'primes.txt'</li>
</ol>


### Plot Venn diagram

Finally, if you want to save plot, invoke this function with the same arguments
as before (internally using
[`VennDiagram`](https://cran.r-project.org/web/packages/VennDiagram/index.html))

```r
venn.compute_plot(sets, output_dir = file.path("tests", "output"))
```

Now, we have a `primes_even_fibo.png` file.  

```{figure} /images/determinar-intersecciones-en-el-diagrama-de-venn-con-r/primes_even_fibo.png
:name: r_venn_1_en
:alt: Venn diagram generate here with VennDiagram.
:align: center

Venn diagram generate here with VennDiagram.
```
