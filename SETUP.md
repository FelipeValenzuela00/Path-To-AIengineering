# Instalación de herramientas

## Ya instaladas (verificado)
Python 3.14.6, Git 2.51, Node 22, Docker 29, VS Code, winget.

## Por instalar
Ejecuta en PowerShell:

```powershell
winget install astral-sh.uv
winget install GitHub.cli
```
Cierra y abre la terminal, y luego:

```powershell
uv tool install ruff
uv tool install jupyterlab
gh auth login
```

## Verificación
```powershell
uv --version
gh --version
ruff --version
```

## Extensiones de VS Code
Python, Pylance, Ruff, Jupyter, Docker.

## Cuentas
- **GitHub:** para publicar el portafolio.
- **Anthropic Console:** crea una clave de API y configura un límite de gasto mensual. Guárdala como variable de entorno `ANTHROPIC_API_KEY`, nunca dentro del código ni en Git.

## Por proyecto
```powershell
uv init nombre-proyecto
cd nombre-proyecto
uv add pydantic httpx
uv add --dev pytest
uv run pytest
```
Dependencias típicas: `fastapi`, `uvicorn`, `pandas`, `sqlalchemy`, `anthropic`.

## Base vectorial (fase 4)
```powershell
docker run -d --name pgvector -e POSTGRES_PASSWORD=dev -p 5432:5432 pgvector/pgvector:pg17
```
