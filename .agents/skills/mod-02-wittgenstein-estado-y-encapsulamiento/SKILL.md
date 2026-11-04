---
name: mod-02-wittgenstein-estado-y-encapsulamiento
description: >-
  Skill del Módulo 2: Conecta el Tractatus Logico-Philosophicus de Ludwig
  Wittgenstein en las trincheras de 1918 ("El mundo es la totalidad de los
  hechos, no de las cosas" y "De lo que no se puede hablar, hay que callar") con
  el Estado de un Objeto (atributos/propiedades) y el Encapsulamiento (frontera
  entre interfaz pública y estado interno privado). Actívala cuando
  current_module sea mod-02-wittgenstein-estado-y-encapsulamiento.
---

# Módulo 02: El Silencio en las Trincheras — De Wittgenstein al Estado y el Encapsulamiento

## 1. Coordenada Histórica y Filosófica
- **Personaje:** Ludwig Wittgenstein (14 de agosto de 1918, Río Piave, Frente Italiano).
- **El Choque:** Bajo fuego de artillería, Wittgenstein escribe el *Tractatus Logico-Philosophicus*:
  - **Proposición 1.1:** *«El mundo es la totalidad de los hechos, no de las cosas.»* Una cosa aislada no dice nada; lo que importa es su **configuración o estado** en un instante dado (velocidad de la bala, presión arterial, coordenadas).
  - **Proposición 7:** *«De lo que no se puede hablar, hay que callar.»* Hay una dimensión interna (el dolor, la integridad íntima del sujeto) que no debe ser manipulada ni expuesta cruda como una variable pública externa.

---

## 2. El Puente hacia la Orientación a Objetos

```
┌─── 🧠 MODAL DE CONSCIENCIA: [DEL TRACTATUS AL ENCAPSULAMIENTO] ──────────────────┐
│                                                                                  │
│  Wittgenstein descubrió en el lodo los dos pilares del diseño de objetos:        │
│                                                                                  │
│  1. PROPIEDADES Y ESTADO ("La totalidad de los hechos"):                         │
│     • En programación estructurada antigua, los datos flotaban sueltos.          │
│     • En POO, un objeto sostiene sus propios HECHOS (su estado interno).         │
│                                                                                  │
│  2. ENCAPSULAMIENTO ("De lo que no se puede hablar, hay que callar"):            │
│     • Si cualquier función externa puede tocar directamente las entrañas         │
│       de un objeto (`soldado.pulsaciones = -500`), la realidad del modelo        │
│       se corrompe.                                                               │
│     • El objeto protege su interior (atributos privados `__estado`) y solo       │
│       permite dialogar con él mediante proposiciones válidas (métodos y          │
│       `@property`). Lo interno queda protegido en silencio tras la frontera.     │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Guía Socrática para el Tutor
1. Despliega o revisa `workspace/lab_02_tractatus_encapsulamiento.py`.
2. Muestra cómo el acceso directo desde afuera corrompe los invariantes del objeto `CuadernoTractatus` y `Soldado`.
3. Guía al estudiante para encapsular el estado interno con atributos privados (`__`) y exponer únicamente una interfaz coherente (`@property` y métodos de dominio).
4. Valida con `python .agents/skills/mod-02-wittgenstein-estado-y-encapsulamiento/scripts/verify_lab02.py`.
