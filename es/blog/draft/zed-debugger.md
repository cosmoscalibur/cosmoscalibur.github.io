# Depurando Python con Zed Debugger

- Instalar `gdb`
- `debugpy` se instala automático en el ambiente.

Para poder tener acceso a la traza de un proceso en ejecución con gdb es
necesario asignar la capacidad de inspección y modificación.

```
sudo setcap CAP_SYS_PTRACE=+eip /usr/bin/gdb
```

## Referencias

- [Solving `ptrace: Operation not permitted.` for GDB](https://hychiang.info/blog/2024/ptrace-not-permitted/)
- [How to solve "ptrace operation not permitted" when trying to attach GDB to a process?](https://stackoverflow.com/a/61874261)
