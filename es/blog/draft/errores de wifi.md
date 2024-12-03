
Si el WiFi de manera aleatoria comienza a desconectarse, y al revisar el
listado de redes estas han desaparecido, algunos detalles por evaluar son:

+ [Deshabilitar "fast boot" de la BIOS](https://bbs.archlinux.org/viewtopic.php?pid=2134101#p2134101):
  En Ubuntu esto no es problema, pero al movernos a Manjaro o derivadas de
  Arch, esto es un problema replicable. Asegúrate de deshabilitar "Fast boot"
  en la BIOS.
+ [Deshabilitar el ahorro de energía de la tarjeta de WiFi](https://forum.manjaro.org/t/wifi-random-disconnects-after-update/142876/3):
  Es recurrene que el modo de ahorro de energía con la tarjeta de WiFi lleve a
  que dejemos de ver las conexiones disponibles. Por lo cual es necesario crear
  el archivo de configuración que apague esta característica y reiniciamos.
  Debes crear el archivo como administrador.

  ```{code}
  ## File: /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  [connection]
  wifi.powersave = 2
  ```

Estos dos ajustes fueron suficientes en mi escenario, sin embargo, no fue tan
claro que debían ser las dos cosas. Esto fue una mezcla de probar distintas
soluciones que reportaban y de probar efectos de las combinaciones. Ejemplo, al
tener deshabilitado "*fast boot*" ya me conectaba siempre desde el inicio, pero
se perdían las redes al rato. Si tenía deshabilitado el ahorro de energía
solamente, permanecían las redes, pero nunca conectaba. Solo al tener las dos
en conjunto funcionó.

También suelen reportar que [deshabilitar la aleatorización de la MAC](https://forum.manjaro.org/t/wifi-not-connecting-at-start-up/113193/3)
ayuda, pero en mi caso esta prueba no tuvo efectos.

[Algunos comandos de inspección](https://forum.manjaro.org/t/cant-get-wifi-to-work-on-asus-laptop-manjaro-kde/144291)
