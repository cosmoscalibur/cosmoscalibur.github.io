# Configuración de Git y recomendaciones

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro

En Manjaro, disponemos de *git* instalado por defecto, pero si no estuviera
instalado sería:

```{code} bash
sudo pamac install git --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu
```{code} bash
sudo apt install git -y
```
:::
::::

Al usar KDE, tendremos instalado por defecto `ksshaskpass`, un *helper* de
credenciales con el cual podremos vincular git. De esta forma podremos evitar
la repetición de nuestras credenciales, pero además tenerlas de forma
encriptada.

Si no usas KDE, lo podemos instalar desde repositorios oficiales.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro
```{code} bash
sudo pamac install ksshaskpass --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu
```{code} bash
sudo apt install ksshaskpass -y
```
:::
::::

```{code} bash
git config --global core.askpass /usr/bin/ksshaskpass
```

Si no deseas instalar el *helper* o prefieres un archivo de texto plano sin
encriptar, puedes usar

```{code} bash
git config --global credential.helper store
```

Para relacionar *commits*, requerimos agregar la información de usuario, y lo
podemos hacer de la siguiente forma:

```{code} bash
git config --global user.email "cosmoscalibur@gmail.com"
git config --global user.name "Edward Villegas-Pulgarin"
```

A la hora de recuperar cambios de un repositorio remoto, necesitamos definir
una estrategia de manejo para nuestros cambios locales. Una forma de reducir
conflictos puede ser mover estos cambios sobre los cambios remotos, manteniendo
una historia lineal. Esto lo logramos con la siguiente configuración:

```{code} bash
git config --global pull.rebase true
git config --global merge.ff false
git config --global pull.ff true
```


https://mergiraf.org/
