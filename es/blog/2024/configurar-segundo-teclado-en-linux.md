---
date: 2024-05-19
tags: teclado
category: linux
---------------

# Configurar segundo teclado en Linux

```{update} 2026-04-18
Este artículo se publicó originalmente con instrucciones exclusivas para X11 usando `xinput` y `setxkbmap`. Se ha actualizado para incluir cómo hacerlo de forma nativa en Wayland (específicamente en KDE Plasma), el entorno gráfico por defecto en distribuciones modernas como Manjaro.
```

Si tienes un segundo teclado para conectar a tu equipo Linux, pero su
distribución de lenguaje es diferente, te explico como configurar aquí.

Resulta que, cuando ingresé a mi empleo actual, me entregaron como dotación un
equipo con teclado inglés. Y bueno, que problema acostumbrarme a la
configuración de teclado internacional para poder escribir con tildes o con "ñ".
Así que decidí comprar un teclado USB.

Resulta que, configurar el lenguaje del teclado en Linux es simple, incluso a
través de la interfaz gráfica, pero tiene un problema: la distribución de
lenguaje aplica para todos los teclados.

Sí, soy caprichoso, y lo que yo buscaba era que, ante una eventualidad, si usaba
el teclado original, funcionara adecuadamente, pero como se aplicaba la
distribución del teclado español no tenía el mapeo adecuado.

## El método moderno: Wayland y KDE Plasma

Si estás utilizando un entorno de escritorio moderno bajo Wayland, como KDE Plasma (por defecto en Manjaro KDE), la configuración es mucho más sencilla y no requiere la terminal. Wayland gestiona los dispositivos de entrada de manera independiente por diseño.

1. Abre las **Preferencias del sistema** (System Settings).
2. Dirígete a la sección de **Dispositivos de entrada** (Input Devices) y luego a **Teclado** (Keyboard).
3. En la pestaña de distribuciones (Layouts), notarás que puedes configurar un dispositivo específico.
4. Simplemente selecciona tu segundo teclado USB de la lista, añade la distribución deseada (ej. Español) y asegúrate de que esté asignada a ese dispositivo.

¡Y listo! Cada teclado funcionará con su propia distribución de manera nativa.

## El método tradicional: X11 (xinput y setxkbmap)

Si por el contrario sigues utilizando X11, o tienes un entorno que no expone esta configuración gráficamente, podemos usar la terminal. Ahora, manos a la obra:

### Método de entrada

Necesitamos conocer el método de entrada asociado, es decir, nuestros
dispositivos conectados para ingresar información, como el teclado, el ratón o
controles.

Para este fin usamos `xinput`. Es una utilidad para configurar y probar los
métodos de entrada.

```{code} bash
xinput
```

Y una salida típica lucirá así:

```{code-block}
---
linenos:
emphasize-lines: 15
---
⎡ Virtual core pointer                      id=2  [master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer                id=4  [slave  pointer  (2)]
⎜   ↳ USB Optical Mouse                         id=9  [slave  pointer  (2)]
⎜   ↳ Elan Touchpad                             id=11  [slave  pointer  (2)]
⎜   ↳ Elan TrackPoint                           id=12  [slave  pointer  (2)]
⎜   ↳ SIGMACHIP USB Keyboard Consumer Control   id=16  [slave  pointer  (2)]
⎣ Virtual core keyboard                     id=3  [master keyboard (2)]
    ↳ Virtual core XTEST keyboard               id=5  [slave  keyboard (3)]
    ↳ Power Button                              id=6  [slave  keyboard (3)]
    ↳ Video Bus                                 id=7  [slave  keyboard (3)]
    ↳ Sleep Button                              id=8  [slave  keyboard (3)]
    ↳ Integrated Camera: Integrated C           id=10  [slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard              id=13  [slave  keyboard (3)]
    ↳ ThinkPad Extra Buttons                    id=14  [slave  keyboard (3)]
    ↳ SIGMACHIP USB Keyboard                    id=15  [slave  keyboard (3)]
    ↳ SIGMACHIP USB Keyboard Consumer Control   id=17  [slave  keyboard (3)]
    ↳ SIGMACHIP USB Keyboard System Control     id=18  [slave  keyboard (3)]
```

Bueno, nuestra función será identificar en el listado anterior nuestro teclado.
En mi caso, el teclado corresponde a `SIGMACHIP USB Keyboard` y vemos que su
identificador es `id=15`.

## Configuración de lenguaje

Ya que sabemos el identificador del teclado, podemos asignarle una configuración
específica al teclado. Para este fin, usamos `setxkbmap`, que es la utilidad
para configuración del teclado.

El identificador previo, corresponde al argumento de `-device`, y el lenguaje
del teclado corresponde al argumento `-layout`. Es necesario que validemos muy
bien esto, porque para un mismo lenguaje existen variantes (`-variant`).
Ejemplo, en español podemos encontrar con variantes como latinoamérica, dvorak y
teclas muertas.

En mi caso, pues mi teclado corresponde al teclado español sin variantes, así
que, la ejecución será:

```{code} bash
setxkbmap -device 15 -layout es
```

Una vez ejecutado, nuestro segundo teclado tendrá la configuración española,
mientras que el teclado principal seguirá en inglés.
