Hace poco decidí realizar este nuevo salto de distribución Linux, y he pasado
de Xubuntu 22.10 (con una pequeña transición por Kubuntu 24.10) a Manjaro KDE
24.1.

Debo decir que, en la corta transición por Kubuntu, me ha encantado KDE y por
eso al pasar a Manjaro, he decido usar esta variante. Respecto a porqué
Manjaro, quería poder usar paquetes con versiones más actualizadas e
instalaciones más simples (en Ubuntu muchos paquetes que quiero usar o probar
ni siquiera están disponibles).

Versiones recientes, nuevos paquetes y disponer a voluntar de snap y no por
defecto. Esto último me ha afectado en que algunas utilidades de los paquetes no
se exponen en sus versiones snap, ejemplo, en Firefox, la opción de instalar
extensiones por línea de comandos no es posible.

git, curl, pkgconfig y ca-certificates vienen por defecto al ser requeridos por
pamac. flatpak viene instalado por defecto. El equivalente de PPA es AUR, y es
natural su gestión con pamac ya soportada, solo hay que agregar `-a` en las
búsquedas o `build` en lugar de `install` para la instalación.

La nueva revolución del ecosistema de Rust se encuentra disponible sin
dificultad en el repositorio oficial o en el AUR, mientras que en Ubuntu y
derivados en caso de estar algunos, sus versiones no se actualizan rápidamente,
y muchos es necesario instalarlos con binarios suministrados directamente por el
proyecto o por compilación con `cargo`.
