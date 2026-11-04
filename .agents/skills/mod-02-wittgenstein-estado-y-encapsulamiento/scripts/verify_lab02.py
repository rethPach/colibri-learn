import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../workspace")))

def main():
    print("┌─── 🧠 MODAL DE EVALUACIÓN: [VERIFICADOR CAPÍTULO 2 - WITTGENSTEIN] ─────────┐")
    try:
        import lab_02_tractatus_encapsulamiento as lab
    except Exception as e:
        print(f"│ [ERROR DE CARGA] No se pudo importar lab_02_tractatus_encapsulamiento.py: {e}")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    cuaderno = lab.CuadernoTractatus("Ludwig Wittgenstein")

    # Verificar que las proposiciones internas estén encapsuladas (privadas)
    if hasattr(cuaderno, "proposiciones"):
        print("│ [PISTA SOCRÁTICA 1] 'De lo que no se puede hablar, hay que callar.'")
        print("│ El atributo `proposiciones` sigue siendo público. Encapsúlalo como")
        print("│ `self.__proposiciones` para evitar que el mundo exterior lo corrompa.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    # Verificar que no se puedan inyectar proposiciones vacías o incoherentes
    try:
        cuaderno.registrar_hecho("")
        print("│ [PISTA SOCRÁTICA 2] Permitiste registrar un hecho vacío ('').")
        print("│ Lanza un `ValueError` cuando alguien intente registrar ruido sin sentido.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)
    except ValueError:
        pass

    cuaderno.registrar_hecho("1. El mundo es todo lo que acaece.")
    if len(cuaderno.hechos) != 1:
        print("│ [PISTA SOCRÁTICA 3] Expón una propiedad `@property def hechos(self)`")
        print("│ que devuelva una tupla inmutable (`tuple(self.__proposiciones)`).")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if not isinstance(cuaderno.hechos, tuple):
        print("│ [PISTA SOCRÁTICA 4] `cuaderno.hechos` devuelve una lista mutable.")
        print("│ Si alguien hace `cuaderno.hechos.append('basura')`, romperá tu cápsula.")
        print("│ Devuelve `tuple(self.__proposiciones)` para garantizar inmutabilidad externa.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    print("│ ✅ [VEREDICTO: SUPERADO]")
    print("│ Has cerrado el cuaderno de hule negro en el Río Piave (1918).")
    print("│ • El estado interno está protegido tras el silencio del encapsulamiento.")
    print("│ • El mundo exterior solo interactúa mediante hechos validados e inmutables.")
    print("└─────────────────────────────────────────────────────────────────────────────┘")
    sys.exit(0)

if __name__ == "__main__":
    main()
