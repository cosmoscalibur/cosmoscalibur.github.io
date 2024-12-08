:date: 2019-11-22
:tags: contenedor, docker, linux, wine, enterprise architect, ealite
:category: tecnología
:author: Edward Villegas-Pulgarin
:language: es

Crear contenedor Docker aplicación GUI - EALite
===============================================

Dando continuidad al uso de contenedores que inicie en la publicación anterior,
:doc:`/es/blog/2019/crear-contenedor-lxc-para-aplicacion-gui-ealite`, reproduciré la
instalación de Enterprise Architect Viewer (EALite) con Docker (y por supuesto,
Wine). Si deseas reproducir el ejemplo de este caso, requieres reproducir la
el artículo mencionado para extraer el directorio de Wine.

A diferencia de LXC, Docker está más orientado al aislamiento de aplicaciones y
no de sistema operativo (LXC cumple una función más cercana a una máquina
virtual) lo cual ayuda a un mejor despliegue de aplicaciones y la
estandarización de las etapas de desarrollo y de pruebas.

Común a LXC tenemos imágenes base que podemos usar, disponibles en
`DockerHub`_. A partir de estas podemos completar
nuestras necesidades especificando en el archivo Dockerfile.

Instalar Docker
---------------

Recomiendo en Linux instalar docker con snap.

.. code::

   sudo snap install docker

Posteriormente, podemos asociar nuestro usuario para la ejecución sin ser
administrador.

.. code::

   sudo groupadd docker
   sudo usermod -aG docker $USER
   newgrp docker

Puedes probar ejecutando como usuario regular, :code:`docker run hello-world`.

Dockerfile
----------

Este archivo es el mecanismo mediante el cual se especifican las reglas de
construcción de nuestra imagen. Se define un lenguaje común sin importar el
sistema operativo base y las funciones específicas del sistema son usadas con
una instrucción que habilita a ejecución en él.

Los comentarios en el archivo son como tradicionalmente estamos acostumbrados
en otros lenguajes (entre ellos, bash), con signo número :code:`#`. Esto posee
una excepción, y es el caso donde existe una directriz después como el caso que
se ejemplificara.

La directriz :code:`escape` es usada para cambiar el carácter de salto de línea
para instrucciones de múltiples líneas. Se puede tener la habitual barra
invertida (``\``) que es conflictivo con rutas con espacios en Linux o
rutas Windows, y la opción de la tilde invertida (`````).

Después podemos definir la imagen base usando :code:`FROM` seguido de la
especificación de la imagen en `DockerHub`_. En este caso, usaremos la `imagen
Docker de Ubuntu <https://hub.docker.com/_/ubuntu>`_ con arquitectura i386 y
versión 18.04. En general, la estructura de invocación es
:code:`arquitectura/ubuntu:version`.

Las instrucciones son ejecutadas por defecto por el usuario *root*
(administrador), de manera que podemos ejecutar la instalación de paquetes
invocando directamente el llamado al sistema iniciando con :code:`RUN`. Como se
observa en el ejemplo, a continuación es una línea típica que se ejecuta en
Ubuntu.

.. note::

   La creación del usuario es necesaria porque wine debe ejecutarse por un
   usuario regular. Adicional, el nombre de usuario corresponde al mismo nombre
   del usuario Linux del cual traemos la copia de la instalación en Wine (Wine
   asigna el nombre de usuario Windows igual al usuario Linux, luego, al copiar
   la carpeta de Wine, solo funcionará si encuentra el mismo usuario).

Podemos cambiar el directorio sobre el cual ejecutamos usando :code:`WORKDIR`.
En la siguiente línea usamos :code:`COPY` para mover un directorio del sistema
hospedador a la imagen. Existe una instrucción similar, :code:`ADD`, la cual
soporta que la fuente sea una URL realizando la descarga, y descomprime
archivos *tar*.

.. note::

   El directorio que moveremos se genero en el contenedor LXC que construimos
   en :doc:`/es/blog/2019/crear-contenedor-lxc-para-aplicacion-gui-ealite`. Para ello,
   iniciamos el contenedor y extraemos el directorio.

   .. code::

      sudo lxc start ea
      sudo lxc file pull -r ea/home/ubuntu/.wine .

Con :code:`USER` cambiamos el usuario que ejecuta los procesos. Es importante
que a la hora de concluir, si un proceso es ejecutado por un usuario regular,
nuestro último cambio de usuario debe apuntar a él, de otra forma el
contenedor estará activo para el usuario administrador. Otro aspecto importante
es el comportamiento por defecto en Linux, donde puede crear el usuario si no
existe (pero no el directorio de usuario).

Finalmente, es necesario indicar que se ejecuta cuando se lanza el contenedor.
Esto es posible con :code:`CMD` o con :code:`ENTRYPOINT`. La diferencia es que
el primero permite sobreescribir la ejecución enviando como parámetro lo que
se desea ejecutar, mientras que la segunda opción solo ejecuta la configurada.

.. code::

   # escape=`
   FROM i386/ubuntu:18.04
   RUN apt update -q && apt install --install-recommends -y wine-stable
   RUN apt install -y fonts-crosextra-carlito
   RUN useradd -ms /bin/bash ubuntu
   WORKDIR /home/ubuntu
   COPY .wine .wine
   RUN chown -R ubuntu .wine
   USER ubuntu
   RUN mkdir -p .local/bin && `
           echo "wine $HOME/.wine/drive_c/Program\ Files/Sparx\ Systems/EA\ LITE/EA.exe" > .local/bin/ealite && `
           chmod 755 .local/bin/ealite
   CMD ".local/bin/ealite"

Construir imagen Docker
-----------------------

La construcción la realizamos con la opción :code:`build`. Se usa el argumento
:code:`-t` para indicar la etiqueta que asignaremos a la imagen y :code:`-f`
para relacionar la ruta del archivo dockerfile que se usará. El siguiente
argumento no posee marca para indicarlo y corresponde al contexto, que viene a
ser la ruta donde se encuentran los archivos que usaremos (que puede ser
reemplazado por un archivo de contexto con la ruta a los distintos archivos).

.. code::

   docker build -t cosmoscalibur/ealite:latest -f dockerfile .

Ejecutar contenedor
-------------------

Ahora puedes lanzar un contenedor gráfico basado en la imagen construida con la
siguiente instrucción.

.. code::

   docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" cosmoscalibur/ealite:latest

Referencias
-----------

+ `Docker docs: Post-installation steps for Linux <https://docs.docker.com/install/linux/linux-postinstall/>`_.
+ `Docker docs: Reference documentation <https://docs.docker.com/reference/>`_.
+ `Running GUI Applications inside Docker Containers <https://medium.com/@SaravSun/running-gui-applications-inside-docker-containers-83d65c0db110>`_.
+ `Installing Enterprise Architect under Linux <https://www.sparxsystems.com/enterprise_architect_user_guide/14.0/product_information/enterprise_architect_linux.html>`_.

.. _DockerHub: https://hub.docker.com
