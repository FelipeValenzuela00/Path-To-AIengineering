"""Ejercicios de la semana 2: async/await. Reemplaza cada `raise NotImplementedError`."""

import asyncio
from collections.abc import AsyncIterator, Awaitable, Callable


async def api_falsa(numero: int, demora: float = 0.1) -> dict[str, int]:
    """Simula una llamada por red: espera `demora` segundos y responde. Ya está hecha."""
    await asyncio.sleep(demora)
    return {"numero": numero, "valor": numero * 10}


# 1. Corrutinas --------------------------------------------------------------
async def obtener_uno(numero: int) -> int:
    """Llama a `api_falsa` y devuelve solo el campo 'valor'. 3 -> 30"""
    resultado = await api_falsa(numero)

    return resultado["valor"]


# 2. Concurrencia ------------------------------------------------------------
async def obtener_todos(numeros: list[int]) -> list[int]:
    """Devuelve el 'valor' de cada número, en el mismo orden, haciendo las llamadas
    A LA VEZ (no una detrás de otra). Pista: asyncio.gather."""
    pendiente = [api_falsa(n) for n in numeros]

    resultado = await asyncio.gather(*pendiente)

    return [r["valor"] for r in resultado]


# 3. Limitar la concurrencia (lo que exigen los rate limits de una API) -------
async def obtener_con_limite(
    numeros: list[int],
    maximo: int,
    llamar: Callable[[int], Awaitable[dict[str, int]]] = api_falsa,
) -> list[int]:
    """Igual que `obtener_todos`, pero con como mucho `maximo` llamadas en curso a la vez.
    `llamar` es la función async que hace cada llamada. Pista: asyncio.Semaphore."""
    portero = asyncio.Semaphore(maximo)

    async def llamada(numero: int) -> dict[str, int]:
        async with portero:
            return await llamar(numero)

    resultado = await asyncio.gather(*[llamada(x) for x in numeros])
    return [r["valor"] for r in resultado]


# 4. Timeouts ----------------------------------------------------------------
async def con_timeout(numero: int, demora: float, limite: float) -> int | None:
    """Llama a `api_falsa(numero, demora)`. Si tarda más de `limite` segundos, devuelve
    None en vez de esperar. Pista: asyncio.timeout y TimeoutError."""
    try:
        async with asyncio.timeout(limite):
            resultado = await api_falsa(numero, demora)
            return resultado["valor"]
    except TimeoutError:
        return None


# 5. Streaming (así llegan las respuestas de un LLM) -------------------------
async def generar_trozos(texto: str, tamano: int) -> AsyncIterator[str]:
    """Generador ASYNC: entrega el texto en trozos de `tamano` caracteres.
    "abcdefg", 3 -> "abc", "def", "g". Haz `await asyncio.sleep(0)` entre trozos."""

    for i in range(0, len(texto), tamano):
        yield texto[i : i + tamano]
        await asyncio.sleep(0)


async def unir_stream(trozos: AsyncIterator[str]) -> str:
    """Recibe los trozos a medida que llegan y devuelve el texto completo.
    Pista: `async for`."""
    lista = []

    async for t in trozos:
        lista.append(t)

    resultado = "".join(lista)

    return resultado
