---
date: 2024-12-07
tags: manjaro, ubuntu, wifi, linux, dmesg
category: tecnología, linux
---

# Problemas de conexión wifi en Linux

Si el WiFi de manera aleatoria comienza a desconectarse, y al revisar el listado
de redes estas han desaparecido, algunos detalles por evaluar son:

- [Deshabilitar "fast boot" de la BIOS](https://bbs.archlinux.org/viewtopic.php?pid=2134101#p2134101):
  En Ubuntu pareciera no ser un problema actualmente (no me había sucedido en el
  mismo equipo con esa configuración, pero existen publicaciones de años
  anteriores relacionadas a Ubuntu con esto), pero al movernos a Manjaro o
  derivadas de Arch, esto es un problema replicable. Asegúrate de deshabilitar
  "Fast boot" en la BIOS.

- [Deshabilitar el ahorro de energía de la tarjeta de wifi](https://forum.manjaro.org/t/wifi-random-disconnects-after-update/142876/3):
  Es recurrente que el modo de ahorro de energía con la tarjeta de wifi lleve a
  que dejemos de ver las conexiones disponibles. Por lo cual es necesario crear
  el archivo de configuración que apague esta característica y reiniciamos.
  Debes crear el archivo como administrador.

  ```{code} text
  ## File: /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  [connection]
  wifi.powersave = 2
  ```

Estos dos ajustes fueron suficientes en mi escenario, sin embargo, no fue tan
claro que debían ser las dos cosas. Esto fue una mezcla de probar distintas
soluciones que reportaban y de probar efectos de las combinaciones. Ejemplo, al
tener deshabilitado "*fast boot*" ya me conectaba siempre desde el inicio, pero
se perdían las redes al rato. Si tenía deshabilitado el ahorro de energía
solamente, permanecían las redes, pero nunca conectaba. Solo al tener las dos en
conjunto funcionó.

Para dar contexto de mi caso específico, tengo Manjaro KDE 24.1 con núcleo 6.11.
La tarjeta de red es *Realtek* y el equipo es ASUS TUF Gaming A15 FA506IV.

También suelen reportar que
[deshabilitar la aleatorización de la MAC](https://forum.manjaro.org/t/wifi-not-connecting-at-start-up/113193/3)
ayuda, pero en mi caso esta prueba no tuvo efectos.

```{code} text
## File: /etc/NetworkManager/conf.d/wifi_rand_mac.conf
[device]
wifi.scan-rand-mac-address=no
```

## Obtén información útil para diagnóstico

Uno de los puntos importantes para buscar como solucionar tus problemas y será
clave si escribes en los foros, es conocer información sobre tu hardware y
controladores.

**Obtener información general de sistema**

Para este caos específico puede ser útil la información de la sección *Network*
y *System*, pero no cortes el resultado si lo publicas en un foro. Estas
utilidades no son solo cuando el error es de wifi, también te aporta información
para otros problemas de hardware.

```{code} bash
inxi --full --admin --filter --width
```

**Obtener información de controladores**

En este punto podemos detallar el controlador y versión de controlador, buscando
la mención de *Network*.

::::\{tab-set} :::\{tab-item} Manjaro

```{code} bash
sudo mhwd -l -li
```

::: :::\{tab-item} Ubuntu

```{code} bash
sudo lshw
```

::: ::::

**Mensajes de diagnóstico del núcleo**

Podemos buscar por mensajes del núcleo asociados al controlador. Ten presente el
controlador desde la sección de *Network* de `inxi`. En mi caso, es `r8169` y
`rtw_8822ce`.

```{code} bash
sudo dmesg | grep r8169
sudo dmesg | grep rtw_8822ce
```
