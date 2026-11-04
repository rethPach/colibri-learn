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
        return [1 - x for x in cinta]


class CabezaSumadora:
    def operar(self, cinta: list[int]):
        return sum(cinta)


class CabezaEco:
    def operar(self, cinta: list[int]):
        return cinta + cinta


def enviar_mensaje(maquina, cinta: list[int]):
    return maquina.operar(cinta)


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🏃‍♂️ Ejecutando simulación en Grantchester Meadows (1936)...")
    cinta = [1, 0, 1]
    for m in (CabezaInversora(), CabezaSumadora(), CabezaEco()):
        print(f"• {m.__class__.__name__} -> {enviar_mensaje(m, cinta)}")
