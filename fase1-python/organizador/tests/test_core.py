from pathlib import Path

import pytest

from organizador import main
from organizador.core import categoria_de, ejecutar, planificar


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
