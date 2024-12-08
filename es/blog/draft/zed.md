```{code} json
{
  "assistant": {
    "default_model": {
      "provider": "ollama",
      "model": "llama3.2:3b"
    },
    "version": "2"
  },
  "features": {
    "inline_completion_provider": "none"
  },
  "ui_font_size": 16,
  "buffer_font_size": 16,
  "theme": {
    "mode": "system",
    "light": "Andromeda",
    "dark": "One Dark"
  },
  "languages": {
    "Markdown": {
      "format_on_save": "on",
      "formatter": {
        "external": {
          "command": "mdformat",
          "arguments": ["--number", "--wrap", "80", "--extensions", "myst", "-"]
        }
      }
    }
  },
  "lsp": {
    "ltex": {
      "settings": {
        "ltex": {
          "language": "es",
          "enabled": ["latex", "markdown"],
          "completionEnabled": true
        }
      }
    }
  }
}
```

```
curl -f https://zed.dev/install.sh | sh

# https://github.com/zed-industries/zed/issues/10943
https://benswift.me/blog/2024/09/20/format-markdown-on-save-in-zed-using-prettier/
https://github.com/vitallium/zed-ltex
```

Se presenta error de no abrir. Si se ejecuta en X11 abre transparente, sin
embargo si es en Wayland, falla. En Wayland el problema es con los
controladores de NVIDIA y se aprecia si pruebas vkcube-wayland (mensaje de
error) y vkcube ejecuta normal.

desinstalar zed https://askubuntu.com/questions/1520457/how-do-i-uninstall-zed-editor-from-my-ubuntu-24


búsqueda general control shift f
modo multibuffer con control shift l
alt clic para selección individual
