---
name: curriculum-architect
description: >-
  Meta-skill para ingerir un tema o material narrativo desde la carpeta inbox/ o
  el prompt del usuario, y transpilarlo automáticamente en un curso versionado
  con syllabus.md, perfil del estudiante, laboratorios de código y skills
  modulares en .agents/skills/. Úsala cuando course/syllabus.md no exista o
  cuando el usuario pida reestructurar o expandir el currículo.
---

# Curriculum Architect (Meta-Skill de Ingesta y Diseño Curricular)

Esta skill convierte cualquier texto base, libro, apunte en `inbox/` o tema abstracto en una arquitectura viva de aprendizaje dentro del repositorio Git.

## Procedimiento de Ingesta y Transpilación

1. **Análisis de Fuentes (`inbox/`)**:
   - Inspecciona todos los archivos en `inbox/`.
   - Extrae el hilo conductor narrativo y mapea cada unidad/capítulo con los conceptos técnicos objetivo (ej. Filosofía de la Lógica → Paradigma Orientado a Objetos).

2. **Generación del Mapa Curricular (`course/syllabus.md`)**:
   - Crea `course/syllabus.md` con:
     - El grafo completo de aprendizaje en formato Mermaid (`flowchart TD` o `LR`).
     - La tabla de módulos, conectando **Coordenada Histórica/Filosófica** ↔ **Concepto de Ingeniería / POO** ↔ **Laboratorio Práctico**.

3. **Inicialización del Estado del Estudiante (`student/`)**:
   - Crea `student/profile.md` con el perfil cognitivo inicial, estilo de aprendizaje (Narrativo + Construccionista) y bitácora de reflexiones.
   - Crea `student/progress.json` con el estado de cada módulo (`locked`, `in_progress`, `completed`), puntuación de dominio y hash del commit correspondiente.

4. **Compilación de Skills Modulares (`.agents/skills/mod-XX-.../`)**:
   - Por cada módulo del curso, genera su carpeta en `.agents/skills/mod-XX-<slug>/` con:
     - `SKILL.md`: Guía pedagógica del módulo, puente conceptual entre la escena histórica y la arquitectura de software, preguntas socráticas clave y criterios de aprobación.
     - `references/`: El fragmento narrativo original o material de lectura profunda para consulta bajo demanda.
     - `scripts/verify_labXX.py`: Script automatizado en Python que evalúa el archivo de práctica del estudiante en `workspace/` y devuelve retroalimentación estilo "Modal de Consciencia".

5. **Despliegue del Primer Laboratorio (`workspace/`)**:
   - Crea el archivo de reto inicial en `workspace/` listo para que el estudiante (o el tutor junto a él) comience a experimentar de inmediato.

6. **Versionado en Git**:
   - Registra el nacimiento del curso con un commit semántico:
     `git add . && git commit -m "feat(curriculum): transpile inbox sources into modular skills and labs"`
