---
date: 2025-04-23
tags: container, docker, linux, manjaro
category: technology, programming
language: en
---

# Install Docker on Manjaro

Now that I use Manjaro, it's worth reviewing the steps to install Docker on
Manjaro.

Due to work-related reasons, more than ever it is important for me to use
Docker, because at Tributi, our official operating system in the Tech team is
Ubuntu (now version 24.04). Since my development environment is Manjaro, my
local setup no longer serves for testing, and I need a way to ensure the same
environment. For this purpose, Docker becomes the appropriate alternative for
reproducibility.

## Docker in Repository

In Manjaro (and Arch), Docker can be installed from the official package
repository. We should note that the container composition component is found in
the `docker-compose` package.

```bash
pamac install docker docker-compose --no-confirm
```

## Docker Configuration

To make Docker available for invocation, we can enable the service daemon or the
*socket*. The first option is suitable for server environments, while the second
is better for local environments to reduce resource consumption (this remains
active with the first call, unlike the first option which stays active since
system boot).

### Enabling the Daemon Service

To enable the daemon service, run:

```bash
sudo systemctl enable docker.service
```

### Enabling the *Socket* Service

To enable the *socket* service, run:

```bash
sudo systemctl enable docker.socket
```

For now, this allows us to initialize Docker, but we must always run it with
administrative permissions. If we wish to run it without administrative
permissions, we can add our user to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

## References

- [Docker](https://wiki.archlinux.org/title/Docker). Wiki ArchLinux.
- [docker.service tops the systemd-analyze critical path](https://github.com/moby/moby/issues/38373#issuecomment-447393517).
  Repositorio Moby.
