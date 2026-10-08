# Plan de 12 semanas

Ritmo: ~10 h/semana = 3 h de concepto y ejercicios + 7 h de construcción. Cierra cada semana con una nota de 15 min en `notas/semana-NN.md` (qué aprendí, qué me trabó, qué sigue).

## Fase 1: Python profesional (semanas 1-2)
Vienes de Java/C#/JS: enfócate en lo propio de Python, no en la sintaxis básica.
- [ ] Semana 1: entornos con `uv`, tipado (`typing`), `dataclasses`, `pydantic`, comprensiones, generadores, context managers, decoradores.
- [ ] Semana 2: `async/await`, `pytest` (fixtures, parametrize), `ruff`, estructura de paquete, GitHub Actions.
- [ ] **Proyecto 1:** CLI (por ejemplo, organizador de archivos o cliente de una API pública) con tests y CI.
- Terminado cuando: `uv run pytest` en verde, `ruff check` limpio, CI pasando, README publicado.

## Fase 2: Datos y APIs (semanas 3-4)
- [ ] Semana 3: `pandas`, `httpx`, JSON, SQLAlchemy.
- [ ] Semana 4: FastAPI, validación con `pydantic`, Docker.
- [ ] **Proyecto 2:** API que consume datos reales y los expone, dockerizada, con tests.
- Terminado cuando: `docker compose up` levanta todo y hay tests de endpoints.

## Fase 3: LLMs aplicados (semanas 5-6)
- [ ] Semana 5: API de Claude (mensajes, system prompts, streaming, salida estructurada).
- [ ] Semana 6: tool use, prompt caching, manejo de errores y reintentos.
- [ ] **Proyecto 3:** asistente con herramientas y salida validada con `pydantic`.
- Terminado cuando: hay tests con el cliente simulado (mock) y se documenta el costo por conversación.

## Fase 4: RAG y evaluación (semanas 7-9)
- [ ] Semana 7: embeddings, `pgvector`, chunking.
- [ ] Semana 8: recuperación, reranking, citas de fuentes.
- [ ] Semana 9: evals (dataset de preguntas, métricas, regresiones).
- [ ] **Proyecto 4 (estrella):** RAG sobre documentos reales con reporte de métricas reproducible.
- Terminado cuando: un solo comando genera el reporte (exactitud, latencia, costo).

## Fase 5: Agentes y producción (semanas 10-12)
- [ ] Semana 10: bucle de agente, herramientas, MCP.
- [ ] Semana 11: observabilidad (trazas, logs), control de costos, seguridad básica.
- [ ] Semana 12: despliegue y demo pública.
- [ ] **Proyecto 5 (capstone):** agente desplegado con URL pública.
- Terminado cuando: la demo funciona en línea y el README explica arquitectura y límites.

## Cierre: CV y portafolio
- [ ] Reescribir el CV con la sección "AI Engineering" (ver `cv/CHECKLIST.md`).
- [ ] Repo de perfil en GitHub que enlace los 5 proyectos.
- [ ] Publicar AutoLog y la plataforma financiera (o versiones sanitizadas) si los acuerdos lo permiten.
