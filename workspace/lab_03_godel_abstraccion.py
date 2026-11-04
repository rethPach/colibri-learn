"""
===============================================================================
CAPÍTULO 3: LA JAULA DE LOS AXIOMAS (Königsberg, 7 de septiembre de 1930)
Laboratorio 03: El Teorema de Incompletitud de Gödel y las Clases Abstractas
===============================================================================

ESCENA:
Kurt Gödel escribe con tiza blanca la fórmula que destruye el sueño de Hilbert:
ningún sistema formal cerrado puede demostrar todas las verdades desde adentro.

TU MISIÓN:
1. Haz que `SistemaFormal` herede de `ABC` y decora `demostrar(self, enunciado: str)`
   con `@abstractmethod`.
2. Haz que `SistemaAritmetico` herede de `SistemaFormal`. Si `enunciado` contiene
   `"no es demostrable"`, debe devolver `"INCOMPLETO"`; de lo contrario, `"DEMOSTRADO"`.
3. Haz que `MetaSistemaGodel` herede de `SistemaFormal` y devuelva
   `"VERDADERO_DESDE_METANIVEL"` cuando analice el enunciado de Gödel.
"""

from abc import ABC, abstractmethod


# TODO Misión 1: Hereda de ABC y convierte `demostrar` en @abstractmethod
class SistemaFormal:
    def demostrar(self, enunciado: str) -> str:
        return "TODO"


class SistemaAritmetico:
    def demostrar(self, enunciado: str) -> str:
        # TODO Misión 2
        return "TODO"


class MetaSistemaGodel:
    def demostrar(self, enunciado: str) -> str:
        # TODO Misión 3
        return "TODO"
