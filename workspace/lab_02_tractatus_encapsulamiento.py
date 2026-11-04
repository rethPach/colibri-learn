"""
===============================================================================
CAPÍTULO 2: EL SILENCIO EN LAS TRINCHERAS (Río Piave, 14 de agosto de 1918)
Laboratorio 02: El Tractatus de Wittgenstein, Estado (Hechos) y Encapsulamiento
===============================================================================

ESCENA:
Bajo el bombardeo en el frente italiano, Ludwig Wittgenstein anota en su
libreta de hule negro:
- Proposición 1.1: "El mundo es la totalidad de los hechos, no de las cosas."
- Proposición 7: "De lo que no se puede hablar, hay que callar."

TU MISIÓN:
1. Oculta la lista interna de proposiciones tras el silencio del encapsulamiento
   cambiando `self.proposiciones` por `self.__proposiciones`.
2. En `registrar_hecho(self, proposicion: str)`, valida que `proposicion` no sea
   una cadena vacía (`if not proposicion or not proposicion.strip(): raise ValueError(...)`).
3. Expón una propiedad de solo lectura `@property def hechos(self) -> tuple:`
   que devuelva `tuple(self.__proposiciones)` para que nadie fuera del objeto
   pueda mutar la libreta directamente.
"""


class CuadernoTractatus:
    def __init__(self, autor: str):
        self.autor = autor
        # TODO Misión 1: Encapsula este atributo como privado (`self.__proposiciones = []`)
        self.proposiciones = []

    def registrar_hecho(self, proposicion: str) -> None:
        # TODO Misión 2: Si `proposicion` está vacía, lanza ValueError
        self.proposiciones.append(proposicion)

    # TODO Misión 3: Crea @property def hechos(self) -> tuple que retorne tuple(self.__proposiciones)
