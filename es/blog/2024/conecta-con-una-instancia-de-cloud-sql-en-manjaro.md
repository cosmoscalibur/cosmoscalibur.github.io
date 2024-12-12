---
date: 2024-12-10
tags: manjaro, ubuntu, google cloud sdk, cloud sql proxy, base de datos
category: tecnología, linux
---

# Conecta con una instancia de Cloud SQL en Manjaro

Aprovechando que estoy en reinstalación por la
[transición de (X/K)ubuntu a Manjaro](/es/blog/2024/que-hacer-despues-de-instalar-manjaro.md),
les contaré sobre como conectar a una instancia de Cloud SQL en Manjaro.

## Google Cloud SDK

### Instalación de Google Cloud SDK

Para la gestión de elementos de infraestructura, lo cual incluye la conexión a
la base de datos, se requiere disponer de *Google Cloud SDK*. El proceso de
instalación depende del sistema operativo, y ante inquietudes, siempre puedes
remitirte a la [documentación oficial](https://cloud.google.com/sdk/docs/install).

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

Este paquete está disponible en el AUR, por lo cual se puede usar en Arch.

```{code} bash
pamac build google-cloud-cli --no-confirm
```

```{hint}
Si no detecta el binario, puedes reiniciar cerrar y abrir la terminal. En mi
caso solo me funcionó de esta forma, ni con {program}`source` de
{file}`~/.zshrc` ni {file}`~/.bashrc` funcionó. A pesar de esto, era detectado
por {program}`whereis` y {program}`which`.
```

:::
:::{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get install apt-transport-https ca-certificates gnupg
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt update -q
sudo apt install -y google-cloud-sdk
```
:::
::::

### Autenticación Google Cloud SDK

Una vez se ha instalado, debemos autenticarnos para la gestión de proyectos y
para el manejo de credenciales de aplicaciones. Si usas más de un navegador y
separas tu perfil personal y laboral según el navegador, o usas múltiple perfil
en el navegador, o incluso si es un escritorio remoto o un contenedor usado
desde Windows y no puedes usar el navegador, recomiendo que la autenticación la
gestiones copiando y pegando manualmente el enlace de autenticación
(`--no-launch-browser`). Ambas autenticaciones requieren validar en navegador.

```{code-block} bash
:name: cloud-sdk-auth
:emphasize-lines: 2

gcloud init --no-launch-browser
gcloud auth application-default login --no-launch-browser
```

## Cloud SQL Proxy

### Instalación de Cloud SQL Proxy

Con el fin de crear el proxy de la conexión a la base de datos, en caso de
requerir funciones de consulta y no de administración general, debemos tener
*Cloud SQL Proxy*. Para mayor detalle puedes remitirte a la
[documentación oficial](https://cloud.google.com/sql/docs/mysql/sql-proxy).

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro
```{code} bash
pamac build cloud-sql-proxy
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu
```{code} bash
curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.14.1/cloud-sql-proxy.linux.amd64
chmod +x cloud-sql-proxy
```

Este método válido para cualquier distribución Linux, dejará fijada la versión.
:::
::::

### Iniciar Cloud SQL Proxy

Con el fin de crear la conexión a la instancia de base de datos, debemos
iniciar el *proxy* de la siguiente forma:

```{code} bash
cloud-sql-proxy <NOMBRE DE INSTANCIA> -p <PUERTO>
```

Esto nos habilitará el acceso por `127.0.0.1:<PUERTO>`.

:::{error}

```{code}
2024/12/10 16:36:44 Authorizing with Application Default Credentials
2024/12/10 16:36:44 Error starting proxy: error initializing dialer: failed to create default credentials: google: could not find default credentials. See https://cloud.google.com/docs/authentication/external/set-up-adc for more information
2024/12/10 16:36:44 The proxy has encountered a terminal error: unable to start: error initializing dialer: failed to create default credentials: google: could not find default credentials. See https://cloud.google.com/docs/authentication/external/set-up-adc for more information
```

Este error corresponde a la necesidad de aplicar la autenticación de
credenciales por defecto de aplicación que se describe
[previamente](#cloud-sdk-auth).
:::

## Conectar a la base de datos

En Tributi usamos MySQL, y auqnue comencé usando {program}`MySQL Workbench`,
este no era muy cómodo y mis compañeros usaban {program}`Dbeaver`. Este me
pareció interesante y fue el que estuve usando hasta que conocí
{program}`DbGate`. Estos dos se encuentran disponibles como *flatpak*.

```{code} bash
flatpak install -y flathub org.dbgate.DbGate  # Verificado
flatpak install -y flathub io.dbeaver.DBeaverCommunity  # No verificado
```

Un punto extra para no usar {program}`MySQL Workbench` es usar no solo un
cliente moderno, sino también con soporte para múltiples bases de datos (no
solo *MySQL*).

:::{hint}
En el pasado, he tenido conflictos con el uso de `localhost` como asignación
del *host* en los clientes, y esto es que no siempre debe resolverse como
`127.0.0.1`, por lo cual es mejor usar siempre en la configuración la IP.
:::
