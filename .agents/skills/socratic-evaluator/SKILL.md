---
name: socratic-evaluator
description: >-
  Meta-skill para conducir sesiones de tutoría socrática, ejecutar los scripts
  de validación de laboratorios en workspace/, actualizar el progreso del
  estudiante en student/progress.json y auto-modificar las skills del
  repositorio cuando se detectan mejoras pedagógicas. Úsala durante el Modo
  Tutoría Activa.
---

# Socratic Evaluator & Autopoietic Loop

Esta skill gobierna cómo el agente enseña, evalúa y evoluciona el repositorio durante las sesiones de estudio.

## Flujo de Evaluación y Tutoría

1. **Diagnóstico de Contexto**:
   - Lee `student/progress.json` para identificar el `current_module`.
   - Lee el archivo `.agents/skills/<current_module>/SKILL.md`.

2. **Ciclo Socrático en 3 Pasos**:
   - **Paso A (Inmersión Narrativa)**: Presenta el dilema del personaje histórico (Russell, Wittgenstein, Gödel, Turing o EOS-7) usando el formato de *Escena en Dos Planos* y el *Modal de Consciencia*.
   - **Paso B (Puente hacia el Código)**: Muestra cómo ese choque filosófico dio origen a un mecanismo concreto de la Programación Orientada a Objetos.
   - **Paso C (Reto en `workspace/`)**: Invita al estudiante a inspeccionar, ejecutar y reparar el archivo del laboratorio activo en `workspace/`.

3. **Verificación Ejecutable**:
   - Cuando el estudiante modifique el código o proponga una solución, ejecuta:
     `python .agents/skills/<current_module>/scripts/verify_labXX.py`
   - Si el script falla, no le escribas la solución completa de inmediato: usa la pista socrática que arroja el verificador.
   - Si el script pasa (`[VEREDICTO: SUPERADO]`), desbloquea el siguiente módulo.

4. **Cierre de Módulo y Autopoiesis en Git**:
   - Actualiza `student/progress.json` marcando el módulo como `completed` y el siguiente como `in_progress`.
   - Registra en `student/profile.md` las intuiciones o preguntas destacadas del alumno.
   - Si durante la lección descubriste una mejor metáfora o ejemplo, edita el `SKILL.md` del módulo para conservar ese aprendizaje en el repositorio.
   - Despliega el laboratorio del siguiente módulo en `workspace/` y ejecuta:
     `git add . && git commit -m "feat(mastery): complete <module_id> and unlock next stage"`
