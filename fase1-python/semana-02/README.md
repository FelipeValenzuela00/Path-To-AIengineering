# Semana 2: async/await

**Para qué:** llamar a una API (como la de Claude) tarda. Con `async` tu programa puede esperar varias respuestas a la vez en lugar de una detrás de otra, limitar cuántas manda a la vez y cortar las que tardan demasiado. Es lo que usarás desde la semana 3.

No hay red de verdad: `api_falsa` simula una llamada que tarda 0.1 s.

## Cómo trabajar
Desde esta carpeta:
```bash
uv run pytest -x
```
```bash
uv run pytest -k timeout
```

## Temas (en orden)

| # | Tema | En C# | Idea clave |
|---|---|---|---|
| 1 | Corrutinas | `async Task<int>` | `async def` crea una corrutina; `await` espera su resultado |
| 2 | Concurrencia | `Task.WhenAll` | `asyncio.gather` lanza varias a la vez y devuelve los resultados en orden |
| 3 | Límite de concurrencia | `SemaphoreSlim` | `asyncio.Semaphore(n)`: como mucho `n` dentro a la vez |
| 4 | Timeouts | `CancellationTokenSource(timeout)` | `async with asyncio.timeout(s):` y capturar `TimeoutError` |
| 5 | Streaming | `IAsyncEnumerable` + `await foreach` | generador con `async def` + `yield`; se recorre con `async for` |

Diferencia clave con C#: en Python una corrutina **no empieza a correr** hasta que alguien la espera (`await`) o la lanza (`gather`, `create_task`). Llamar `obtener_uno(3)` sin `await` no hace nada: devuelve un objeto corrutina.

Los tests usan `asyncio.run(...)`, que es el punto de entrada: arranca el bucle de eventos, ejecuta la corrutina y lo cierra.

## Para leer (40-60 min)
- Corrutinas y tareas: https://docs.python.org/3/library/asyncio-task.html (hasta "Timeouts").
- Semáforos: https://docs.python.org/3/library/asyncio-sync.html#semaphore
- Generadores async: https://peps.python.org/pep-0525/ (solo la sección "Rationale and Goals").

## Terminado cuando
- [ ] Los tests de esta carpeta pasan
- [ ] `uv run ruff check` y `uv run ruff format --check` limpios
- [ ] Puedes explicar con tus palabras por qué `obtener_todos` tarda ~0.1 s y no ~1 s
