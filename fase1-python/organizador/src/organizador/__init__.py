"""CLI para organizar una carpeta por tipo de archivo."""

import argparse
from pathlib import Path

from organizador.core import ejecutar, planificar


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="organizador", description="Organiza archivos por extensión."
    )
    parser.add_argument("carpeta", type=Path, help="carpeta a organizar")
    parser.add_argument(
        "--aplicar",
        action="store_true",
        help="mueve los archivos (por defecto solo muestra el plan)",
    )
    args = parser.parse_args(argv)

    if not args.carpeta.is_dir():
        parser.error(f"no es una carpeta: {args.carpeta}")

    movimientos = planificar(args.carpeta)
    if not args.aplicar:
        for m in movimientos:
            print(f"{m.origen.name} -> {m.destino.parent.name}/")
        print(f"\n{len(movimientos)} archivos. Usa --aplicar para moverlos.")
        return 0

    aplicados = ejecutar(movimientos)
    print(f"{len(aplicados)} archivos movidos.")
    return 0
