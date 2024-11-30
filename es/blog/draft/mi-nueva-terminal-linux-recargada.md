Linux utilities # bat: cat # bottom (btm): top # du-dust (dust): du # eza: ls #
fd-find: find # ripgrep: grep # bottom: top/htop # procs: ps

```
cargo install --locked bat bottom du-dust eza fd-find procs ripgrep
sudo apt install -y fzf
```

alacritty: terminal emulator (rs) sudo apt install -y alacritty # man pages,
logo, desktop entry sudo update-alternatives --install
/usr/bin/x-terminal-emulator x-terminal-emulator \$(which alacritty) 70 # sudo
update-alternatives --config x-terminal-emulator ## check

```
# Atajo de teclado
# Aplicaciones por defecto
```

zellij: multiplexer (rs) cargo install --locked zellij # Ejecutar zellij en
alacritty mkdir -p ~/.config/alacritty cat \<< EOF >
~/.config/alacritty/alacritty.toml [shell] args = \["-l", "-c", "zellij attach
--index 0 || zellij"\] program = "/usr/bin/bash" EOF

starship: prompt (rs) curl -sS https://starship.rs/install.sh | sh echo 'eval
"\$(starship init bash)"' >> ~/.bashrc

zsh zoxide

cargo install --locked yazi-fm yazi-cli # file manager terminal
