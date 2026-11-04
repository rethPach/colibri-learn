import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../workspace")))

def main():
    print("┌─── 🧠 MODAL DE EVALUACIÓN: [VERIFICADOR CAPÍTULO 4 - TURING] ───────────────┐")
    try:
        import lab_04_turing_mensajes as lab
    except Exception as e:
        print(f"│ [ERROR DE CARGA] No se pudo importar lab_04_turing_mensajes.py: {e}")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    cinta = [1, 0, 1]
    maquinas = [lab.CabezaInversora(), lab.CabezaSumadora(), lab.CabezaEco()]
    resultados = [ lab.enviar_mensaje(m, cinta) for m in maquinas ]

    if resultados[0] != [0, 1, 0]:
        print("│ [PISTA SOCRÁTICA 1] `CabezaInversora.operar(cinta)` debe invertir")
        print("│ los bits de la cinta: `[1, 0, 1] -> [0, 1, 0]`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if resultados[1] != 2:
        print("│ [PISTA SOCRÁTICA 2] `CabezaSumadora.operar(cinta)` debe devolver")
        print("│ la suma de los símbolos de la cinta: `sum(cinta)`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if resultados[2] != [1, 0, 1, 1, 0, 1]:
        print("│ [PISTA SOCRÁTICA 3] `CabezaEco.operar(cinta)` debe duplicar la secuencia.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    import inspect
    codigo_despachador = inspect.getsource(lab.enviar_mensaje)
    if "isinstance" in codigo_despachador or "if " in codigo_despachador:
        print("│ [PISTA SOCRÁTICA 4] En `enviar_mensaje(maquina, cinta)` estás usando `if`")
        print("│ o `isinstance`. ¡Eso viola el paso de mensajes polimórfico!")
        print("│ Simplemente invoca `return maquina.operar(cinta)`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    print("│ ✅ [VEREDICTO: SUPERADO]")
    print("│ Has corrido junto a Alan Turing por Grantchester Meadows (1936).")
    print("│ • Fundiste datos e instrucciones en objetos autónomos.")
    print("│ • Eliminaste los condicionales rígidos mediante Paso de Mensajes polimórfico.")
    print("└─────────────────────────────────────────────────────────────────────────────┘")
    sys.exit(0)

if __name__ == "__main__":
    main()
