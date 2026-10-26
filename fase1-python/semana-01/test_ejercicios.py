from pathlib import Path

import pytest
from pydantic import ValidationError

from ejercicios import (
    Precio,
    Tarea,
    contar_por_extension,
    cuadrados_pares,
    en_lotes,
    leer_lineas_no_vacias,
    parsear_tarea,
    registrar,
    reintentar,
)


def test_comprension_lista() -> None:
    assert cuadrados_pares([1, 2, 3, 4]) == [4, 16]
    assert cuadrados_pares([]) == []


def test_comprension_dict() -> None:
    assert contar_por_extension(["a.py", "b.py", "c.md"]) == {".py": 2, ".md": 1}


def test_generador_lineas(tmp_path: Path) -> None:
    archivo = tmp_path / "x.txt"
    archivo.write_text("  hola \n\n   \nmundo\n")
    resultado = leer_lineas_no_vacias(archivo)
    assert iter(resultado) is resultado  # es un iterador, no una lista
    assert list(resultado) == ["hola", "mundo"]


@pytest.mark.parametrize(
    ("items", "tamano", "esperado"),
    [
        (["a", "b", "c", "d", "e"], 2, [["a", "b"], ["c", "d"], ["e"]]),
        (["a", "b"], 5, [["a", "b"]]),
        ([], 3, []),
    ],
)
def test_generador_lotes(
    items: list[str], tamano: int, esperado: list[list[str]]
) -> None:
    assert list(en_lotes(iter(items), tamano)) == esperado


def test_context_manager_limpia_con_excepcion() -> None:
    eventos: list[str] = []
    with pytest.raises(RuntimeError), registrar(eventos):
        eventos.append("trabajo")
        raise RuntimeError
    assert eventos == ["inicio", "trabajo", "fin"]


def test_decorador_reintenta() -> None:
    intentos = []

    @reintentar(veces=3)
    def inestable() -> str:
        """doc original"""
        intentos.append(1)
        if len(intentos) < 3:
            raise ConnectionError
        return "ok"

    assert inestable() == "ok"
    assert len(intentos) == 3
    assert inestable.__doc__ == "doc original"  # functools.wraps


def test_decorador_relanza_si_se_agotan() -> None:
    @reintentar(veces=2)
    def siempre_falla() -> None:
        raise ConnectionError("caído")

    with pytest.raises(ConnectionError, match="caído"):
        siempre_falla()


def test_dataclass() -> None:
    assert Precio(150) + Precio(50) == Precio(200)
    with pytest.raises(ValueError):
        Precio(1, "USD") + Precio(1, "CLP")
    with pytest.raises(AttributeError):
        Precio(1).centavos = 2  # type: ignore[misc]  # frozen


def test_pydantic_valido() -> None:
    tarea = parsear_tarea('{"titulo": "Leer docs", "prioridad": 2}')
    assert tarea == Tarea(titulo="Leer docs", prioridad=2, etiquetas=[])


@pytest.mark.parametrize(
    "json_texto",
    ['{"titulo": "x", "prioridad": 9}', '{"prioridad": 1}', "no es json"],
)
def test_pydantic_invalido(json_texto: str) -> None:
    with pytest.raises(ValidationError):
        parsear_tarea(json_texto)
