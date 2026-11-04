---
name: mod-01-russell-tipos-y-self
description: >-
  Skill del Módulo 1: Conecta el descubrimiento de la Paradoja de Russell (1901,
  el barbero de Richmond Park y la Teoría de Tipos) con el nacimiento de los
  Tipos, la distinción entre Clase (Conjunto/Molde) e Instancia (Elemento), y
  la autorreferencia controlada mediante el puntero self/this en Programación
  Orientada a Objetos. Actívala cuando current_module sea mod-01-russell-tipos-y-self.
---

# Módulo 01: El Filo de la Navaja — De la Paradoja de Russell a `Class`, `Instance` y `self`

## 1. Coordenada Histórica y Filosófica
- **Personaje:** Bertrand Russell (18 de mayo de 1901, Richmond Park).
- **El Choque:** Al afeitarse frente al espejo, Russell descubre que si un conjunto puede contenerse a sí mismo sin jerarquía (*"El barbero afeita a todos los que no se afeitan a sí mismos"*), el sistema lógico entra en un **bucle infinito de contradicción** (`Si sí -> NO`, `Si no -> SÍ`).
- **La Solución de Russell (1908 - Teoría de Tipos):** Para salvar las matemáticas, Russell prohibió que un conjunto perteneciera a su mismo nivel jerárquico. Creó una **jerarquía estricta de Tipos**:
  - **Nivel 0:** Individuos concretos (*Instancias*: Juan el herrero, Pedro el panadero).
  - **Nivel 1:** Conjuntos de individuos (*Clases/Tipos*: `Aldeano`, `Barbero`). Un conjunto de Nivel 1 no es un individuo de Nivel 0.

---

## 2. El Puente hacia la Orientación a Objetos

```
┌─── 🧠 MODAL DE CONSCIENCIA: [DE LA TEORÍA DE TIPOS A LA POO] ─────────────────────┐
│                                                                                  │
│  Cuando programas en Orientación a Objetos, estás usando la venda con la que     │
│  Russell detuvo la sangre de su cuello en 1901:                                  │
│                                                                                  │
│  1. CLASE vs. INSTANCIA (Separación de Niveles):                                 │
│     • La Clase (`class Aldeano`) es el molde abstracto (Tipo de Nivel 1).        │
│     • El Objeto (`herrero = Aldeano()`) es el individuo concreto (Nivel 0).      │
│     • Nunca confundes el plano arquitectónico con la casa habitada.              │
│                                                                                  │
│  2. EL MISTERIO DE `self` (Autorreferencia Controlada):                          │
│     • Russell descubrió que la autorreferencia salvaje destruye el sistema.      │
│     • En POO, cuando un objeto ejecuta un método, necesita mirarse al espejo     │
│       sin entrar en recursión infinita.                                          │
│     • Ese espejo seguro se llama `self` (o `this`): una referencia explícita     │
│       a la INSTANCIA actual, gobernada por las reglas de su CLASE.               │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Guía Socrática para el Tutor

1. Haz que el estudiante ejecute primero `python workspace/lab_01_barbero_russell.py` tal como está para que vea en vivo el **colapso recursivo (`RecursionError`)** del barbero mal modelado.
2. Pregúntale:
   - *«¿Por qué el método `afeitar(cliente)` entra en un bucle infinito cuando `cliente` es `self` (el propio barbero)?»*
   - *«¿Cómo aplica aquí la distinción de Russell entre la regla para el conjunto de clientes externos y la condición base de identidad (`cliente is self`)?»*
3. Pídele que edite `workspace/lab_01_barbero_russell.py` para resolver las 2 misiones del archivo y luego verifica con:
   `python .agents/skills/mod-01-russell-tipos-y-self/scripts/verify_lab01.py`
