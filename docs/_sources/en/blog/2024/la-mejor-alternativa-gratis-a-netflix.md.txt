---
date: 2024-10-21
tags: netflix, disney plus, prime video, apple tv, stremio, torrentio, torrents, pluto tv, watch free movies, watch free series, popcorn time
category: entertainment, linux
language: en
---

# The Best Free Netflix Alternative

Tired of streaming subscriptions draining your wallet? Perhaps not, but I'll
share a trick to comfortably, safely, and freely access a lot of content. I'll
be talking about Stremio and an extension that pulls content from torrents.

## Stremio

[Stremio](https://www.stremio.com/) is a multimedia content aggregator that
allows you to search for providers to play the content you're interested in.
This provider search is done through an extension system for different services
(you can link your streaming accounts like Netflix, Disney+, Prime Video, Apple
TV) to have everything unified in a single multimedia hub. Because it's based on
extensions, you can also get extensions to play content from torrent indexes,
giving you access to free and safe content. It's also available for Linux, Mac,
Windows,
[Android](https://play.google.com/store/apps/details?id=com.stremio.one&hl=es_CO),
and even [Web](https://web.stremio.com/).

While Stremio can run without an account, creating one is important. This allows
you to synchronize not only what you watch, your watchlists, and progress, but
also installed extensions. This is key for using Stremio with the torrent
extension on your mobile or TV.

`````{tab-set}
````{tab-item} Linux
On Linux, you can easily install the package with the official Flatpak
version.

```{code} bash
flatpak install -y flathub com.stremio.Stremio
```
````
````{tab-item} Windows
On Windows, [the traditional .exe installer](https://www.stremio.com/downloads)
is available.
````
`````

## Torrentio

The magic for watching free movies and series comes from an extension that lets
you play torrent content in Stremio and has several torrent servers available.
I'll highlight *The Pirate Bay*, *Torrent Galaxy* (for English content),
*Cinecalidad* (for Latin American Spanish audio), *Mejor Torrent* (for Spanish
audio), and *Nyaasi* (for anime).

To install Torrentio, use this
[link](https://torrentio.strem.fun/providers=yts,eztv,rarbg,1337x,thepiratebay,kickasstorrents,torrentgalaxy,magnetdl,horriblesubs,nyaasi,tokyotosho,anidex,mejortorrent,wolfmax4k,cinecalidad%7Csort=seeders%7Clanguage=spanish,latino%7Cqualityfilter=cam/configure),
which has the configuration I recommend. The special features of this
configuration are:

1. *Providers*: We exclude *Rutor*, *Rutracker*, *Comando*, *BluDV*, and
   *Torrent9*. Excluding these removes content primarily in Russian, Portuguese,
   and Italian, leaving content in English, Spanish, and Japanese (anime).
2. *Sorting*: We apply *By seeders*, prioritizing content that will potentially
   play best. If there are few seeders, playback might be problematic,
   especially with large files, but sometimes there are surprises, so you can
   try even with few seeders.
3. *Priority foreign language*: *Spanish* and *Latino*. This prioritizes content
   in Spanish, following the seeder sorting and then again by seeders but in any
   other language. Usually, the declared language corresponds to the available
   audio language.
4. *Exclude qualities/resolutions*: *CAM*. You don't want to watch this content.
   These are recordings made with a camera over a cinema or home playback. The
   image and audio are terrible.

If you want to modify anything, go ahead, and then click the *INSTALL* button.

In my experience, there's a good chance of finding popular content in both Latin
American and Spain Spanish, but it's always best to be willing to watch content
in English for reliable and smooth playback. Thanks to the OpenSubtitles v3 and
OpenSubtitles extensions (both official), we have a repository of subtitles for
our content, even if they aren't embedded (embedded is much better).

## Installing on TV

Stremio and its extensions work on Android, so you can use this not only on your
mobile but also on your Android TV. As I previously mentioned, it's important
that you've created a Stremio account because there's no login form on TV, and
you'll have to use a login link or QR code to access it from your mobile or
computer.

Installation is the best option, but if Stremio isn't available for your TV, you
can also cast from your mobile or connect your computer or mobile via cable to
the TV.

## Extra: Pluto TV

This isn't exactly a good alternative to replace your streaming subscriptions,
but you'll find good free content in Latin American Spanish. If you create an
account, you can opt for progress sync options.
[Pluto TV](https://www.pluto.tv/welcome) is available on the web, Android, and
iOS.
