---
date: 2020-06-13
tags: lenguaje r, bioinformática, diagrama de Venn
category: tecnología
author: Edward Villegas-Pulgarin
language: es
---

# Determinar intersecciones en el diagrama de Venn con R

Esta entrada es mi primera entrada asociada al lenguaje R y sobre mi primer paquete en R: [`venn.compute`](https://github.com/cosmoscalibur/venn.compute). Este paquete surge por un caso de uso particular que estaba ayudando a automatizar de determinar los elementos (no solo el dibujo ni la cantidad) de las intersecciones y específicos de un diagrama de Venn, útil en bioinformática para comparación de genes.

Así, esta entrada es tipo tutorial de como usar el paquete que hice para este fin.

## Caso de uso

Se posee la información de múltiples conjuntos en archivos de texto plano, en donde cada elemento es una línea de dicho archivo. No siempre es la misma cantidad de conjuntos y se desea poder generar archivos de salida para revisar las intersecciones y elementos específicos. Usualmente, puede importar el gráfico por lo cual se puede incluir.

Como ejemplo se usarán 3 archivos ubicados en una carpeta `tests`, con los nombres `primes.txt`, `even.txt` y `fibo.txt` con el contenido de los números primos, pares y de Fibonacci hasta el 20.

## Instalación

Por el momento, se debe instalar el paquete a partir de GitHub, por lo cual debes usar la utilidad incluida en `devtools` en lugar del mecanismo de instalación habitual (ya está sometido el paquete, así que en el futura podría usarse).

Si usas Anaconda en Linux, probablemente debas configurar la ruta del ejecutable de `tar` (al instalar desde GitHub genera un error indicando que no encuentra el ejecuta `sh: 1: /bin/gtar: not found`).


```R
Sys.setenv(TAR = "/bin/tar") # Si es Anaconda Linux
```

Ahora sí, haremos la instalación desde el repositorio de GitHub del paquete (se indica `usuario/paquete`).


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



## Ejecución

Lo primero que debemos hacer es cargar el paquete.


```R
library(venn.compute)
```

### Lectura de archivos

Para leer los archivos, he creado una función específica para la lectura, de manera que el contenido de los archivos sea cargado a arreglos de caracteres y estos se anexan a una lista. Adicional, se asocian los nombres personalizados a los conjuntos de elementos de cada archivo.

Las rutas a los archivos y los nombres que asociaremos, se agregan como
arreglos de caracteres, y tiene soporte genérico para una cantidad diferente
a la ilustrada.


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



Como observamos, se han creado las listas nombradas con los contenidos de los archivos. Estos nombres son los usados para crear los archivos, asociar las listas nombradas de las intersecciones y el gráfico (usa un paquete externo donde el ingreso de esta manera permite pasarlo como única variable).

### Determinar elementos

Ya con los conjuntos cargados en la lista, podemos determinar los elementos que van en cada área del diagrama de Venn (intersecciones y específicos).


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



Usando la convención del nombre asignado a los conjuntos unidos por guion bajo, se distinguen las áreas asociadas. Así, **\$primes_even_fibo** representa el área de intersección de los tres conjuntos, y posee solo un elemento (`'2'`), y **\$fibo** representa los específicos de dicho conjunto, es decir, los que pertenecen exclusivamente a este y no a intersecciones con otros, el cual en este caso es vacío.

Si esta información es masiva, es conveniente escribir el resultado en archivos y no en memoria. Así, debemos crear una carpeta para los archivos e indicamos su ruta como segundo argumento.


```R
venn.compute_specific(sets, output_dir = file.path("tests", "output"))
```

Podemos verificar la creación de los archivos con la misma convención de nombre y extensión `txt`.


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



### Graficar diagrama de Venn

Para obtener el diagrama tengo una función que define un flujo por defecto que crea los archivos del paso anterior y adicional el gráfico del diagrama con el paquete [`VennDiagram`](https://cran.r-project.org/web/packages/VennDiagram/index.html).


```R
venn.compute_plot(sets, output_dir = file.path("tests", "output"))
```


Además de generar como les conté, los archivos de las intersecciones y específicos, se generó un archivo cuyo nombre es la convención seguida para la intersección de la totalidad de conjuntos y con extensión `png`, `primes_even_fibo.png`.

```{figure} /images/determinar-intersecciones-en-el-diagrama-de-venn-con-r/primes_even_fibo.png
:name: r_venn_1
:alt: Diagrama de Venn generado para los 3 conjuntos.
:align: center

Diagrama de Venn generado para los 3 conjuntos.
```
