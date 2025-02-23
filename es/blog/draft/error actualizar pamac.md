❯ pamac update Preparando... ==== AUTHENTICATING FOR org.manjaro.pamac.commit
==== Se requiere autentificación para instalar, actualizar o eliminar paquetes
Authenticating as: Edward Villegas (cosmoscalibur) Password: ==== AUTHENTICATION
COMPLETE ==== Sincronizando bases de datos de paquetes... cp: no se puede
acceder a '/var/lib/pacman/sync/download-QIm2wN': Permiso denegado Error: Fallo
al preparar la transacción: base de datos no válida o dañada

~ took 10s ❯ sudo pacman-mirrors --fasttrack

Solución

- https://bbs.archlinux.org/viewtopic.php?id=268153
- https://forum.manjaro.org/t/hi-i-have-a-notification-by-493-updates-and-when-a-try-it-the-system-says-fallo-al-preparar-la-transaccion-base-de-datos-no-valida-o-danada/124119
- https://forum.manjaro.org/t/permission-denied-in-pamac-output/171654/2

```{code} bash
sudo rm -R /var/lib/pacman/sync/
sudo pacman-mirrors --fasttrack
sudo pacman -Syyu
LANG=C pamac update --force-refresh
```

Si el error es
`Error: Fallo al preparar la transacción: Objetivo no encontrado:`
