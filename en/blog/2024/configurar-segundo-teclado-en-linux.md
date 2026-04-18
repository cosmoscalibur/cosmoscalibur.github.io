---
date: 2026-04-18
tags: linux, xinput, usb keyboard, setxkbmap, x11
category: technology, linux
language: en
---

# Configure a second keyboard in Linux

```{update} 2026-04-18
This article was originally published with instructions exclusively for X11 using `xinput` and `setxkbmap`. It has been updated to include how to do it natively in Wayland (specifically in KDE Plasma), the default graphical environment in modern distributions like Manjaro.
```

If you have a second keyboard to connect to your Linux machine, but its language layout is different, I explain how to configure it here.

It turns out that, when I joined my current job, they gave me a computer with an English keyboard as equipment. And well, what a problem getting used to the international keyboard layout to be able to type with accents or with "ñ". So I decided to buy a USB keyboard.

It turns out that configuring the keyboard language in Linux is simple, even through the graphical interface, but it has a problem: the language layout applies to all keyboards.

Yes, I am capricious, and what I was looking for was that, in case of an eventuality, if I used the original keyboard, it would work properly, but since the Spanish keyboard layout was applied, it did not have the right mapping.

## The modern method: Wayland and KDE Plasma

If you are using a modern desktop environment under Wayland, such as KDE Plasma (default in Manjaro KDE), the configuration is much simpler and does not require the terminal. Wayland manages input devices independently by design.

1. Open the **System Settings**.
2. Go to the **Input Devices** section and then to **Keyboard**.
3. In the Layouts tab, you will notice that you can configure a specific device.
4. Simply select your second USB keyboard from the list, add the desired layout (e.g. Spanish) and make sure it is assigned to that device.

And that's it! Each keyboard will work with its own layout natively.

## The traditional method: X11 (xinput and setxkbmap)

If on the other hand you are still using X11, or you have an environment that does not expose this configuration graphically, we can use the terminal. Now, let's get down to work:

### Input method

We need to know the associated input method, that is, our connected devices to input information, such as the keyboard, mouse or controllers.

For this purpose we use `xinput`. It is a utility to configure and test input methods.

```{code} bash
xinput
```

And a typical output will look like this:

```{code-block}
---
linenos:
emphasize-lines: 15
---
⎡ Virtual core pointer                      id=2  [master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer                id=4  [slave  pointer  (2)]
⎜   ↳ USB Optical Mouse                         id=9  [slave  pointer  (2)]
⎜   ↳ Elan Touchpad                             id=11  [slave  pointer  (2)]
⎜   ↳ Elan TrackPoint                           id=12  [slave  pointer  (2)]
⎜   ↳ SIGMACHIP USB Keyboard Consumer Control   id=16  [slave  pointer  (2)]
⎣ Virtual core keyboard                     id=3  [master keyboard (2)]
    ↳ Virtual core XTEST keyboard               id=5  [slave  keyboard (3)]
    ↳ Power Button                              id=6  [slave  keyboard (3)]
    ↳ Video Bus                                 id=7  [slave  keyboard (3)]
    ↳ Sleep Button                              id=8  [slave  keyboard (3)]
    ↳ Integrated Camera: Integrated C           id=10  [slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard              id=13  [slave  keyboard (3)]
    ↳ ThinkPad Extra Buttons                    id=14  [slave  keyboard (3)]
    ↳ SIGMACHIP USB Keyboard                    id=15  [slave  keyboard (3)]
    ↳ SIGMACHIP USB Keyboard Consumer Control   id=17  [slave  keyboard (3)]
    ↳ SIGMACHIP USB Keyboard System Control     id=18  [slave  keyboard (3)]
```

Well, our function will be to identify our keyboard in the list above. In my case, the keyboard corresponds to `SIGMACHIP USB Keyboard` and we see that its identifier is `id=15`.

## Language configuration

Now that we know the keyboard identifier, we can assign a specific configuration to the keyboard. For this purpose, we use `setxkbmap`, which is the utility for keyboard configuration.

The previous identifier corresponds to the `-device` argument, and the keyboard language corresponds to the `-layout` argument. It is necessary that we validate this very well, because for the same language there are variants (`-variant`). For example, in Spanish we can find variants such as Latin America, dvorak and dead keys.

In my case, since my keyboard corresponds to the Spanish keyboard without variants, the execution will be:

```{code} bash
setxkbmap -device 15 -layout es
```

Once executed, our second keyboard will have the Spanish layout, while the main keyboard will remain in English.

----

*This article was originally published in Spanish on 2024-05-19.*
