# Diseño de `--deshacer` (organizador)

Objetivo: revertir la última organización que se aplicó con `--aplicar`, devolviendo cada archivo a donde estaba.

## El problema central
El programa termina al acabar. Cuando después se escribe `--deshacer`, ¿cómo sabe qué movió la vez anterior?
`ejecutar()` ya devuelve la lista de `Movimiento` realmente aplicados (con el destino real, incluso si hubo `_1`). Esa lista tiene toda la información; hay que **guardarla en disco**.

## Decisiones a tomar (anótalas antes de programar)
1. **¿Dónde se guarda el historial?** Opciones: un archivo oculto dentro de la carpeta organizada (por ejemplo `.organizador-historial.json`) o en una carpeta del usuario. ¿Qué pasa si organizas dos carpetas distintas?
2. **¿Qué formato?** JSON es lo más simple. Ojo: `Path` no se puede guardar directo en JSON; hay que convertirlo a texto y volver a `Path` al leerlo.
3. **¿Solo la última vez o varias?** Empieza con solo la última. Pregúntate qué pasa si ejecutas `--aplicar` dos veces seguidas y luego `--deshacer`.
4. **¿Qué pasa si algo cambió?** El archivo movido ya no está, o en el origen ya existe otro con el mismo nombre. Nunca debe sobrescribir ni perder datos (igual que `_destino_libre`).
5. **¿Qué hacer con las carpetas que quedan vacías** (`imagenes/`, `2025-03/`)? ¿Se borran o se dejan?
6. **¿Cómo se usa?** Consistencia con el resto: por defecto solo muestra qué haría y con `--aplicar` lo hace. ¿Eso aplica también a `--deshacer`?
7. **Sin historial:** mensaje claro y código de salida distinto de 0, no un traceback.

## Herramientas nuevas para ti
- Módulo `json`: `json.dumps` / `json.loads`.
- `Path.write_text()` / `Path.read_text()`.
- Convertir `Movimiento` a diccionario y volver (pista: `dataclasses.asdict` + `str()` de las rutas).
- `Path.exists()`, `Path.rmdir()` (solo borra carpetas vacías).

## Orden de trabajo (test primero, siempre)
1. Escribe tus pasos y decisiones (arriba) en texto.
2. **Guardar historial:** test de que, tras `ejecutar`, existe el archivo con los movimientos.
3. **Leer historial:** test de ida y vuelta (lo que guardas es lo que lees).
4. **`deshacer()` en `core.py`:** test con `tmp_path` que organiza, deshace y comprueba que los archivos volvieron.
5. **Casos borde:** sin historial, archivo faltante, origen ocupado.
6. **El flag `--deshacer` en el CLI**, con su test (como `test_cli_por_mes`).
7. `uv run ruff check`, `uv run ruff format`, `uv run pytest -q`, README y commit.

## Antes de empezar
- La rama `porfecha` debe estar fusionada en `main` (revisa el Pull Request y que el CI salga verde).
- Crea una rama nueva desde `main` actualizado: `git checkout main`, `git pull` y `git checkout -b deshacer`.
