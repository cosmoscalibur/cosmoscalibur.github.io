---
date: 2024-10-20
tags: ffmpeg, bash
category: technology, linux
language: en
---

# Merging Video and Audio with FFmpeg and Bash

Recently, my girlfriend asked me to help her download the videos of a course
before access to the account expired, and it involved downloading videos from
Vimeo. However, the download trick for these videos requires combining the audio
and video later, so I'll explain how to do this using FFMPEG and Bash.

## Downloading a Video from Vimeo

Well, this is the initial point of our adventure, and it's how to download a
video from Vimeo through a site with authentication. Since going directly to
Vimeo would be enough with the extraction using
[yt-dlp](https://github.com/yt-dlp/yt-dlp), we run into trouble because the
Vimeo video is embedded in another site, making it impossible to proceed (or at
least I couldn't find a way to do so, as an error message about unrecognized
portal was displayed).

After continuing our search, we found that the only option available was a
Chrome extension called
[Free Vimeo Downloader](https://chromewebstore.google.com/detail/free-vimeo-downloader/migiikaijhclkmlpnnficpopgmcpgia?hl=es-419),
which enables us to download videos from Vimeo embedded in any portal. It offers
the option to download videos in different qualities, but be aware that audio is
downloaded separately, and you'll need to start playback first to download it.

```{attention}
To proceed with the download, it's essential to **reproduce** the video first,
as this will allow you to access the audio and initiate its separate download.
```

The downloaded files have a pattern where the video file name is followed by the
video quality, and in the case of the audio file, it is followed by `-audio`,
both in MP4 format.

Now, how do we merge the video and audio?

## Processing with FFmpeg

Now, the task associated with processing to merge the audio files with the video
files will be delegated to [FFmpeg](https://ffmpeg.org/download.html), a
powerful command-line utility for audio and video processing that is free and
open-source.

If you use Debian/Ubuntu or any derivative, like I do, you can install it as
follows. If not, you can refer to the official website or also install it with
the package manager {program}`conda` (applies to all operating systems).

`````{tab-set}
````{tab-item} Ubuntu
```{code} bash
sudo apt install -y ffmpeg
```
````
````{tab-item} Manjaro
```{code} bash
sudo pamac install --no-confirm ffmpeg
```
````
`````

To test the concept, we will use one of the video and audio file pairs.

```{code} bash
ffmpeg -i Modulo\ 2\ Clase\ 2\ Parte\ 5\ \(720p\ with\ 30fps\).mp4 -i Modulo\ 2\ Clase\ 2\ Parte\ 5-audio.mp4 -c copy output/Modulo\ 2\ Clase\ 2\ Parte\ 5.mp4
```

As the audio and video are already in the same format and codec, there is no
need to apply transformations using FFmpeg. We only need to use FFmpeg to
maintain the video channel from the first file and copy the audio channel from
the second file, generating a new multimedia file.

We observe the `-i` parameter that we use to indicate a source file, whether it
be audio, video, or even images and text files. In this case, we are using it to
indicate the video file and the audio file we want to match (each file should be
preceded by `-i`).

If it were necessary to apply a codec to these files, we would specify the
respective option after the path of each file. In this case, it does not
interest us, which helps FFmpeg to execute more quickly. Therefore, we simply
indicate after the second file `-c copy` to indicate that it is copied directly,
preserving the original quality and format.

```{hint}
FFmpeg and its documentation can be a bit challenging for someone not familiar
with the command line. If you have doubts about where to start, I recommend
visiting the following resource:
[ffmprovisr](https://amiaopensource.github.io/ffmprovisr/).
```

We can open the video file, and we will see the video with the audio included.
And now, what happens if there are 56 videos along with their 56 corresponding
audio files?

## Batch Processing with Bash

Since the files have a pattern in their names and can be listed in order, and
the process executed on each pair is the same, we can create a routine for this
batch processing. This will help avoid potential errors such as omitting a file
pair, mixing a video with another video's audio, or typing errors.

We need to store separate lists of the video and audio files. We will iterate
over the total number of videos in general terms and move forward in both lists,
which are ordered and have a name pattern starting with the video's general
name, allowing us to match them.

Then, cyclically, we obtain these pairs, with which we form names for `-i`
parameter in {program}`ffmpeg`, and the assignment of the output path.

We will do this in _Bash_ (this is for Linux users, but if you use Windows, I
invite you to replicate it in PowerShell or your favorite language).

```{code-block} bash
---
name: bash-ffmpeg-unir
caption: *Bash* code to merge a set of video and audio files with FFMPEG.
linenos:
---
#! /usr/bin/bash

OUTPUT=output
mkdir -p $OUTPUT
AUDIO_LIST=(*audio.mp4)
VIDEO_LIST=(*fps*.mp4)
LEN=${#AUDIO_LIST[*]}
echo "$LEN videos"
for ((i = 0; i < LEN; i++)); do
    echo "Procesando video: $((i + 1))"
    VIDEO_NAME="${VIDEO_LIST[$i]}"
    ffmpeg -i "$VIDEO_NAME" -i "${AUDIO_LIST[$i]}" -c copy "$OUTPUT/$VIDEO_NAME"
done
```

I will explain each part of the code..

In line 1, we use a shebang (`#!/bin/bash`) to indicate the path of the shell
interpreter. In this case, it's `bash`.

On line 3, we assign the name of the output directory. This will be used to
create the directory in line 4 and to form the complete output path in line 12.

On line 4, we use `$` to expand the result of a command or variable. Here, we
are using `mkdir -p`, which creates a directory and its parents if they do not
already exist.

To get the list of files, we could use `ls`, but for converting to an array, we
need to adjust the `IFS` (Internal Field Separator). However, using direct file
name expansion is simpler and more straightforward as shown in lines 4 and 5.

In Bash, we refer to an array using `${ }`. For example, to access a specific
element (`${ARR[0]}`), as used in lines 11 and 12. To access all elements of the
array (`${ARR[*]}` or `${ARR[@]}`), or for counting purposes with `#` before the
array name (as used in line 7).

We use the `echo` command to print messages to the terminal. The message is
enclosed in double quotes (`"`) to prevent expansion of the result beyond that
point.

In lines 9 and 10, we see the use of double parentheses `(())`, which allows
arithmetic expansion. For any arithmetic operations, we always use double
parentheses.

Line 9 is the start of a Bash `for` loop that uses arithmetic expansion to
assign the initial value to the variable for iterating over the lists. The loop
condition checks whether it is less than the length of the list, and then
increments by one to move to the next element. After the `do` keyword, we have
the block of code that will be repeated, depending on our loop variable (`i`).
Finally, closes the loop with `done`.

Save the file with `.sh` extension, and run with `bash`, `source` or `. `.

```{code} bash
bash merge_video.sh
. merge_video.sh
source merge_video.sh
```

The last two options are the reason for using the shebang in line 1 to
distinguish the shell to be used.

```{hint}
Here are three resources that I recommend for Bash:

- [Explain Shell](https://explainshell.com/).
- [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls).
- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html)
  and [BASH Programming - Introduction HOW-TO](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html):
  from The Linux Documentation Project, *TLDP*.
```
