Con permisos de administrador, ejecutamos en la consola

```{code-block} bash
---
name: install-vm-kvm
caption: Instalación de QEMU, KVM y Virt Manager para la gestión de máquinas virtuales
linenos:
---
sudo apt install qemu-kvm qemu-guest-agent \
  libvirt-daemon-system libvirt-clients \
  bridge-utils virt-manager
sudo adduser $USER libvirt
sudo adduser $USER kvm
```

Debemos cerrar sesión y volver a hacer ingreso con el fin de reconocer los
permisos del grupo de `libvirt`.

## Referencias

[Setting Up Virtual Machines with QEMU, KVM, and Virt-Manager on Debian/Ubuntu](https://linuxconfig.org/setting-up-virtual-machines-with-qemu-kvm-and-virt-manager-on-debian-ubuntu)

[Issue with Virt-manager](https://askubuntu.com/questions/318702/issue-with-virt-manager)

linux612-virtualbox-host-modules virtualbox-guest-iso virtualbox
