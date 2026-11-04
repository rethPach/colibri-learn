import sys
import os
import inspect
from abc import ABC

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../workspace")))

def main():
    print("┌─── 🧠 MODAL DE EVALUACIÓN: [VERIFICADOR CAPÍTULO 3 - GÖDEL] ────────────────┐")
    try:
        import lab_03_godel_abstraccion as lab
    except Exception as e:
        print(f"│ [ERROR DE CARGA] No se pudo importar lab_03_godel_abstraccion.py: {e}")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if not hasattr(lab, "SistemaFormal") or not issubclass(lab.SistemaFormal, ABC):
        print("│ [PISTA SOCRÁTICA 1] `SistemaFormal` debe heredar de `abc.ABC`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    try:
        lab.SistemaFormal()
        print("│ [PISTA SOCRÁTICA 2] ¡Pudiste instanciar `SistemaFormal()` directamente!")
        print("│ Como demostró Gödel, el contrato abstracto está incompleto por sí solo.")
        print("│ Marca `demostrar(self, enunciado)` con `@abstractmethod`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)
    except TypeError:
        pass

    aritmetica = lab.SistemaAritmetico()
    meta = lab.MetaSistemaGodel()

    if not isinstance(aritmetica, lab.SistemaFormal) or not isinstance(meta, lab.SistemaFormal):
        print("│ [PISTA SOCRÁTICA 3] Tanto `SistemaAritmetico` como `MetaSistemaGodel`")
        print("│ deben implementar el contrato `SistemaFormal`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    enunciado_godel = "G: Esta proposicion no es demostrable en SistemaAritmetico"
    if aritmetica.demostrar(enunciado_godel) != "INCOMPLETO":
        print("│ [PISTA SOCRÁTICA 4] Cuando `SistemaAritmetico` recibe el enunciado `G`,")
        print("│ debe reconocer su límite y devolver `'INCOMPLETO'`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if meta.demostrar(enunciado_godel) != "VERDADERO_DESDE_METANIVEL":
        print("│ [PISTA SOCRÁTICA 5] `MetaSistemaGodel` observa desde afuera y demuestra")
        print("│ la verdad de `G` devolviendo `'VERDADERO_DESDE_METANIVEL'`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    print("│ ✅ [VEREDICTO: SUPERADO]")
    print("│ Has dejado caer la tiza blanca en Königsberg (1930).")
    print("│ • Comprendiste que la abstracción (`ABC`) es humildad matemática hecha código.")
    print("└─────────────────────────────────────────────────────────────────────────────┘")
    sys.exit(0)

if __name__ == "__main__":
    main()
