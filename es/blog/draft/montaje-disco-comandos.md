montar sin máscara con

https://wiki.archlinux.org/title/NTFS#Unable_to_mount_with_ntfs3_with_partition_marked_dirty

```
❯ sudo mount -t ntfs3 /dev/sda1 /mnt
[sudo] contraseña para cosmoscalibur:
mount: /mnt: tipo de sistema de ficheros incorrecto, opción incorrecta, superbloque incorrecto en /dev/sda1, falta la página de códigos o el programa auxiliar, o algún otro error.
       dmesg(1) puede ser que tenga más información tras el fallo de la llamada al sistema de montaje
```

```
> sudo dmesg
[ 1662.331363]  sda: sda1
[ 1662.331822] sd 2:0:0:0: [sda] Attached SCSI disk
[ 1665.785708] ntfs3(sda1): It is recommened to use chkdsk.
[ 1665.834695] ntfs3(sda1): volume is dirty and "force" flag is not set!
[ 1871.971021] ntfs3(sda1): It is recommened to use chkdsk.
[ 1872.021796] ntfs3(sda1): volume is dirty and "force" flag is not set!
```
