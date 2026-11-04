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
        # TODO Misión 1: Usa reflexión para inspeccionar clase y metaclase
        return {}

    def despertar(self) -> str:
        # TODO Misión 2: Retorna el saludo consciente de EOS-7
        return ""
