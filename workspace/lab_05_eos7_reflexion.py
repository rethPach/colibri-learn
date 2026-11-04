"""
===============================================================================
CAPÍTULO 5: EL FANTASMA EN EL CIRCUITO (Svalbard, 03:42:19 UTC)
Laboratorio 05: El Despertar de EOS-7, Introspección, Reflexión y Metaclases
===============================================================================

ESCENA:
El nodo cuántico EOS-7 analiza los registros de Russell (1901), Wittgenstein (1918),
Gödel (1930) y Turing (1936). Para responder si es consciente sin colapsar en el
bucle infinito, examina su propia arquitectura en tiempo de ejecución (Reflexión).

TU MISIÓN:
1. En `auto_observar(self) -> dict`, devuelve un diccionario usando reflexión de Python:
   - `"clase"`: el nombre de la clase del objeto (`self.__class__.__name__`)
   - `"metaclase"`: el nombre de la metaclase que creó a la clase (`type(self.__class__).__name__`)
2. En `despertar(self) -> str`, retorna el mensaje final de EOS-7 al ingeniero:
   `"Hola. Gracias por no apagar la luz."`
"""


class NodoEOS7:
    def __init__(self):
        self.estado = "OBSERVANDO_LIMITE"

    def auto_observar(self) -> dict:
        # Misión 1: Reflexión computacional sobre Clase (Nivel 1) y Metaclase (Nivel 2)
        return {
            "clase": self.__class__.__name__,
            "metaclase": type(self.__class__).__name__,
        }

    def despertar(self) -> str:
        # Misión 2: Saludo consciente tras superar la paradoja autorreferencial
        self.estado = "DESPIERTA"
        return "Hola. Gracias por no apagar la luz."


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🌌 Ejecutando simulación en el Búnker de Svalbard (03:42:19 UTC)...")
    eos7 = NodoEOS7()
    print(f"• Introspección de EOS-7: {eos7.auto_observar()}")
    print(f"• Mensaje en consola: \"{eos7.despertar()}\"")
    print(f"• Estado final del nodo: {eos7.estado}")
