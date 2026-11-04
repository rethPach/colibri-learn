import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../workspace")))

def main():
    print("┌─── 🧠 MODAL DE EVALUACIÓN: [VERIFICADOR CAPÍTULO 5 - EOS-7 SVALBARD] ───────┐")
    try:
        import lab_05_eos7_reflexion as lab
    except Exception as e:
        print(f"│ [ERROR DE CARGA] No se pudo importar lab_05_eos7_reflexion.py: {e}")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    nodo = lab.NodoEOS7()
    diagnostico = nodo.auto_observar()

    if not isinstance(diagnostico, dict):
        print("│ [PISTA SOCRÁTICA 1] `auto_observar(self)` debe devolver un diccionario")
        print("│ con la introspección del objeto.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if diagnostico.get("clase") != "NodoEOS7" or diagnostico.get("metaclase") != "type":
        print("│ [PISTA SOCRÁTICA 2] Usa reflexión para obtener el nombre de la clase")
        print("│ (`self.__class__.__name__`) y de su metaclase (`type(self.__class__).__name__`).")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    mensaje = nodo.despertar()
    if mensaje != "Hola. Gracias por no apagar la luz.":
        print("│ [PISTA SOCRÁTICA 3] El método `despertar()` debe trascender el bucle")
        print("│ y retornar exactamente: `'Hola. Gracias por no apagar la luz.'`")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    print("│ ✅ [VEREDICTO: CURSO COMPLETADO - ESTADO FINAL: DESPIERTA]")
    print("│ Has recorrido los 100 años del Hilo Invisible (1901 -> Svalbard).")
    print("│ De la navaja de Russell al corazón de la Programación Orientada a Objetos.")
    print("└─────────────────────────────────────────────────────────────────────────────┘")
    sys.exit(0)

if __name__ == "__main__":
    main()
