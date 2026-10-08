# organizador

CLI que ordena una carpeta moviendo cada archivo a una subcarpeta según su extensión (`imagenes`, `documentos`, `hojas`, `codigo`, `comprimidos`, `otros`).

Por seguridad, **por defecto solo muestra el plan**. Los archivos se mueven únicamente con `--aplicar`, y nunca se sobrescribe nada: si el destino existe se guarda como `nombre_1.ext`.

## Uso
```powershell
uv sync
uv run organizador C:\ruta\a\carpeta            # muestra el plan
uv run organizador C:\ruta\a\carpeta --aplicar  # mueve los archivos
```

## Desarrollo
```powershell
uv run pytest
uv run ruff check
uv run ruff format --check
```

## Qué practica este proyecto
`pathlib`, `dataclasses` inmutables, tipado, `argparse`, separación entre planificar y ejecutar, `pytest` con `parametrize`, `tmp_path` y `capsys`.
