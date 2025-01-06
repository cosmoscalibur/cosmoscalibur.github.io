# Eliminar archivos generados
clean:
    uv run -- ablog clean

# Generar con entorno local
build $DEPLOY_LOCAL="1": clean
    uv run -- ablog build

# Generar con entorno final
deploy: clean
    uv run -- ablog build

# Iniciar servidor con entorno local
serve: build
    uv run -- ablog serve
