# Plan de 12 semanas

**Objetivo:** conseguir trabajo como AI Engineer (o backend con foco en IA). Todo el plan se mide por eso: proyectos públicos que se puedan mostrar en una entrevista y búsqueda activa desde la semana 3, no al final.

**Punto de partida:** programador con experiencia en otros lenguajes, sin Python. No hace falta aprender a programar, sí aprender Python bien y rápido.

**Ritmo:** ~20 h/semana (60 % construir, 25 % estudiar, 15 % búsqueda de trabajo). Si tienes menos horas, estira cada fase; no saltes la búsqueda. Cierra cada semana con una nota de 15 min en `notas/semana-NN.md`.

## Fase 1: Python (semanas 1-2)
- [ ] Semana 1: sintaxis y modelo de datos (listas, dicts, sets, slicing, f-strings, excepciones, `pathlib`), luego `fase1-python/semana-01`: comprensiones, generadores, context managers, decoradores, `dataclasses`, `pydantic`. Tipado en todo.
- [ ] Semana 2: `async/await`, `pytest` (fixtures, parametrize), `ruff`, estructura de paquete con `uv`, GitHub Actions.
- [ ] **Proyecto 1:** el CLI `organizador`. Ya existe una versión base: léela hasta entender cada línea y agrégale tú una función nueva con su test (por ejemplo `--por-fecha` o `--deshacer`). Si no lo escribiste tú, no lo puedes defender en una entrevista.
- Terminado cuando: tests en verde, `ruff` limpio, CI pasando en GitHub, README publicado.

## Fase 2: APIs (semana 3)
- [ ] FastAPI, `httpx`, validación con `pydantic`, Docker.
- [ ] **Proyecto 2:** API pequeña con un par de endpoints, tests y `Dockerfile`. Es la base sobre la que se monta el asistente de la fase 3, no un proyecto aparte.
- Terminado cuando: `docker compose up` la levanta y hay tests de endpoints.

## Fase 3: LLMs aplicados (semanas 4-5)
- [ ] Semana 4: API de Claude (mensajes, system prompts, streaming, salida estructurada con `pydantic`).
- [ ] Semana 5: tool use, prompt caching, reintentos y manejo de errores, costo por llamada.
- [ ] **Proyecto 3:** asistente con herramientas expuesto por la API de la fase 2.
- Terminado cuando: tests con cliente simulado (mock) y costo por conversación documentado.

## Fase 4: RAG y evaluación (semanas 6-8) — el proyecto estrella
- [ ] Semana 6: embeddings, `pgvector`, chunking.
- [ ] Semana 7: recuperación, reranking, citas de fuentes.
- [ ] Semana 8: evals (dataset de preguntas, métricas, regresiones).
- [ ] **Proyecto 4:** RAG sobre documentos reales con reporte de métricas reproducible.
- Terminado cuando: un solo comando genera el reporte (exactitud, latencia, costo).

## Fase 5: Agentes y producción (semanas 9-11)
- [ ] Semana 9: bucle de agente, herramientas, MCP.
- [ ] Semana 10: observabilidad (trazas, logs), control de costos, seguridad básica (prompt injection).
- [ ] Semana 11: despliegue y demo pública.
- [ ] **Proyecto 5:** agente desplegado con URL pública.
- Terminado cuando: la demo funciona en línea y el README explica arquitectura y límites.

## Semana 12: cierre
- [ ] Pulir READMEs (problema, demo, arquitectura, números).
- [ ] Ensayar la explicación de cada proyecto en 2 minutos.

## En paralelo: búsqueda de trabajo
- [ ] Semana 2: perfil de GitHub con README y LinkedIn con el titular apuntando a AI Engineering.
- [ ] Semana 3: CV reescrito (ver `cv/CHECKLIST.md`). Los proyectos se agregan a medida que se terminan.
- [ ] Desde semana 4: postular a 5-10 ofertas por semana (junior/semi-senior backend Python, AI/ML engineer, LLM engineer). Registrar en `cv/postulaciones.md`.
- [ ] Desde semana 6: preparación de entrevistas: 3 ejercicios de código por semana en Python (nivel fácil-medio) y diseño de sistemas con LLMs (RAG, costos, latencia, evals).
- [ ] Publicar AutoLog y la plataforma financiera (o versiones sanitizadas) si los acuerdos lo permiten.
