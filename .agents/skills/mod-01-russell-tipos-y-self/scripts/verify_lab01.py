import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../workspace")))

def main():
    print("┌─── 🧠 MODAL DE EVALUACIÓN: [VERIFICADOR CAPÍTULO 1 - RUSSELL] ──────────────┐")
    try:
        import lab_01_barbero_russell as lab
    except Exception as e:
        print(f"│ [ERROR DE CARGA] No se pudo importar lab_01_barbero_russell.py: {e}")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    try:
        herrero = lab.Aldeano("Herrero", se_afeita_solo=False)
        panadero = lab.Aldeano("Panadero", se_afeita_solo=True)
        russell = lab.Barbero("Bertrand")
    except Exception as e:
        print(f"│ [FALLO DE INSTANCIACIÓN] Revisa el __init__ de Aldeano y Barbero: {e}")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    # 1. Verificar jerarquía de tipos (Barbero es subtipo de Aldeano o instancia válida)
    if not isinstance(russell, lab.Aldeano):
        print("│ [PISTA SOCRÁTICA 1] En la Teoría de Tipos de Russell, un Barbero también")
        print("│ es un habitante del pueblo. Haz que `Barbero` herede de `Aldeano`.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    # 2. Verificar comportamiento con otros aldeanos
    try:
        res_herrero = russell.afeitar(herrero)
        res_panadero = russell.afeitar(panadero)
    except RecursionError:
        print("│ [COLAPSO LÓGICO: RecursionError] ¡La navaja sigue cortando el cuello!")
        print("│ El barbero cayó en bucle infinito al evaluar a los aldeanos.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if not herrero.afeitado:
        print("│ [PISTA SOCRÁTICA 2] El herrero NO se afeita solo (`se_afeita_solo=False`).")
        print("│ El barbero DEBE afeitarlo (`cliente.afeitado = True`).")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if panadero.afeitado:
        print("│ [PISTA SOCRÁTICA 3] El panadero SÍ se afeita en casa (`se_afeita_solo=True`).")
        print("│ El barbero NO debe afeitarlo directamente en la barbería.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    # 3. La prueba de fuego: Autorreferencia (russell.afeitar(russell))
    try:
        res_self = russell.afeitar(russell)
    except RecursionError:
        print("│ [VÉRTIGO LÓGICO: RecursionError EN AUTORREFERENCIA]")
        print("│ Cuando `russell.afeitar(russell)` se ejecuta, `cliente is self`.")
        print("│ Rompe la paradoja detectando la identidad (`if cliente is self:`)")
        print("│ para que el barbero reconozca su propio reflejo sin llamarse recursivamente.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    if not russell.afeitado:
        print("│ [PISTA SOCRÁTICA 4] El barbero evitó el bucle infinito, ¡pero sigue con")
        print("│ barba! Cuando `cliente is self`, cambia su estado `self.afeitado = True`")
        print("│ asumiendo su rol de individuo (Nivel 0) fuera de la regla municipal.")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
        sys.exit(1)

    print("│ ✅ [VEREDICTO: SUPERADO]")
    print("│ Has detenido la hemorragia en Richmond Park (1901).")
    print("│ • Separaste el Tipo (`class`) de la Instancia (`objeto`).")
    print("│ • Controlaste la autorreferencia (`cliente is self`) evitando el")
    print("│   RecursionError que desveló a Russell y Frege.")
    print("└─────────────────────────────────────────────────────────────────────────────┘")
    sys.exit(0)

if __name__ == "__main__":
    main()
