---
date: 2025-01-10
tags: manjaro, ubuntu, linux, disco externo, mount, lsblk
category: tecnología, linux
---

# Montar disco en Linux y error de volumen sucio

Llevaba algún tiempo sin usar mi disco externo, en formato NTFS, y cuando fui a
usarlo (montarlo) después de actualizar el sistema operativo, me ha salido el
error de volumen sucio. Si te ha pasado, a continuación te indico como
solucionarlo.

## Montaje de disco en Linux

Para montar nuestro disco por línea de comandos en Linux, procedemos primero a
consultar el punto en el cual se encuentra disponible, esto lo hacemos con
`lsblk`.

La salida es similar a lo que vemos a continuación. Las unidades externas
(disco, USB, etc.), se anexan a los puntos `sd*`, que en este caso es `sda1`
(debemos tomarlo con el numeral). Estos puntos siempre van precedidos de la ruta
{file}`/dev/`.

```{code}
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 931,5G  0 disk
└─sda1        8:1    0 931,5G  0 part
nvme0n1     259:0    0 953,9G  0 disk
├─nvme0n1p1 259:1    0   300M  0 part /boot/efi
└─nvme0n1p2 259:2    0 953,6G  0 part /
```

Debemos disponer de un directorio para el montaje de la unidad, así que
crearemos un directorio nuevo (o si lo dispones ya):

```{code}
mkdir -p ~/media/eddisk
```

Ahora realizamos el montaje:

```{code}
sudo mount -t ntfs-3g /dev/sda1 ~/media/eddisk
```

Si todo está bien, ya disponemos del disco disponible en ese directorio.

## Error de volumen sucio

La historia en mi caso, es que no todo estaba bien, no funcionaba el automontaje
ni el montaje por línea de comandos. Algo curioso, es que el montaje con el
gestor de archivos (en mi caso, {program}`dolphin`, ya que uso KDE como entorno
de escritorio), funcionaba correctamente. Al parecer, este error se puede
producir cuando usas el disco en Windows con *fast boot* habilitado.

El error que veremos será:

> tipo de sistema de ficheros incorrecto, opción incorrecta, superbloque
> incorrecto en /dev/sda1, falta la página de códigos o el programa auxiliar, o
> algún otro error. dmesg(1) puede ser que tenga más información tras el fallo
> de la llamada al sistema de montaje

Al inspeccionar con la sugerencia del error, `sudo dmesg`

```{code}
[ 1662.331363]  sda: sda1
[ 1662.331822] sd 2:0:0:0: [sda] Attached SCSI disk
[ 1665.785708] ntfs3(sda1): It is recommened to use chkdsk.
[ 1665.834695] ntfs3(sda1): volume is dirty and "force" flag is not set!
```

Esto nos indica que presentamos el error de volumen sucio y podemos solucionarlo
ejecutando:

```{code}
sudo ntfsfix -d /dev/sda1
```

## Referencias

- ArchLinux Wiki.
  [NTFS - Unable to mount with ntfs3 with partition marked dirty](https://wiki.archlinux.org/title/NTFS#Unable_to_mount_with_ntfs3_with_partition_marked_dirty)
- AskUbuntu.
  [ntfs external hard drive does not mount](https://askubuntu.com/questions/1513180/ntfs-external-hard-drive-does-not-mount)
- AskUbuntu.
  [How to correctly fix a "dirty" NTFS partition without using chkdsk](https://askubuntu.com/questions/112150/how-to-correctly-fix-a-dirty-ntfs-partition-without-using-chkdsk)
