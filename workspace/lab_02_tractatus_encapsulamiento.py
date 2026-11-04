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
        # Misión 1: Encapsulamiento como atributo privado (`self.__proposiciones`)
        self.__proposiciones = []

    def registrar_hecho(self, proposicion: str) -> None:
        # Misión 2: Validación de invariantes (solo proposiciones con sentido)
        if not proposicion or not proposicion.strip():
            raise ValueError("De lo que no tiene sentido, hay que callar: la proposición no puede estar vacía.")
        self.__proposiciones.append(proposicion)

    # Misión 3: Propiedad de solo lectura que devuelve una tupla inmutable
    @property
    def hechos(self) -> tuple:
        return tuple(self.__proposiciones)


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("📓 Ejecutando simulación en el Río Piave (1918)...")
    cuaderno = CuadernoTractatus("Ludwig Wittgenstein")
    cuaderno.registrar_hecho("1.1 El mundo es la totalidad de los hechos, no de las cosas.")
    cuaderno.registrar_hecho("7. De lo que no se puede hablar, hay que callar.")
    print(f"• Hechos registrados (tupla inmutable): {cuaderno.hechos}")
    print(f"• ¿Existe atributo público `proposiciones`?: {hasattr(cuaderno, 'proposiciones')}")
