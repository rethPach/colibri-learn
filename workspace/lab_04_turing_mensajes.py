"""
===============================================================================
CAPÍTULO 4: EL CORREDOR Y LA CINTA INFINITA (Grantchester Meadows, 8 de mayo de 1936)
Laboratorio 04: La Máquina Universal de Turing, Objetos y Paso de Mensajes
===============================================================================

ESCENA:
Alan Turing descubre que las instrucciones son datos en la misma cinta.
Décadas después, Alan Kay lleva esta idea al límite: cada Objeto es una
pequeña Máquina Universal que fusiona estado + comportamiento y responde a mensajes.

TU MISIÓN:
1. Implementa el método `operar(self, cinta: list[int])` en cada máquina:
   - `CabezaInversora`: devuelve una nueva lista invirtiendo 0s y 1s (`[1 - x for x in cinta]`).
   - `CabezaSumadora`: devuelve la suma de los elementos (`sum(cinta)`).
   - `CabezaEco`: devuelve la cinta duplicada (`cinta + cinta`).
2. En `enviar_mensaje(maquina, cinta)`, elimina los condicionales rígidos (`if/isinstance`)
   y reemplázalos por un único envío de mensaje polimórfico: `return maquina.operar(cinta)`.
"""


class CabezaInversora:
    def operar(self, cinta: list[int]):
        # TODO Misión 1a
        pass


class CabezaSumadora:
    def operar(self, cinta: list[int]):
        # TODO Misión 1b
        pass


class CabezaEco:
    def operar(self, cinta: list[int]):
        # TODO Misión 1c
        pass


def enviar_mensaje(maquina, cinta: list[int]):
    # TODO Misión 2: Reemplaza este bloque procedural por polimorfismo puro (una sola línea)
    if isinstance(maquina, CabezaInversora):
        return None
    elif isinstance(maquina, CabezaSumadora):
        return None
    else:
        return None
