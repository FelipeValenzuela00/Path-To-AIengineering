"""Lógica para organizar archivos en subcarpetas según su extensión."""

import shutil
from dataclasses import dataclass
from datetime import datetime
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


def mes_de(archivo: Path) -> str:
    """Devuelve el mes de modificación del archivo como 'AAAA-MM' (hora local)."""
    dateNmb = archivo.stat().st_mtime
    date = datetime.fromtimestamp(dateNmb)
    return date.strftime("%Y-%m")


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


def planificar(carpeta: Path, por_fecha: bool = False) -> list[Movimiento]:
    """Calcula los movimientos sin tocar el disco.

    Agrupa por tipo de archivo; con `por_fecha=True`, por mes de modificación.
    """

    if por_fecha:
        carpeta_final = mes_de
    else:
        carpeta_final = categoria_de

    return [
        Movimiento(f, carpeta / carpeta_final(f) / f.name)
        for f in sorted(carpeta.iterdir())
        if f.is_file()
    ]
