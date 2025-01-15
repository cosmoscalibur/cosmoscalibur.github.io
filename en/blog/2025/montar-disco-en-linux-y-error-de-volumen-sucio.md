---
date: 2025-01-10
tags: manjaro, ubuntu, linux, disk, mount, lsblk, dmesg
category: technology, linux
language: en
---

# Mounting a disk in Linux and dirty volume error

I hadn't used my external hard drive for some time, which was formatted as NTFS,
and when I went to use it (mount it) after updating the operating system, an
error about a dirty volume appeared. If you've encountered this too, here's how
to solve it.

## Mounting a disk in Linux

To mount our disk from the command line in Linux, we first need to find out
where it is located. We do this by using `lsblk`.

The output will look similar to what's shown below. External devices (hard
drive, USB, etc.), are appended to the {file}`/dev/sdX*` points, where `X` is a
letter and `*` is a number. In this case, our external hard drive is recognized
as {file}`/dev/sda1`. Note that these points always start with the {file}`/dev/`
path.

```{code}
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 931,5G  0 disk
└─sda1        8:1    0 931,5G  0 part
nvme0n1     259:0    0 953,9G  0 disk
├─nvme0n1p1 259:1    0   300M  0 part /boot/efi
└─nvme0n1p2 259:2    0 953,6G  0 part /
```

We need a directory to mount the unit, so we'll create a new one (or use an
existing one if you have it).

```{code}
mkdir -p ~/media/eddisk
```

Now we'll mount the disk.

```{code}
sudo mount -t ntfs-3g /dev/sda1 ~/media/eddisk
```

If everything is okay, we now have access to the available disk in that
directory.

## Dirty Volume Error

The story in my case is that not everything was okay - the automatic mounting
and manual mounting via command line wouldn't work. A curious thing is that the
mounting with the file manager (in my case, {program}`dolphin`, since I use KDE
as my desktop environment) worked correctly. It seems that this error can occur
when using the disk in Windows with *fast boot* enabled.

The error message we'll see will be:

> wrong fs type, bad option, bad superblock on /dev/sda1, missing codepage or
> helper program, or other error. dmesg(1) may have more information after
> failed mount system call.

Upon inspecting with the suggestion of the error message, I ran the command
`sudo dmesg`.

```{code}
[ 1662.331363]  sda: sda1
[ 1662.331822] sd 2:0:0:0: [sda] Attached SCSI disk
[ 1665.785708] ntfs3(sda1): It is recommened to use chkdsk.
[ 1665.834695] ntfs3(sda1): volume is dirty and "force" flag is not set!
```

This tells us that we are presenting an error of a dirty volume, and we can
solve it by executing:

```{code}
sudo ntfsfix -d /dev/sda1
```

## Referencias

- ArchLinux Wiki.
  [NTFS - Unable to mount with ntfs3 with partition marked dirty](https://wiki.archlinux.org/title/NTFS#Unable_to_mount_with_ntfs3_with_partition_marked_dirty)
- AskUbuntu.
  [ntfs external hard drive does not mount](https://askubuntu.com/questions/1513180/ntfs-external-hard-drive-does-not-mount)
- AskUbuntu.
  [How to correctly fix a "dirty" NTFS partition without using chkdsk](https://askubuntu.com/questions/112150/how-to-correctly-fix-a-dirty-ntfs-partition-without-using-chkdsk)
