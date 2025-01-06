---
date: 2024-06-04
tags: linux videogames, steam, wine, linux applications
category: entertainment, videogames
language: en
---

# Proton: Compatibility Mode of Steam

Do you want to play that Steam game that is supported on Windows, but not on
Linux? I'll tell you how to use the compatibility mode of Steam for all games.

Yes, I have a gamer side and previously told you a bit about configuring
Retroarch in Steam ([](/en/blog/2021/configurar-retroarch-en-steam.rst)) because
it's my preferred platform (along with others, since many of the games offered
by [Humble Bundle](https://www.humblebundle.com/) are compatible with this). And
it's common for the games I've purchased from bundles or some free-to-play
titles that caught my attention to not have a Linux option, which is my primary
system operating system. But Steam has a solution or at least an alternative
worth trying before forgetting.

## Proton

In the Linux world, you are likely familiar with a tool that allows us to try
running Windows programs on Linux, called [Wine](https://www.winehq.org/).

It turns out that Wine is exactly the default solution, and if not, it's an
adapted solution that applies modifications on top of existing Wine
functionality. And so, Proton emerges as the solution developed by _Valve_ (the
developers of Steam) to enable portability of Windows games for a growing
audience of gamers who use Linux.

[Proton](https://github.com/ValveSoftware/Proton) builds upon Wine, adding a
series of components and patches to make compatibility with Steam games that
were originally designed for Windows. And this has been crucial for the
[Steam Deck](https://store.steamedeck.com/) project, the Linux-based portable
Steam console.

## Steam Play

If we want to install games on our Linux PC that are supported on Windows but
not on Linux, then the compatibility option, which is called Steam Play, comes
pre-enabled by default. However, this only applies to officially supported
titles.

There are still games that can be viewed and run perfectly without being
officially supported, just like this week when I decided to play
[Brawlhalla](https://store.steamedeck.com/app/291550/Brawlhalla/) with my
colleagues, and the surprise was that it wasn't supported on Linux.

So, when we don't have a game enabled, we go to the top menu bar, select
{menuselection}`Steam --> Settings --> Compatibility`, and see that the section
is shown. We will see that the first option (for titles that are officially
supported) is already enabled, but the option for all titles is not. Now, let's
enable it for all titles and accept the restart of Steam. Once we return to
Brawlhalla, we'll see that the {guilabel}`Add to library` button is now enabled.

After completing the installation and starting the game, we'll see a single
error message, which doesn't require concern - we can simply ignore it and play
without any issues.
