"""Ejercicios de la semana 1. Reemplaza cada `raise NotImplementedError`."""

from collections.abc import Callable, Iterable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, Field


# 1. Comprensiones -----------------------------------------------------------
def cuadrados_pares(numeros: list[int]) -> list[int]:
    """Devuelve el cuadrado de cada número par, sin modificar la lista original."""
    return [n**2 for n in numeros if n % 2 == 0]


def contar_por_extension(nombres: list[str]) -> dict[str, int]:
    """Cuenta los archivos por extensión: ['a.py', 'b.py', 'c.md'] -> {'.py': 2, '.md': 1}."""
    extensiones = [Path(n).suffix for n in nombres]
    return {ext: extensiones.count(ext) for ext in set(extensiones)}


# 2. Generadores -------------------------------------------------------------
def leer_lineas_no_vacias(ruta: Path) -> Iterator[str]:
    """Entrega una a una las líneas del archivo sin espacios en los extremos, saltando las vacías."""
    with ruta.open() as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                yield linea


def en_lotes(items: Iterable[str], tamano: int) -> Iterator[list[str]]:
    """Agrupa en listas de `tamano`; el último lote puede ser menor.
    Lo usarás en la fase 4 para mandar textos a embeddings por lotes."""
    lote: list[str] = []
    for item in items:
        lote.append(item)
        if len(lote) == tamano:
            yield lote
            lote = []
    if lote:
        yield lote


# 3. Context managers --------------------------------------------------------
@contextmanager
def registrar(eventos: list[str]) -> Iterator[None]:
    """Agrega 'inicio' al entrar y 'fin' al salir, aunque el bloque lance una excepción."""
    eventos.append("inicio")
    try:
        yield
    finally:
        eventos.append("fin")


# 4. Decoradores -------------------------------------------------------------
def reintentar(veces: int) -> Callable[[Callable], Callable]:
    """Reintenta la función hasta `veces` intentos si lanza excepción; si todos
    fallan, relanza la última. Usa functools.wraps. (Fase 3: reintentos a la API.)"""

    def reintentar(f):
        from functools import wraps

        @wraps(f)
        def wrapper(*args, **kwargs):
            for intento in range(veces):
                try:
                    return f(*args, **kwargs)
                except Exception:
                    if intento == veces - 1:
                        raise

        return wrapper

    return reintentar


# 5. dataclasses -------------------------------------------------------------
@dataclass(frozen=True)
class Precio:
    """Precio inmutable en centavos (nunca float para dinero)."""

    centavos: int
    moneda: str = "USD"

    def __add__(self, otro: Precio) -> Precio:
        """Suma dos precios y devuelve uno nuevo; ValueError si las monedas difieren."""
        if self.moneda != otro.moneda:
            raise ValueError("Monedas diferentes")
        return Precio(self.centavos + otro.centavos, self.moneda)


# 6. pydantic ----------------------------------------------------------------
class Tarea(BaseModel):
    """Tarea con título, prioridad de 1 a 5 y etiquetas opcionales."""

    titulo: str
    prioridad: int = Field(ge=1, le=5)
    etiquetas: list[str] = []


def parsear_tarea(json_texto: str) -> Tarea:
    """Convierte un JSON en Tarea; pydantic lanza ValidationError si es inválido."""
    return Tarea.model_validate_json(json_texto)
