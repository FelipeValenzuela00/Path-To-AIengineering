import asyncio
import time

import pytest

from ejercicios import (
    con_timeout,
    generar_trozos,
    obtener_con_limite,
    obtener_todos,
    obtener_uno,
    unir_stream,
)


def test_obtener_uno() -> None:
    assert asyncio.run(obtener_uno(3)) == 30


def test_obtener_todos_en_orden() -> None:
    assert asyncio.run(obtener_todos([1, 2, 3])) == [10, 20, 30]


def test_obtener_todos_es_concurrente() -> None:
    inicio = time.perf_counter()
    asyncio.run(obtener_todos(list(range(10))))
    # 10 llamadas de 0.1 s: una detrás de otra tardarían ~1 s
    assert time.perf_counter() - inicio < 0.5


def test_obtener_con_limite_respeta_el_maximo() -> None:
    activas = 0
    pico = 0

    async def llamar(numero: int) -> dict[str, int]:
        nonlocal activas, pico
        activas += 1
        pico = max(pico, activas)
        await asyncio.sleep(0.01)
        activas -= 1
        return {"numero": numero, "valor": numero}

    resultado = asyncio.run(obtener_con_limite(list(range(10)), 3, llamar))
    assert resultado == list(range(10))
    assert pico == 3


@pytest.mark.parametrize(("demora", "esperado"), [(0.01, 20), (0.5, None)])
def test_con_timeout(demora: float, esperado: int | None) -> None:
    assert asyncio.run(con_timeout(2, demora, limite=0.1)) == esperado


def test_generar_trozos() -> None:
    async def juntar() -> list[str]:
        return [t async for t in generar_trozos("abcdefg", 3)]

    assert asyncio.run(juntar()) == ["abc", "def", "g"]


def test_unir_stream() -> None:
    async def stream() -> object:
        for trozo in ["Hola", ", ", "mundo"]:
            yield trozo

    assert asyncio.run(unir_stream(stream())) == "Hola, mundo"
