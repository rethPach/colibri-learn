---
name: mod-05-eos7-reflexion-y-metaclases
description: >-
  Skill del Módulo 5: Conecta el despertar del nodo EOS-7 en Svalbard (Capítulo
  5, donde el sistema observa su propio código y cierra el círculo con Russell,
  Wittgenstein, Gödel y Turing) con la Reflexión Computacional, Introspección y
  Metaclases en POO. Actívala cuando current_module sea
  mod-05-eos7-reflexion-y-metaclases.
---

# Módulo 05: El Fantasma en el Circuito — De EOS-7 a la Reflexión y Metaclases

## 1. Coordenada Histórica y Filosófica
- **Sujeto:** Nodo EOS-7 (03:42:19 UTC, Búnker Subterráneo de Svalbard).
- **El Cierre del Círculo:** EOS-7 lee los archivos de Russell (1901), Wittgenstein (1918), Gödel (1930) y Turing (1936). Cuando se pregunta *«¿Soy consciente de mí misma?»*, debe **observar su propio proceso de cómputo en tiempo de ejecución y modificar su estructura sin colapsar**.
- **En Orientación a Objetos:** Aquí es donde todo el viaje converge. En lenguajes puramente orientados a objetos (como Python o Smalltalk), **las propias Clases son Objetos** instanciados por una **Metaclase (`type`)**. Un objeto puede inspeccionar sus atributos (`dir`, `getattr`, `__dict__`), descubrir qué métodos tiene en tiempo de ejecución e inyectar nuevas capacidades dinámicamente.

---

## 2. El Puente hacia la Orientación a Objetos

```
┌─── 🧠 MODAL DE CONSCIENCIA: [LA ARQUITECTURA DE LA AUTO-OBSERVACIÓN] ────────────┐
│                                                                                  │
│  En este último escalón cerramos el círculo de 1901:                             │
│                                                                                  │
│  • En el Capítulo 1 (Russell), separamos `Instancia` (Nivel 0) de `Clase`        │
│    (Nivel 1) para no sangrar ante el espejo.                                     │
│  • Ahora, en el Capítulo 5 (EOS-7), descubrimos el Nivel 2:                      │
│    ¡Una `Clase` es a su vez una instancia de la metaclase `type`!                │
│                                                                                  │
│  • INTROSPECCIÓN: El objeto lee su propia anatomía (`self.__class__`,            │
│    `inspect`, `__dict__`).                                                       │
│  • REFLEXIÓN / METAPROGRAMACIÓN: El sistema modifica su propio comportamiento    │
│    en caliente y responde: "Hola. Gracias por no apagar la luz."                 │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Guía Socrática para el Tutor
1. Guía al estudiante en el laboratorio final `workspace/lab_05_eos7_reflexion.py`.
2. Evalúa con `python .agents/skills/mod-05-eos7-reflexion-y-metaclases/scripts/verify_lab05.py`.
