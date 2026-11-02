# organizador

CLI que ordena una carpeta moviendo cada archivo a una subcarpeta según su extensión (`imagenes`, `documentos`, `hojas`, `codigo`, `comprimidos`, `otros`).

Con `--por-fecha` agrupa en cambio por mes de modificación (`2025-03`, `2025-05`, ...).

Por seguridad, **por defecto solo muestra el plan**. Los archivos se mueven únicamente con `--aplicar`, y nunca se sobrescribe nada: si el destino existe se guarda como `nombre_1.ext`.

## Uso
```powershell
uv sync
uv run organizador C:\ruta\a\carpeta            # muestra el plan
uv run organizador C:\ruta\a\carpeta --aplicar  # mueve los archivos
uv run organizador C:\ruta\a\carpeta --por-fecha          # plan agrupado por mes
uv run organizador C:\ruta\a\carpeta --por-fecha --aplicar  # lo aplica
```

Ejemplo de salida del plan (no mueve nada):
```
a.txt -> 2025-03/
b.txt -> 2025-05/

2 archivos. Usa --aplicar para moverlos.
```

## Desarrollo
```powershell
uv run pytest
uv run ruff check
uv run ruff format --check
```

## Qué practica este proyecto
`pathlib`, `dataclasses` inmutables, tipado, `argparse`, separación entre planificar y ejecutar, `pytest` con `parametrize`, `tmp_path` y `capsys`, y fechas de archivos (`stat().st_mtime`, `os.utime` en los tests).
