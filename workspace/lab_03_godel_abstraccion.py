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


# Misión 1: Contrato abstracto gödeliano con ABC y @abstractmethod
class SistemaFormal(ABC):
    @abstractmethod
    def demostrar(self, enunciado: str) -> str:
        """Contrato abstracto: ningún sistema cerrado se instancia sin implementación."""
        pass


class SistemaAritmetico(SistemaFormal):
    def demostrar(self, enunciado: str) -> str:
        # Misión 2: Reconoce su incompletitud ante el enunciado autorreferencial G
        if "no es demostrable" in enunciado:
            return "INCOMPLETO"
        return "DEMOSTRADO"


class MetaSistemaGodel(SistemaFormal):
    def demostrar(self, enunciado: str) -> str:
        # Misión 3: Observa desde el metanivel y valida la verdad de G
        if "no es demostrable" in enunciado:
            return "VERDADERO_DESDE_METANIVEL"
        return "DEMOSTRADO"


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🏛️ Ejecutando simulación en Königsberg (1930)...")
    enunciado_g = "G: Esta proposicion no es demostrable en SistemaAritmetico"
    aritmetica = SistemaAritmetico()
    metasistema = MetaSistemaGodel()
    print(f"• SistemaAritmetico ante G: {aritmetica.demostrar(enunciado_g)}")
    print(f"• MetaSistemaGodel ante G:  {metasistema.demostrar(enunciado_g)}")
