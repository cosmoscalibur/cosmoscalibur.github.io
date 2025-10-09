---
date: 2025-05-0
tags: manjaro, arch, aur, pamac
category: tecnologia, linux
---

# Error de caché al actualizar paquetes AUR

He presentado problemas de instalación de las actualizaciones de paquetes AUR,
en particular con el paquete
[`cloud-sql-proxy`](https://aur.archlinux.org/packages/cloud-sql-proxy/). Y el
error experimentado se corresponde con el permiso denegado para el borrado de
archivos en el directorio de caché de AUR (un directorio temporal,
{file}`/var/tmp/pamac-build-<user>/`), con los archivos de dependencias de Go.

Ejemplo del error:

```{code} bash
```

## Solución al error de caché AUR

La solución de fondo a este problema, realmente corresponde al responsable del
paquete AUR, quien debería incluir en el {file}`PKGBUILD` una línea sobre el
borrado de archivos en el directorio de caché de AUR, que en este caso
corresponde a `go clean -modcache`.

Sin embargo, si el mantenedor del paquete no lo hace, tenemos las siguientes
opciones, que pueden ser válidas para otros problemas generados por la caché de
los paquetes, o incluso simplemente por la cantidad de espacio en disco que se
acumula. Estos pasos son necesarios antes de una actualización, si los paquetes
afectados no han sido ajustados por los mantenedores.

- Borrar manualmente el directorio de caché del paquete AUR:
  `rm -rf /var/tmp/pamac-build-<user>/cloud-sql-proxy`.
- Instrucción para limpiar el caché de paquetes AUR: `pamac clean` o específico
  para la caché de paquetes AUR, `pamac clean -b`.

Otra alternativa es utilizar la versión de paquetes binarios cuando estén
disponibles (terminan en `-bin`), de esta forma no se atraviesa por el proceso
de compilación/construcción del paquete. En este caso puede ser usar
`cloud-sql-proxy-bin`, aunque este posee una frecuencia de actualización menor.

## Referencias

- [Cleaning up and freeing disk space](https://forum.manjaro.org/t/cleaning-up-and-freeing-disk-space/6703/31).
  Manjaro Forum.
- [Pamac: Cleaning the Cache](https://wiki.manjaro.org/index.php/Pamac#Cleaning_the_Cache).
  Manjaro Wiki.
- [Pamac clean ALL caches in a one liner script](https://forum.manjaro.org/t/pamac-clean-all-caches-in-a-one-liner-script/84233/2).
  Manjaro Forum.
- [AUR package build fails because it cannot remove build files: Permission denied](https://gitlab.manjaro.org/applications/pamac/-/issues/1114).
  Pamac GitLab.
