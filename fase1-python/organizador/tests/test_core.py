import os
from datetime import datetime
from pathlib import Path

import pytest

from organizador import main
from organizador.core import categoria_de, ejecutar, mes_de, planificar


@pytest.mark.parametrize(
    ("nombre", "esperada"),
    [
        ("foto.JPG", "imagenes"),
        ("informe.pdf", "documentos"),
        ("script.py", "codigo"),
        ("raro.xyz", "otros"),
        ("sinextension", "otros"),
    ],
)
def test_categoria_de(nombre: str, esperada: str) -> None:
    assert categoria_de(Path(nombre)) == esperada


def test_planificar_no_toca_el_disco(tmp_path: Path) -> None:
    (tmp_path / "a.png").write_text("x")
    movimientos = planificar(tmp_path)
    assert [m.destino for m in movimientos] == [tmp_path / "imagenes" / "a.png"]
    assert (tmp_path / "a.png").exists()


def test_ejecutar_mueve_archivos(tmp_path: Path) -> None:
    (tmp_path / "a.pdf").write_text("x")
    ejecutar(planificar(tmp_path))
    assert (tmp_path / "documentos" / "a.pdf").exists()
    assert not (tmp_path / "a.pdf").exists()


def test_ejecutar_no_sobrescribe(tmp_path: Path) -> None:
    (tmp_path / "documentos").mkdir()
    (tmp_path / "documentos" / "a.pdf").write_text("viejo")
    (tmp_path / "a.pdf").write_text("nuevo")
    ejecutar(planificar(tmp_path))
    assert (tmp_path / "documentos" / "a.pdf").read_text() == "viejo"
    assert (tmp_path / "documentos" / "a_1.pdf").read_text() == "nuevo"


def test_cli_por_defecto_solo_muestra(tmp_path: Path, capsys) -> None:
    (tmp_path / "a.png").write_text("x")
    assert main([str(tmp_path)]) == 0
    assert "a.png -> imagenes/" in capsys.readouterr().out
    assert (tmp_path / "a.png").exists()


def test_cli_por_mes(tmp_path: Path, capsys) -> None:
    archivo1 = tmp_path / "a.txt"
    archivo1.write_text("x")
    modificacion1 = datetime(2025, 3, 15).timestamp()
    acceso1 = datetime(2025, 3, 15).timestamp()

    archivo2 = tmp_path / "b.txt"
    archivo2.write_text("x")
    modificacion2 = datetime(2025, 5, 15).timestamp()
    acceso2 = datetime(2025, 5, 15).timestamp()
    os.utime(archivo1, (acceso1, modificacion1))
    os.utime(archivo2, (acceso2, modificacion2))

    assert main([str(tmp_path), "--por-fecha"]) == 0
    salida = capsys.readouterr().out
    assert "a.txt -> 2025-03/" in salida
    assert "b.txt -> 2025-05/" in salida
    assert (tmp_path / "a.txt").exists()
    assert (tmp_path / "b.txt").exists()


def test_mes_de(tmp_path: Path) -> None:
    archivo = tmp_path / "a.txt"
    archivo.write_text("x")
    modificacion = datetime(2025, 3, 15).timestamp()
    acceso = datetime(2026, 1, 10).timestamp()
    os.utime(archivo, (acceso, modificacion))
    assert mes_de(archivo) == "2025-03"


def test_planificar_por_mes(tmp_path: Path) -> None:
    archivo_1 = tmp_path / "a.txt"
    archivo_2 = tmp_path / "b.txt"
    archivo_1.write_text("x")
    archivo_2.write_text("x")
    os.utime(
        archivo_1,
        ((datetime(2025, 3, 15)).timestamp(), (datetime(2025, 3, 15)).timestamp()),
    )
    os.utime(
        archivo_2,
        ((datetime(2025, 5, 15)).timestamp(), (datetime(2025, 5, 15)).timestamp()),
    )
    movimientos = planificar(tmp_path, True)
    assert [m.destino for m in movimientos] == [
        tmp_path / "2025-03" / "a.txt",
        tmp_path / "2025-05" / "b.txt",
    ]
    assert (tmp_path / "a.txt").exists()
    assert (tmp_path / "b.txt").exists()
