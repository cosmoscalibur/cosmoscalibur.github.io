---
date: 2024-12-07
tags: manjaro, ubuntu, wifi, linux
category: technology, linux
language: en
---

# Wi-Fi issues in Linux

If Wi-Fi starts to disconnect randomly and upon reviewing the list of networks,
these have disappeared, there are some points to consider evaluating.

- [Disable "fast boot" de la BIOS](https://bbs.archlinux.org/viewtopic.php?pid=2134101#p2134101):
  In Ubuntu, it doesn't seem to be a current issue (it didn't happen on this
  same machine with that configuration before, but there are older posts related
  to Ubuntu about this), but when moving to Manjaro or derivatives of Arch, this
  is a replicable problem. Make sure to disable 'Fast boot' in the BIOS.

- [Deisable Wi-Fi power saving](https://forum.manjaro.org/t/wifi-random-disconnects-after-update/142876/3):
  It's common that the power-saving mode of the Wi-Fi card causes us to stop
  seeing available connections. Therefore, it's necessary to create a
  configuration file that disables this feature and we have to restart.

  You need to create the file as an administrator.

  ```{code} text
  ## File: /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  [connection]
  wifi.powersave = 2
  ```

These two adjustments were sufficient in my scenario, but it wasn't clear that
they should be both applied together. This was a mix of testing different
solutions that reported success and testing the effects of combining them. For
example, when I disabled "*fast boot*", I would always connect from the start,
but the networks would disappear after a short while. If I only disabled
power-saving alone, the networks would remain connected, but I would never get
connected in the first place. It was only when both were enabled together that
it worked.

To provide context to my specific case, I'm running Manjaro KDE 24.1 with kernel
6.11. The network card is *Realtek*, and the equipment is an ASUS TUF Gaming A15
FA506IV.

Also, they often report that
[disabling MAC address randomization](https://forum.manjaro.org/t/wifi-not-connecting-at-start-up/113193/3)
helps, but in my case, this test had no effect.

```{code} text
## File: /etc/NetworkManager/conf.d/wifi_rand_mac.conf
[device]
wifi.scan-rand-mac-address=no
```

## Diagnostic Information

One of the key points to find when trying to solve your problems is to know
information about your hardware and drivers.

**Getting General System Information**

For this specific issue, it can be useful to look at the *Network* and *System*
sections, but don't cut off the results if you post them on a forum. These
utilities are not only helpful when the error is related to Wi-Fi, but also
provide valuable information for other hardware problems.

```{code} bash
inxi --full --admin --filter --width
```

**Getting Driver Information**

At this point, we can detail the driver and its version, looking for mentions of
"Network".

`````{tab-set}
````{tab-item} Manjaro

```{code} bash
sudo mhwd -l -li
```

````
````{tab-item} Ubuntu

```{code} bash
sudo lshw
```

````
`````

We can search for kernel diagnostic messages associated with the driver. Keep in
mind the driver from the *Network* section of `inxi`. In my case, it's `r8169`
and `rtw_8822ce`.

```{code} bash
sudo dmesg | grep r8169
sudo dmesg | grep rtw_8822ce
```
