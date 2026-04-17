---
date: 2026-04-17
tags: windows, winget, scoop, chocolatey, software
category: tecnología, software
---

# Gestores de paquetes en Windows

Windows no ha sido históricamente el sistema operativo más amigable para
instalar paquetes de manera rápida y centralizada. Durante años, la norma fue
buscar un instalador `.exe` o `.msi` en una página web, descargarlo y seguir un
asistente de instalación. Hoy en día, sin embargo, el ecosistema ha evolucionado
y contamos con opciones robustas:
[WinGet](https://learn.microsoft.com/es-es/windows/package-manager/winget/), el
gestor oficial de Microsoft, y alternativas de la comunidad como
[Chocolatey](https://chocolatey.org/) y [Scoop](https://scoop.sh/).

```{figure} /images/gestores-de-paquetes-en-windows/terminal-powershell-scoop-winget.webp
---
alt: Terminal de PowerShell instalando paquetes con Scoop y WinGet
align: center
width: 800px
---
   Instalar *software* en Windows desde la terminal: Scoop y WinGet como
   gestores principales.
```

## Comparativa

Para sacar el máximo partido a estas herramientas, es clave entender sus
diferencias:

- Tanto WinGet como Chocolatey requieren permisos de administrador, pues
  instalan el *software* de forma global (para todos los usuarios). Scoop, en
  cambio, instala en el espacio de usuario (`~/scoop`) y no requiere privilegios
  elevados.
- Chocolatey y Scoop requieren habilitar la ejecución de *scripts* en
  PowerShell; WinGet no, al ser nativo del sistema.
- WinGet y Chocolatey incluyen *software* de terceros que puede no ser de
  código abierto, mientras que Scoop se enfoca en *software* de código abierto
  y herramientas de desarrollo.
- Scoop evita la interacción con *popups*, facilitando la instalación
  desatendida.

### ¿Cuál elegir?

- **WinGet:** Para *software* propio de Microsoft o que requiera la mejor
  integración con el sistema operativo (registros, menú de inicio, asociación
  de tipos de archivo).
- **Chocolatey:** Para *software* de terceros con amplia compatibilidad y
  catálogo:

  ```{code} powershell
  choco install <paquete>
  ```

  Sin embargo, si la mayoría de tus herramientas son de código abierto o para
  desarrollo, Chocolatey añade poco valor frente a Scoop y queda fuera de mi
  flujo habitual.
- **Scoop:** Para *software* de código abierto y herramientas de desarrollo. Se
  siente familiar si vienes de Linux o macOS.

Las herramientas que uso a diario son mayormente de código abierto y orientadas
al desarrollo, por lo que **Scoop** cubre la gran mayoría. Para el resto,
recurro a **WinGet**.

## Trabajando con Scoop

Para instalar Scoop, ejecuta en PowerShell:

```{code} powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

Scoop organiza el *software* en "buckets" (repositorios). El bucket principal
ya está disponible al instalar, pero puedes agregar otros según tus necesidades.
Algunos comandos esenciales:

```{code} powershell
# Instalar paquetes
scoop install 7zip git

# Buscar un paquete
scoop search <nombre>

# Ver lo instalado y su estado de actualización
scoop list
scoop status

# Actualizar todo
scoop update *
```

## La razón de usar WinGet también

Aunque Scoop es mi herramienta principal, hay casos puntuales donde WinGet es
la opción correcta:

- **LibreOffice:** WinGet lo registra en el sistema como alternativa para abrir
  tipos de archivo (`.odt`, `.ods`, etc.), algo que Scoop no hace al evitar
  modificar los registros globales.
- **Zed:** La auto-actualización integrada de Zed funciona correctamente cuando
  se instala con WinGet. Instalado con Scoop, Zed actualiza en la ruta habitual
  del sistema ignorando la estructura de Scoop, lo que elimina el ejecutable
  gestionado y deja el editor sin arrancar.
- **zoxide:** El propio desarrollador recomienda instalarlo con WinGet en
  Windows.

Para actualizar todo lo instalado con WinGet:

```{code} powershell
winget upgrade --all
```

## Anclar versiones (pinning)

Hay *software* que conviene no actualizar automáticamente: Teams, OneDrive,
Visual Studio Community y los redistribuibles de Visual C++ son ejemplos
típicos, pues sus actualizaciones pueden romper dependencias o entornos de
trabajo. En WinGet se usa `pin`:

```{code} powershell
# Ver paquetes anclados
winget pin list

# Anclar a la versión actual
winget pin add --id Microsoft.Teams

# Anclar a una versión específica
winget pin add --id Microsoft.Teams --version 1.2.3

# Bloquear cualquier actualización
winget pin add --id Microsoft.Teams --blocking
```

```{admonition} Nota sobre --include-pinned
---
class: note
---
Al ejecutar `winget upgrade --all`, los paquetes anclados se omiten. Para
incluirlos explícitamente, usa `winget upgrade --all --include-pinned`.
```

En Scoop, el equivalente es `hold`:

```{code} powershell
scoop hold <app>
scoop unhold <app>
```

## Tips para desarrolladores

### Modo Desarrollador de Windows

Actívalo en *Configuración > Privacidad y seguridad > Para desarrolladores*.
Esto permite que herramientas como Scoop creen enlaces simbólicos (`mklink`)
sin requerir permisos de administrador, lo que es necesario para su correcto
funcionamiento interno.

### Perfiles de PowerShell

El perfil de Windows PowerShell (v5.1) y el de PowerShell Core (v7+) se ubican
en rutas distintas:

- Windows PowerShell (v5.1):
  `%USERPROFILE%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`
- PowerShell Core (v7+):
  `%USERPROFILE%\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`

Si personalizas alias, funciones o la inicialización de herramientas como
zoxide, asegúrate de configurar ambos perfiles.

## Conclusión

Mi flujo habitual es: **Scoop** para herramientas CLI y *software* de código
abierto, y **WinGet** para aplicaciones GUI con integración de sistema o
cuando el propio proyecto lo recomienda. Chocolatey queda fuera porque Scoop
cubre todo lo que necesito en esa categoría sin los permisos adicionales que
Chocolatey requiere.

## Referencias

- [Documentación oficial de WinGet](https://learn.microsoft.com/es-es/windows/package-manager/winget/). Microsoft.
- [Scoop.sh](https://scoop.sh/). Comunidad.
- [Chocolatey Software](https://chocolatey.org/). Chocolatey Software, Inc.
- [Allow mklink for a non-admin user](https://stackoverflow.com/questions/58038683/allow-mklink-for-a-non-admin-user). Stack Overflow.
