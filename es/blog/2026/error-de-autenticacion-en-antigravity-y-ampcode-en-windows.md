---
date: 2026-02-21
tags: antigravity, ampcode, windows, autenticación, navegador
category: tecnología, programación
---

# Error de autenticación en Antigravity y AmpCode en Windows

Si has instalado
[Antigravity](/es/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md)
o [AmpCode](https://ampcode.com/install) en Windows 11 y te ha resultado
imposible iniciar sesión, no eres el único. Este problema de autenticación es
más común de lo que parece y las soluciones habituales no siempre funcionan. Te
cuento cómo lo solucioné.

## El problema

Al intentar iniciar sesión tanto en Antigravity como en AmpCode, el proceso de
autenticación basado en el navegador no se completa. En Antigravity, la pantalla
de inicio de sesión se queda sin respuesta o no finaliza el flujo. En AmpCode,
el enlace de autenticación que se genera en la terminal no logra completar la
autorización.

## Soluciones comunes que no funcionaron

Buscando en foros y reportes de problemas, las soluciones que se mencionan con
más frecuencia son:

### Variables de entorno `HOME` y `APPDATA`

La solución más referenciada sugiere verificar o modificar las variables de
entorno `HOME` y `APPDATA` del usuario en Windows. La idea es que estas
variables apunten correctamente a la carpeta del perfil del usuario, ya que
algunas herramientas dependen de ellas para almacenar credenciales y
configuración.

Para verificarlas, puedes abrir una terminal (PowerShell o CMD) y ejecutar:

```{code} powershell
echo $env:HOME
echo $env:APPDATA
```

### Copiar la carpeta *Local Storage*

Otra solución mencionada consiste en copiar la carpeta *Local Storage* de una
instalación exitosa (por ejemplo, de otro equipo o de otra sesión de usuario) al
directorio de configuración de Antigravity o AmpCode. Si bien puede funcionar
como un parche temporal, no es una solución sostenible y no aborda la causa
raíz.

### Chrome no detectado

Algunos reportes mencionan que el problema se relaciona con que Chrome no es
detectado por la herramienta, pero no ofrecen una solución clara más allá de
señalar el síntoma.

## La solución: cambiar el navegador predeterminado a Chrome

Ninguna de las soluciones anteriores funcionó en mi caso. Mi navegador
predeterminado era Firefox, y tras agotar las opciones, probé algo simple:
**cambiar el navegador predeterminado a Google Chrome**.

Para cambiar el navegador predeterminado en Windows 11:

1. Abre **Configuración** ({kbd}`Win+I`).
2. Ve a **Aplicaciones** > **Aplicaciones predeterminadas**.
3. Busca **Google Chrome** en la lista.
4. Haz clic en **Establecer como predeterminado**.

Tras realizar este cambio, tanto la autenticación de Antigravity como la de
AmpCode funcionaron perfectamente. El flujo de inicio de sesión en Antigravity
se completó sin problemas, y el enlace de autenticación de AmpCode en la
terminal abrió correctamente el navegador y finalizó la autorización.

## ¿Por qué funciona?

El flujo de autenticación OAuth de estas herramientas abre una URL en el
navegador predeterminado del sistema. Aunque Firefox es un navegador compatible,
el flujo de redirección (*callback*) parece depender de una integración
específica con Chrome (o navegadores basados en Chromium). Al ser estas
herramientas parte del ecosistema de Google o al depender de su infraestructura
de autenticación, la integración con Chrome es más robusta.

## Conclusión

Si estás en Windows 11 con Firefox como navegador predeterminado y no logras
autenticarte en Antigravity o AmpCode, prueba cambiar el navegador
predeterminado a Chrome. Es una solución simple que puede ahorrarte horas de
frustración con variables de entorno y parches manuales.

## Referencias

- [Antigravity](https://antigravity.google/download). Google DeepMind.
- [AmpCode](https://ampcode.com/install). Sourcegraph.
