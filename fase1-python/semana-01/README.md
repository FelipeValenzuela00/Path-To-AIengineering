# Semana 1: lo propio de Python

Ya sabes programar, así que esto no explica qué es un bucle: muestra lo que Python hace distinto. Si todavía no viste la sintaxis básica, lee antes el tutorial oficial, secciones 3 a 5 y 8 (https://docs.python.org/3/tutorial/), unas 2-3 h. Cada tema tiene un ejercicio en `ejercicios.py` con su test en `test_ejercicios.py`. Todos fallan al principio; tu trabajo es ponerlos en verde uno por uno.

## Cómo trabajar
```powershell
cd fase1-python\semana-01
uv run --with pytest --with pydantic pytest -x    # se detiene en el primer fallo
uv run --with pytest --with pydantic pytest -k generador   # solo un tema
```
`--with` crea un entorno temporal: no hace falta `pyproject.toml` para practicar.

## Temas (en orden)

| # | Tema | Equivalente que ya conoces | Idea clave |
|---|---|---|---|
| 1 | Comprensiones | LINQ `Select/Where`, `stream().map().filter()` | `[f(x) for x in xs if cond]`, también `{k: v ...}` y `{x ...}` |
| 2 | Generadores | `yield return` (C#), iteradores perezosos | `yield` produce valores bajo demanda; no carga todo en memoria |
| 3 | Context managers | `using` (C#), try-with-resources (Java) | `with` garantiza la limpieza aunque haya excepción |
| 4 | Decoradores | atributos/anotaciones + AOP | una función que recibe una función y devuelve otra |
| 5 | `dataclasses` | `record` (C#/Java) | `@dataclass(frozen=True)` genera `__init__`, `__eq__`, `__repr__` |
| 6 | `pydantic` | DTO + validación (FluentValidation, Bean Validation) | valida datos externos en la frontera; la base de la salida estructurada con LLMs (fase 3) |

Tipado (`typing`) y `uv` los practicas en todos: cada firma lleva tipos.

## Para leer (30-45 min en total)
- Comprensiones y generadores: https://docs.python.org/3/howto/functional.html
- Context managers: https://docs.python.org/3/library/contextlib.html
- Decoradores: `functools.wraps` en https://docs.python.org/3/library/functools.html
- dataclasses: https://docs.python.org/3/library/dataclasses.html
- pydantic: https://docs.pydantic.dev/latest/concepts/models/

## Ya lo tienes aplicado
El proyecto `../organizador` usa `dataclass(frozen=True)`, comprensiones, `pathlib` y `pytest`. Léelo después del ejercicio 5 y compara.

## Terminado cuando
- [ ] Los tests de esta carpeta pasan
- [ ] `uv run --with ruff ruff check` limpio
- [ ] Nota en `notas/semana-01.md`
