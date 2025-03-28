# Gestores de paquetes en Windows

Windows no ha sido muy popular en el pasado para instalar paquetes de manera
fácil y rápida. Sin embargo, con el tiempo, han aparecido varias opciones para
hacerlo,
[WinGet](https://learn.microsoft.com/es-es/windows/package-manager/winget/) que
es el gestor de paquetes oficial de Microsoft, y otras opciones como
[Chocolatey](https://chocolatey.org/) y [Scoop](https://scoop.sh/), que son
gestores de paquetes populares.

Para tomar la máxima ventaja de estos gestores de paquetes, es importante
entender cómo funcionan y cuáles son sus ventajas y desventajas. Además, es
importante tener en cuenta que cada gestor de paquetes tiene sus propias
características y requisitos, por lo que es importante elegir el que mejor se
adapte a tus necesidades.

Tanto WinGet como Chocolatey requieren permisos de administrador para instalar
paquetes ya que son instalados de manera global (instalados para todos los
usuarios), mientras que Scoop no lo requiere al instalar los paquetes en el
espacio de usuario. Chocolatey y Scoop requieren habilitar la ejecución de
scripts en PowerShell, lo que no es necesario para WinGet por ser nativo. Winget
y Chocolatey incluyen software de terceros que pueden no ser de código abierto,
mientras que Scoop se enfoca en software de código abierto (y herramientas de
desarrollo). Otra diferencia es que Scoop evita la interacción con _popups_ por
lo que facilita la instalación de paquetes sin interacción adicional.

Recomendaciones sobre la elección del gestor de paquetes pueden ser:

- Si requieres software propio de Microsoft, se puede tener una mejor
  integración con WinGet.
- Si requieres software de terceros, se puede tener mejor compatibilidad y
  oferta con Chocolatey.
- Si requieres software de código abierto o herramientas de desarrollo, o eres
  más familiar con los gestores de paquetes de Linux, se puede tener una mayor
  oferta y familiaridad con Scoop.

Con las herramientas que suelo usar y lo que veo disponible de forma oficial en
muchas de ellas, prefiero Scoop (son de código abierto y para desarrollo, en su
mayoría).

## Instalar Scoop en Windows

```{code} powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

## Agregar repositorios a Scoop

## Instalar paquetes con Scoop

```{code} powershell
scoop install 7zip git
```

## Otras opciones de Scoop

- list
- search
