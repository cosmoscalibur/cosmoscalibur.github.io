---
date: 2024-12-10
tags: manjaro, ubuntu, google cloud sdk, cloud sql proxy, database
category: technology, linux
language: en
---

# Connecting to a Cloud SQL instance on Manjaro

Since I'm currently in a full system installation process following
[the transition from (X/K)Ubuntu to Manjaro](/en/blog/2024/que-hacer-despues-de-instalar-manjaro.md),
I'll explain how to connect to a Cloud SQL instance on Manjaro.

## Google Cloud SDK

### Installation of Google Cloud SDK

To manage infrastructure elements, including database connections, you need to
have *Google Cloud SDK* installed. The installation process depends on the
operating system, and if you have any doubts, you can refer to the
[official documentation](https://cloud.google.com/sdk/docs/install).

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

This package is available in the AUR (Arch User Repository), so it can be used
on Arch.

```{code} bash
pamac build google-cloud-cli --no-confirm
```

```{hint}
If it doesn't detect the binary, you can try restarting and closing, then
opening the terminal again. In my case, only this worked for me. Neither using
{command}`source` of {file}`~/.zshrc` nor {file}`~/.bashrc` worked either,
despite that it was detected by {command}`whereis` and {command}`which`.
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get install apt-transport-https ca-certificates gnupg
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt update -q
sudo apt install -y google-cloud-sdk
```
````
`````

### Google Cloud SDK Authentication

Once installed, we need to authenticate in order to manage projects and handle
application credentials. If you use multiple browsers and separate your personal
and professional profiles according to the browser, or use multiple profiles in
the browser, or even if it's a remote desktop or a container used from Windows
and can't use the browser, I recommend managing authentication by manually
copying and pasting the authentication link (`--no-launch-browser`). Both
authentication methods require validation in a browser.

```{code-block} bash
---
name: cloud-sdk-auth
emphasize-lines: 2
---
gcloud init --no-launch-browser
gcloud auth application-default login --no-launch-browser
```

## Cloud SQL Proxy

### Instalación de Cloud SQL Proxy

In order to create the proxy for database connection, in cases where we need
query functions and not general administration functions, we must have *Cloud
SQL Proxy*. For more detail, you can refer to the
[official documentation](https://cloud.google.com/sql/docs/mysql/sql-proxy).

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code} bash
pamac build cloud-sql-proxy
```

````
````{tab-item} Ubuntu
:sync: ubuntu

```{code} bash
curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.14.1/cloud-sql-proxy.linux.amd64
chmod +x cloud-sql-proxy
```

This approach is universal across Linux distributions and will keep the version
static.
````
`````

### Start Cloud SQL Proxy

With the aim of creating a connection to the database instance, we must start
the proxy in the following way:

```{code} bash
cloud-sql-proxy <INSTANCE NAME> -p <PORT>
```

Esto nos habilitará el acceso por `127.0.0.1:<PORT>`.

````{error}

```{code}
2024/12/10 16:36:44 Authorizing with Application Default Credentials
2024/12/10 16:36:44 Error starting proxy: error initializing dialer: failed to create default credentials: google: could not find default credentials. See https://cloud.google.com/docs/authentication/external/set-up-adc for more information
2024/12/10 16:36:44 The proxy has encountered a terminal error: unable to start: error initializing dialer: failed to create default credentials: google: could not find default credentials. See https://cloud.google.com/docs/authentication/external/set-up-adc for more information
```

This error corresponds to the need to apply the default authentication for
application credentials, which is described previously in
[Cloud SDK Authentication](#cloud-sdk-auth).
````

## Connecting to database

In my work, we use MySQL, and although I initially used *MySQL Workbench*, it
wasn't very comfortable and my colleagues were using
[{program}`dbeaver`](https://dbeaver.io/). This caught my attention and was the
one I was using until I discovered [{program}`dbgate`](https://dbgate.org/).

These two are available as *flatpak* so that they can be installed comfortably
on any Linux distribution, but the particular case of `{program}`dbeaver\` does
not look well on Wayland when installed in this way, making it more preferred to
install from the official repository.

`````{tab-set}
````{tab-item} Manjaro
:sync: manjaro

```{code} bash
sudo pamac install dbeaver --no-confirm
sudo pamac install dbeaver-plugin-office dbeaver-plugin-svg-format --as-deps --no-confirm
pamac build dbgate-bin
```

````
````{tab-item} Flatpak
:sync: ubuntu

```{code} bash
flatpak install -y flathub org.dbgate.DbGate  # Verificado
flatpak install -y flathub io.dbeaver.DBeaverCommunity  # No verificado
```
````
`````

An additional point for not using {program}`MySQL Workbench` is that it doesn't
just offer a modern client, but also comes with support for multiple databases
(not just *MySQL*).

```{hint}
In the past, I have had conflicts with using `localhost` as an assignment for
the *host* in clients, and that's why it's not always resolved as `127.0.0.1`.
That's why it's better to use the IP address consistently in the configuration.
```
