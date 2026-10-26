"""Ejercicios de la semana 1. Reemplaza cada `raise NotImplementedError`."""

from collections.abc import Callable, Iterable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel


# 1. Comprensiones -----------------------------------------------------------
def cuadrados_pares(numeros: list[int]) -> list[int]:
    """Cuadrado de cada número par, en una sola línea. [1, 2, 3, 4] -> [4, 16]"""
    raise NotImplementedError


def contar_por_extension(nombres: list[str]) -> dict[str, int]:
    """{'.py': 2, '.md': 1} para ['a.py', 'b.py', 'c.md']. Pista: Path(n).suffix."""
    raise NotImplementedError


# 2. Generadores -------------------------------------------------------------
def leer_lineas_no_vacias(ruta: Path) -> Iterator[str]:
    """Produce (yield) cada línea sin espacios en los extremos, saltando las vacías."""
    raise NotImplementedError


def en_lotes(items: Iterable[str], tamano: int) -> Iterator[list[str]]:
    """Agrupa en listas de `tamano`; el último lote puede ser menor.
    Lo usarás en la fase 4 para mandar textos a embeddings por lotes."""
    raise NotImplementedError


# 3. Context managers --------------------------------------------------------
@contextmanager
def registrar(eventos: list[str]) -> Iterator[None]:
    """Agrega 'inicio' al entrar y 'fin' al salir, AUNQUE el bloque lance excepción."""
    raise NotImplementedError
    yield  # mantiene esto como generador; bórralo al implementar


# 4. Decoradores -------------------------------------------------------------
def reintentar(veces: int) -> Callable[[Callable], Callable]:
    """Reintenta la función hasta `veces` intentos si lanza excepción; si todos
    fallan, relanza la última. Usa functools.wraps. (Fase 3: reintentos a la API.)"""
    raise NotImplementedError


# 5. dataclasses -------------------------------------------------------------
@dataclass(frozen=True)
class Precio:
    """Precio inmutable en centavos (nunca float para dinero)."""

    centavos: int
    moneda: str = "USD"

    def __add__(self, otro: "Precio") -> "Precio":
        """Suma dos precios; ValueError si las monedas difieren."""
        raise NotImplementedError


# 6. pydantic ----------------------------------------------------------------
class Tarea(BaseModel):
    """Define los campos: titulo (str), prioridad (int, 1 a 5) y etiquetas
    (list[str], vacía por defecto). Pista: Field(ge=1, le=5)."""


def parsear_tarea(json_texto: str) -> Tarea:
    """Convierte JSON en Tarea; deja que pydantic lance ValidationError si es inválido."""
    raise NotImplementedError
