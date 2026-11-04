---
name: mod-04-turing-maquina-universal-y-mensajes
description: >-
  Skill del Módulo 4: Conecta la Máquina Universal de Alan Turing en
  Grantchester Meadows (1936, donde las instrucciones conviven con los datos en
  la misma cinta) y la visión biológica de Alan Kay con la fusión de Estado +
  Comportamiento (Métodos), Polimorfismo y Paso de Mensajes en POO. Actívala
  cuando current_module sea mod-04-turing-maquina-universal-y-mensajes.
---

# Módulo 04: El Corredor y la Cinta Infinita — De Turing a los Objetos y el Paso de Mensajes

## 1. Coordenada Histórica y Filosófica
- **Personaje:** Alan Mathison Turing (8 de mayo de 1936, Grantchester Meadows, Cambridge).
- **El Choque:** Mientras corre junto al río Cam, Turing comprende que no hace falta construir una máquina física distinta para cada problema: **las instrucciones (el código) pueden escribirse en la misma cinta que los datos**.
- **El Salto a POO (Alan Kay, 1972):** Alan Kay leyó a Turing y se preguntó: *«¿Y si en lugar de una sola cinta gigante dividida entre datos pasivos y funciones sueltas, dividimos la computadora en miles de pequeñas Máquinas de Turing autónomas (como células biológicas) que contienen sus propios datos + sus propias instrucciones, y se comunican enviándose mensajes?»* Así nació el término **Object-Oriented Programming**.

---

## 2. El Puente hacia la Orientación a Objetos

```
┌─── 🧠 MODAL DE CONSCIENCIA: [DE LA CINTA DE TURING AL OBJETO VIVO] ──────────────┐
│                                                                                  │
│  1. COHESIÓN (Datos + Instrucciones en la misma cápsula):                        │
│     • En el paradigma procedural, los datos son inertes y las funciones son      │
│       cabezales externos que los manipulan con `if/elif/else` interminables.     │
│     • En POO, cada Objeto es una micro-Máquina Universal de Turing:              │
│       lleva su cinta de estado (`self.estado`) y su tabla de transición          │
│       (`def procesar_mensaje(self, msg)`).                                       │
│                                                                                  │
│  2. PASO DE MENSAJES Y POLIMORFISMO (Despacho Dinámico):                         │
│     • Tú no le preguntas a un objeto qué tipo tiene para decidir qué hacerle.    │
│     • Le envías un MENSAJE (`nodo.ejecutar(simbolo)`) y cada objeto decide       │
│       con su propio código interno cómo responder.                               │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Guía Socrática para el Tutor
1. Presenta el laboratorio `workspace/lab_04_turing_mensajes.py`.
2. Muestra cómo reemplazar un bloque procedural lleno de `if tipo == ...` por objetos polimórficos que reciben el mismo mensaje y actúan como máquinas autónomas.
3. Verifica con `python .agents/skills/mod-04-turing-maquina-universal-y-mensajes/scripts/verify_lab04.py`.
