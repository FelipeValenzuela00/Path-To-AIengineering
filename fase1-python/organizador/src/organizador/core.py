"""Lógica para organizar archivos en subcarpetas según su extensión."""

import shutil
from dataclasses import dataclass
from pathlib import Path

CATEGORIAS: dict[str, str] = {
    ".jpg": "imagenes",
    ".jpeg": "imagenes",
    ".png": "imagenes",
    ".gif": "imagenes",
    ".pdf": "documentos",
    ".docx": "documentos",
    ".txt": "documentos",
    ".xlsx": "hojas",
    ".csv": "hojas",
    ".zip": "comprimidos",
    ".py": "codigo",
    ".js": "codigo",
}
OTROS = "otros"


@dataclass(frozen=True)
class Movimiento:
    origen: Path
    destino: Path


def categoria_de(archivo: Path) -> str:
    """Devuelve la carpeta destino para un archivo según su extensión."""
    return CATEGORIAS.get(archivo.suffix.lower(), OTROS)


def planificar(carpeta: Path) -> list[Movimiento]:
    """Calcula los movimientos necesarios sin tocar el disco."""
    return [
        Movimiento(f, carpeta / categoria_de(f) / f.name)
        for f in sorted(carpeta.iterdir())
        if f.is_file()
    ]


def _destino_libre(destino: Path) -> Path:
    """Evita sobrescribir: agrega un sufijo numérico si el destino ya existe."""
    if not destino.exists():
        return destino
    n = 1
    while (
        candidato := destino.with_name(f"{destino.stem}_{n}{destino.suffix}")
    ).exists():
        n += 1
    return candidato


def ejecutar(movimientos: list[Movimiento]) -> list[Movimiento]:
    """Mueve los archivos y devuelve los movimientos realmente aplicados."""
    aplicados = []
    for m in movimientos:
        destino = _destino_libre(m.destino)
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(m.origen, destino)
        aplicados.append(Movimiento(m.origen, destino))
    return aplicados
