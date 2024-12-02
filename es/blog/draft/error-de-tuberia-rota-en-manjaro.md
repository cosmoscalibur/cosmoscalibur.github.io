Si usas

```{code}
sudo pamac build dropbox

dropbox-lnx.x86_64-211.4.6008.tar.gz ... cat: error de escritura: Tubería rota
FIRMA NO ENCONTRADA
HA FALLADO
==> ERROR: ¡No se ha podido verificar alguna de las firmas PGP!
Finished with result: exit-code
Main processes terminated with: code=exited, status=1/FAILURE
Service runtime: 7.592s
CPU time consumed: 3.329s
Memory peak: 118.2M (swap: 0B)
Error: Fallo al construir dropbox
```

El error se soluciona con

```{code}
pamac build dropbox
```

El problema ocurre porque la firma debe agregarse a nivel de usuario y no de
sistema.

https://forum.manjaro.org/t/cant-upgrade-dropbox-due-to-key-error/105830

spotify tiene la misma situación
