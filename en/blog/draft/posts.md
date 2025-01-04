# problemas wifi

La transición a #Manjaro no ha sido completamente limpia, pero no me ha
desilusionado. Si has presentado problemas con tu #wifi (aplicable a #Linux en
general), te cuento algunas posibles soluciones basadas en lo que me ocurrió en
https://www.cosmoscalibur.com/es/blog/2024/problemas-de-conexion-wifi-en-linux/

Resumen:

1. Si el equipo tiene doble arranque con Windows, o simplemente tenías fast boot
   habilitado, deshabilita este.
2. Deshabilita el modo de ahorro de energía de la tarjeta de red.
3. Deshabilita la aleatorización de la dirección MAC.

# instancia cloud manjaro

Aprovechando la transición a #Manjaro en la cual estoy reinstalando, les cuento
como conectarse a una instancia de #Google #CloudSql.

Resumen:

- Instalar Google Cloud SDK (#AUR)
  - Autenticación proyecto
  - Autenticación credenciales por defecto de aplicación
- Instalar Cloud SQL Proxy (AUR)
- Instalar cliente de base de datos. En este caso, uso #DbGate (flatpak)

https://www.cosmoscalibur.com/es/blog/2024/conecta-con-una-instancia-de-cloud-sql-en-manjaro/

# zsh starship manjaro

#Zsh en #Manjaro habilita por defecto #powerline como #prompt y esto hace que el
procedimiento oficial de #starship no funcione. En esta entrada de mi blog te
cuento el paso extra que requieres para tener Starship funcional en Manjaro.

https://www.cosmoscalibur.com/es/blog/2024/configurar-starship-en-manjaro-y-zsh/

# wayland gráficos híbridos

En #Manjaro experimenté un problema con las aplicaciones nativas de #Wayland que
hacen uso de #Vulkan para el renderizado que no me sucedió en Ubuntu. La
particularidad, en el equipo que me sucedió, tiene gráficos híbridos (#GPU
#NVIDIA y #AMD). Esto me afecta por ejemplo con #Zed. Les cuento como poder usar
las aplicaciones configurando una variable de entorno de Vulkan:
'VK_DRIVER_FILES'

https://www.cosmoscalibur.com/es/blog/2024/problema-de-wayland-y-graficos-hibridos-en-linux/
