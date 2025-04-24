---
date: 2025-04-23
tags: contenedor, docker, linux, manjaro
category: tecnologia, programación
---

# Instalar Docker en Manjaro

En el pasado publiqué un artículo de como
[instalar y usar Docker en Ubuntu con Snap](es/blog/2019/crear-contenedor-docker-aplicacion-gui-ealite.rst)
y ahora que uso Manjaro vale la pena revisar los pasos para instalar Docker en
Manjaro.

Por motivos laborales ahora más que nunca es importante para mí el uso de
Docker, porque en Tributi nuestro sistema operativo oficial en el área de
tecnología es Ubuntu (ahora en versión 24.04). Como en mi equipo tengo Manjaro,
mi ambiente local ya no me sirve para las pruebas y necesito una forma de
asegurar el mismo ambiente. Para ello, Docker se vuelve en la alternativa
adecuada de reproducibilidad.

## Docker en repositorio

En Manjaro (y Arch) se puede instalar Docker desde el repositorio de paquetes
oficiales. Debemos tener presente que la componente de composición de
contenedores se encuentra en el paquete `docker-compose`.

```bash
pamac install docker docker-compose --no-confirm
```

## Configuración de Docker

Con el fin de disponer Docker para ser invocado, podemos habilitar el servicio
del demonio o del *socket*. La primera opción es adecuada para entornos de
servidores y la segunda para entornos locales para reducir el consumo de
recursos (este queda activo con el primer llamado, a diferencia de la primera
opción que queda activo desde el arranque del sistema).

Para habilitar el servicio del demonio, ejecutamos:

```bash
sudo systemctl enable docker.service
```

Para habilitar el servicio del *socket*, ejecutamos:

```bash
sudo systemctl enable docker.socket
```

De momento esto nos permite inicializar Docker, pero debemos ejecutarlo siempre
con permisos de administrador. Si deseamos ejecutarlo sin permisos de
administrador, podemos agregar nuestro usuario al grupo `docker`:

```bash
sudo usermod -aG docker $USER
```

## Referencias

- [Docker](https://wiki.archlinux.org/title/Docker). Wiki ArchLinux.
- [docker.service tops the systemd-analyze critical path](https://github.com/moby/moby/issues/38373#issuecomment-447393517).
  Repositorio Moby.
