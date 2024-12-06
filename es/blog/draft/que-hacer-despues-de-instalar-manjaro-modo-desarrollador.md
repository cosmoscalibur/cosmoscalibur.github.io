UV

curl -LsSf https://astral.sh/uv/install.sh | sh

Rust

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Zed

curl -f https://zed.dev/install.sh | sh


Development

cargo install --locked difftastic just hyperfine
sudo pamac install difftastic just hyperfine --no-confirm

```
sudo snap install --classic helix
cargo install --locked evcxr_jupyter  # Rust jupyter kernel
cargo install --locked shellharden  # shellcheck
sudo apt install -y shellcheck shfmt


cargo install --git https://github.com/bbqsrc/xml-pretty
```

Instalar Code

```{code} bash
sudo snap install --classic code
pamac install code
ln -s /usr/share/hunspell/\* ~/.config/Code/Dictionaries
```

Extensiones

- timonwong.shellcheck
- mads-hartmann.bash-ide-vscode
- eamodio.gitlens
- executablebookproject.myst-highlight
- rust-lang.rust-analyzer
- swyddfa.esbonio
- ms-azuretools.vscode-docker
- ban.spellright
- ms-python.python
- james-yu.latex-workshop


```
git config --global user.email "cosmoscalibur@gmail.com"
git config --global user.name "Edward Villegas-Pulgarin"
git config --global pull.rebase true
```

Extensiones solo disponibles para VSCode y no para Code (OSS).
