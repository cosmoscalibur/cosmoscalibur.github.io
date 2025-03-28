---
date: 2024-12-18
tags: manjaro, wayland, zed, nvidia, gpu, linux, x11
category: tecnología, linux
---

# Problema de Wayland y gráficos híbridos en Linux

Los [gráficos híbridos](https://wiki.archlinux.org/title/Hybrid_graphics) son
una estrategia de los equipos modernos a incorporar dos tarjetas gráficas, una
integrada y una dedicada, con capacidades y consumo de energía diferentes. La
idea es no usar la dedicada, salvo que sea requerido para el renderizado 3D. Sin
embargo, esto no es un problema resuelto en Linux y afecta a las aplicaciones
nativas en Wayland, el cual es el nuevo y moderno protocolo para comunicación de
servidor gráfico usado por los compositores de ventanas en Linux (en reemplazo
de X11), que hagan uso de Vulkan.

Una de estas aplicaciones afectadas es el editor de código {program}`zed`. Al
momento de escribir esta entrada, la versión del controlador NVIDIA es 550.135
en la rama estable de Manjaro.

## Síntomas del problema

### Caso Zed

Considerando el ejemplo de {program}`zed`, al ejecutar en Wayland, veremos por
un breve momento que se intenta lanzar una ventana, pero a los pocos segundos se
cierra. Podemos entrar a detallar mucho más, y podemos probar en la terminal
`zed --foreground`, y allí veremos el error
`"payload": "called `Result::unwrap()`on an`Err` value: ERROR_INITIALIZATION_FAILED"`.

Si como yo, te ves afectado por este problema, puedes también contribuir con
información útil al proyecto de Zed, reportando la salida de `vulkaninfo` y
`RUST_LOG=blade_graphics=debug zed --foreground`, con info extra de lo siguiente
que veremos para entender si el problema es más cercano a Vulkan/Wayland, o
propiamente a Zed. Es el reporte
[zed/8168](https://github.com/zed-industries/zed/issues/8168).

### Caso VkCube (demo)

Resulta que Vulkan posee unas aplicaciones de demostración para X11 y Wayland,
`vkcube` y `vkcube-wayland` (disponibles en el paquete `vulkan-tools`), y lo
esperado es que si estas funcionan, Zed (y otras basadas en Vulkan) deberían
funcionarte, al menos por soporte de la plataforma.

En mi caso, `vkcube` funciona sin problema y Zed en X11 al menos abre la primera
vez de la sesión, pero `vkcube-wayland` reporta
`segmentation fault (core dumped)`. Esto último lleva a que probablemente las
aplicaciones nativas de Wayland con Vulkan no funcionen adecuadamente.

Ahora, posiblemente esto depende realmente de NVIDIA para los casos híbridos,
porque en lo observado en Zed y con reportes de Vulkan, la afectación no ocurre
en equipos con solo integrada o solo NVIDIA. Los casos reportados en Zed con
solo integrada, era suficiente con instalar el controlador Vulkan adecuado para
solucionar el problema. Y en Kubuntu 24.10 (que lo probé unas semanas), Zed me
funcionó perfectamente en Wayland (pero entiendo que el controlador NVIDIA es de
la serie 560).

## Saber si tengo gráficos híbridos

Para conocer si tu caso es por gráficos híbridos, puedes revisar la salida de
las siguientes instrucciones

```{code-block} bash
---
caption: Consulta de controladores compatibles con salida VGA. Cualquier distribución
  Linux.
---
❯ lspci | grep VGA
01:00.0 VGA compatible controller: NVIDIA Corporation TU106M [GeForce RTX 2060 Mobile] (rev a1)
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir [Radeon Vega Series / Radeon Vega Mobile Series] (rev f0)
```

```{code-block} bash
---
caption: Utilidad de Manjaro para consultar controladores.
---
❯ mhwd -li
> Installed PCI configs:
--------------------------------------------------------------------------------
                  NAME               VERSION          FREEDRIVER           TYPE
--------------------------------------------------------------------------------
           video-linux            2024.05.06                true            PCI
video-hybrid-amd-nvidia-prime            2023.03.23               false            PC
```

En ambos casos de puede apreciar la disponibilidad de una tarjeta gráfica NVIDIA
y la tarjeta gráfica AMD (también podría ser Intel). Así que, esto puede ser la
causa (considerando la versión del controlador NVIDIA).

## Saber la versión del controlador NVIDIA

Si no eres consciente de la versión del controlador, puedes usar tu
[gestor de paquetes para consultarlo](#pamac-commands), validando la versión del
paquete de `nvidia-utils`. En mi caso, sería `pamac info nvidia-utils` o en
derivados de Ubuntu, `apt show nvidia-utils`.

También puedes ejecutar {program}`nvidia-smi`, y lo verás en la primera fila,
`Driver version`.

## Solución provisional

Es claro que queremos poder usar nuestras aplicaciones favoritas, como en mi
caso lo es poder usar {program}`zed`. Sobre algunos problemas de Wayland en
Manjaro, asociados con la tarjeta gráfica NVIDIA, he visto que la conclusión es
esperar la serie 560, pero esta sigue en la rama inestable.

Pero mientras esto ocurre, podemos
[indicar explícitamente al controlador de Vulkan](https://vulkan.lunarg.com/doc/view/1.3.250.1/windows/LoaderDriverInterface.html#overriding-the-default-driver-discovery)
que haga uso de la configuración de la tarjeta integrada. Los archivos de
configuración disponibles se encuentran en el directorio
{file}`/usr/share/vulkan/icd.d/`. Si es la tarjeta AMD, son los archivos que
mencionan *radeon*, y el caso de Intel dirá *intel*. Esto se logra asignando la
lista a la
[variable de entorno `VK_DRIVER_FILES`](https://wiki.archlinux.org/title/Vulkan#NVIDIA_-_vulkan_is_not_working_and_can_not_initialize).
En mi caso, sería:

```{code} bash
export VK_DRIVER_FILES=/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json
```

Una vez realices este cambio, puedes probar nuevamente {program}`vkcube-wayland`
o {program}`zed`, y si funciona, hacer este cambio permanente en el archivo
{filename}`/etc/environment`.

```{code} bash
sudo bash -c "echo 'VK_DRIVER_FILES=/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json' >> /etc/environment"
```

Este cambio también soluciona el error en X11 en la cual las aperturas
posteriores dejan una ventana invisible.

## Solución definitiva

Cuando se encuentre disponible la serie 560 espero contarles si esto en Manjaro
resolvió el problema, y para ese momento es necesario remover la línea anterior
de las variables de entorno. Y cuando deseemos ejecutar algo directamente con la
tarjeta NVIDIA, deberemos usar {program}`prime-run`, que en este momento no hace
diferencia.

Sin remover la línea, y solo para probar con el fin de saber si vale la pena
hacerlo, puedes desasignar la variable con `unset VK_DRIVER_FILES`.
