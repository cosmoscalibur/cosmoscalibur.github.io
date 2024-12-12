# Recarga la terminal Linux


## Nuevo ecosistema de utilidades

+ `bat`: Sustituto de `cat`.
+ `bottom` (`btm`): Sustituto de `top`.
+ `eza`: Sustituto de `ls`.
+ `fd-find`: Sustituto de `find`.
+ `procs`: Sustituto de `ps`.
+ `du-dust` (`dust`): Sustituto de `du`.
+ `ripgrep`: Sustituto de `grep`.
+ `fzf`: Buscador difuso en Go.

::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro
```{code} bash
sudo pamac install bat bottom dust eza fd fzf procs ripgrep --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu
```{code} bash
sudo apt install -y bat du-dust eza fd-find fzf ripgrep
cargo install --locked bottom procs

```
:::



## Kit de terminal

+ *Alacritty*: Emulador de terminal
+ *Zellij*: Multiplexador de terminal
+ *Starship*: *Prompt* de terminal.
+ *Zsh*: *Shell* (lenguaje de terminal)
+ zoxide: Alternativa a cd
+ yazi
+ helix


::::{tab-set}
:::{tab-item} Manjaro
:sync: manjaro
```{code} bash
sudo pamac install zsh alacritty zellij starship zoxide yazi helix --no-confirm
```
:::
:::{tab-item} Ubuntu
:sync: ubuntu
```{code} bash
sudo apt install -y zsh alacritty zoxide
cargo install --locked zellij yazi-fm yazi-cli
curl -sS https://starship.rs/install.sh | sh
flatpak install flathub com.helix_editor.Helix
```
:::
::::


```{code} bash
chsh -s /bin/zsh  # Configurar shell por defecto: ingresamos contraseña
```

```{code} bash
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
echo 'eval "$(zoxide init zsh)"' >> ~/.zshrc
source ~/.zshrc
```

```{code} bash
bat << 'EOF' > ~/.config/alacritty.toml
[terminal.shell]
args = ["-l", "-c", "zellij attach --index 0 || zellij"]
program = "/bin/zsh"
EOF
```


KDE

{menuselection}`Aplicaciones predeterminadas --> Emulador de terminal --> Alacritty`
{menuselection}`Atajos de teclado --> Añadir nuevo --> Aplicación --> Alacritty`
Configuramos atajo de "Lanzar" dando clic a {guilabel}`Añadir`, y tras ello el atajo
deseado. En mi caso prefiero el habitual de la terminal de {kbd}`Control-Alt-T`.
Aplicamos el cambio ({guilabel}`Aplicar`).
