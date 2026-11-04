---
name: mod-03-godel-abstraccion-y-contratos
description: >-
  Skill del Módulo 3: Conecta el Teorema de Incompletitud de Kurt Gödel en
  Königsberg (1930) con el principio de Abstracción, Clases Base Abstractas
  (ABC), Interfaces y Contratos en POO. Actívala cuando current_module sea
  mod-03-godel-abstraccion-y-contratos.
---

# Módulo 03: La Jaula de los Axiomas — De Gödel a la Abstracción y los Contratos

## 1. Coordenada Histórica y Filosófica
- **Personaje:** Kurt Gödel (7 de septiembre de 1930, Königsberg).
- **El Choque:** David Hilbert soñaba con un sistema único, cerrado y monolítico que demostrara toda verdad. Gödel demuestra que **todo sistema formal tiene afirmaciones que no puede resolver desde adentro** sin abrirse a un nivel superior de abstracción.
- **La Lección para el Software:** Si intentas construir una clase monolítica ("Clase Dios" / *HilbertSystem*) que contenga todas las reglas concretas del universo, tu código se volverá rígido e incompleto ante el primer caso nuevo.

---

## 2. El Puente hacia la Orientación a Objetos

```
┌─── 🧠 MODAL DE CONSCIENCIA: [DE LA INCOMPLETITUD A LA ABSTRACCIÓN] ─────────────┐
│                                                                                  │
│  Gödel destruyó el monolito de Hilbert; en POO destruimos las clases rígidas     │
│  mediante la ABSTRACCIÓN (`abc.ABC` y `@abstractmethod`):                        │
│                                                                                  │
│  1. LA INTERFAZ ES UN AXIOMA ABIERTO:                                            │
│     • Una Clase Abstracta (`SistemaFormal(ABC)`) declara QUÉ operación existe    │
│       (`@abstractmethod def evaluar(self, proposicion): pass`), pero admite      │
│       con humildad gödeliana que ella misma es INCOMPLETA: no puede              │
│       instanciarse sola ni dictar un único algoritmo cerrado.                    │
│                                                                                  │
│  2. EXTENSIBILIDAD SIN MODIFICACIÓN (Principio Abierto/Cerrado):                 │
│     • Cuando aparece una verdad que el sistema actual no puede demostrar,        │
│       creamos una nueva subclase concreta que implementa el contrato sin         │
│       destruir el sistema anterior.                                              │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Guía Socrática para el Tutor
1. Revisa con el estudiante `workspace/lab_03_godel_abstraccion.py`.
2. Pídele que transforme la clase rígida `MaquinaHilbert` en una arquitectura extensible basada en `abc.ABC` y `@abstractmethod`.
3. Ejecuta `python .agents/skills/mod-03-godel-abstraccion-y-contratos/scripts/verify_lab03.py`.
