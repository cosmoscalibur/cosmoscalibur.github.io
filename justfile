# Directorio de caché para preservar imágenes de previsualización social
_social_cache := ".cache/social_previews"
_social_build := "docs/_images/social_previews"

# Respaldar previsualizaciones sociales antes de limpiar
[private]
backup-social:
    #!/usr/bin/env zsh
    if [[ -d "{{ _social_build }}" ]]; then
        mkdir -p "{{ _social_cache }}"
        cp -a "{{ _social_build }}/." "{{ _social_cache }}/"
    fi

# Restaurar previsualizaciones sociales después de limpiar
[private]
restore-social:
    #!/usr/bin/env zsh
    if [[ -d "{{ _social_cache }}" ]]; then
        mkdir -p "{{ _social_build }}"
        cp -a "{{ _social_cache }}/." "{{ _social_build }}/"
    fi

# Eliminar archivos generados (preserva social previews)
clean: backup-social
    rm -rf docs .doctrees
    just restore-social

# Generar con entorno local
build $DEPLOY_LOCAL="1": clean
    uv run -- sphinx-build . docs

# Generar con entorno final
deploy: clean
    uv run -- sphinx-build . docs

# Iniciar servidor con entorno local
serve: build
    -kill $(lsof -ti:8000) 2>/dev/null
    uv run -- python -m http.server -d docs
