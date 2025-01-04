---
date: 2024-12-18
tags: manjaro, wayland, x11, zed, hybrid graphics, nvidia, radeon, vulkan, gpu, graphics card
category: technology, linux
language: en
---

# Wayland and Hybrid Graphics Issues in Linux

[Hybrid graphics cards](https://wiki.archlinux.org/title/Hybrid_graphics) are a
strategy used by modern computers to incorporate two graphics cards: one
integrated and one dedicated, with different capabilities and energy
consumption. The idea is not to use the dedicated card unless necessary for 3D
rendering. However, this is not a resolved issue in Linux and affects native
applications running on Wayland, which is the new and modern protocol for
server-side graphics communication used by window compositors in Linux
(replacing X11), that utilize Vulkan.

One of these affected applications is the code editor Zed. At the time of
writing this entry, the NVIDIA controller version is 550.135 in the stable
branch of Manjaro.

## Symptoms of the Problem

### Case of Zed

Considering the example of the {program}`zed` editor, we will see for a brief
moment that an attempt is made to launch a window on Wayland, but it closes
after a few seconds. We can delve deeper into this issue and test it in the
terminal by running `zed --foreground`, which reveals the error message
`` "payload": "called `Result::unwrap()`on an`Err` value: ERROR_INITIALIZATION_FAILED" ``.

If you are also experiencing this problem, you can contribute to the Zed project
by providing useful information. Reporting the output of `vulkaninfo` and
`RUST_LOG=blade_graphics=debug zed --foreground`, with additional details such
as what we see to understand if the issue is closer to Vulkan/Wayland or Zed
itself.

Please refer to the GitHub report
[zed/8168](https://github.com/zed-industries/zed/issues/8168).

### Case of VkCube (demo)

It turns out that Vulkan has demo applications for X11 and Wayland, `vkcube` and
`vkcube-wayland`, which are available in the `vulkan-tools` package. The
expected outcome is that if these demos work on X11, they should at least work
on platforms supported by Zed (and other Vulkan-based applications).

In my case, `vkcube` works without issues, but Zed on X11 at least opens once
during the session. However, `vkcube-wayland` reports a
`segmentation fault (core dumped)`, which suggests that native Wayland
applications with Vulkan are not working properly.

This is likely to be true for hybrid cases because in my observation of Zed and
Vulkan reports, the issue does not occur on systems with only integrated
graphics card or only NVIDIA graphics. In contrast, the reported cases with only
integrated GPUs were solvable by installing the correct Vulkan driver, which
suggests that there's a dependency on NVIDIA for hybrid cases.

On Kubuntu 24.10 (which I tried recently), Zed works perfectly in Wayland, but
it requires an NVIDIA controller from the 560 series (although I understand this
might change).

## Check if you have Hybrid Graphics

To determine if your case is related to hybrid graphics, you can review the
output of the following instructions:

```{code-block} bash
---
caption: VGA Compatible Device Compatibility Check (any Linux distribution)
---
❯ lspci | grep VGA
01:00.0 VGA compatible controller: NVIDIA Corporation TU106M [GeForce RTX 2060 Mobile] (rev a1)
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir [Radeon Vega Series / Radeon Vega Mobile Series] (rev f0)
```

```{code-block} bash
---
caption: Manjaro hardware detection.
---
❯ mhwd -li
> Installed PCI configs:
--------------------------------------------------------------------------------
                  NAME               VERSION          FREEDRIVER           TYPE
--------------------------------------------------------------------------------
           video-linux            2024.05.06                true            PCI
video-hybrid-amd-nvidia-prime            2023.03.23               false            PC
```

In both cases, you should be able to see the availability of an NVIDIA graphics
card and/or an AMD (or possibly Intel) graphics card. This could be a
contributing factor to your issue.

## Checking the NVIDIA Driver Version

If you're not aware of the NVIDIA driver version, you can use your package
manager to check it:

- Use `pamac info nvidia-utils` (for Manjaro-based systems) or
  `apt show nvidia-utils` (for Ubuntu-based systems) to verify the version of
  the `nvidia-utils` package (see
  [package manager commands](#pamac-commands-en)).
- Alternatively, run `{program}` `nvidia-smi`, and you'll see the driver version
  in the first row, labeled as "Driver version".

This information can help you determine if there are any compatibility issues
with your system's NVIDIA driver.

## Workaround

We want to be able to use our favorite applications, such as Zed, which is a
must for me. Regarding some Wayland issues on Manjaro related to the NVIDIA
graphics card, I've seen that the recommended solution is to wait for the 560
series, but this is still in the unstable branch.

In the meantime, we can
[explicitly tell the Vulkan driver](https://vulkan.lunarg.com/doc/view/1.3.250.1/windows/LoaderDriverInterface.html#overriding-the-default-driver-discovery)
to use the integrated card's configuration by setting it to use the default
drivers. The configuration files are available in the `/usr/share/vulkan/icd.d/`
directory. If you have an AMD card, these will be the ones with `radeon`, and
for Intel, they'll be marked as `intel`.

This is done by assigning the list of files to the
[`VK_DRIVER_FILES` environment variable](https://wiki.archlinux.org/title/Vulkan#NVIDIA_-_vulkan_is_not_working_and_can_not_initialize).
In my case, it would be:

```{code} bash
export VK_DRIVER_FILES=/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json
```

Once you've made this change, you can try running {program}`vkcube-wayland` or
{program}`zed` again to see if it works. If it does, you can make this change
permanent by adding the following line to your system's {file}`/etc/environment`
file:

```{code} bash
sudo echo 'VK_DRIVER_FILES=/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json' >> /etc/environment
```

This change also fixes the issue where subsequent windows appear to leave an
invisible window in X11.

## Definitive fix

When the 560 series becomes available, I'll report back on whether this resolves
the problem in Manjaro. For now, it's necessary to remove the previous line from
the environment variables.

To execute something directly with the NVIDIA card, we need to use
{program}`prime-run`, which doesn't currently make a difference.

If you want to test without making any changes, you can simply unset the
`VK_DRIVER_FILES` variable using the command `unset VK_DRIVER_FILES`.
