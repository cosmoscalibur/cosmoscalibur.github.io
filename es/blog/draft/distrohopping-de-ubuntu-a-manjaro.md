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
