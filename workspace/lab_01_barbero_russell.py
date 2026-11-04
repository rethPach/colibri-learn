"""
===============================================================================
CAPÍTULO 1: EL FILO DE LA NAVAJA (Richmond Park, 18 de mayo de 1901)
Laboratorio 01: La Paradoja de Russell, Teoría de Tipos y el puntero `self`
===============================================================================

ESCENA:
Bertrand Russell sostiene la navaja de acero Sheffield frente al espejo.
En el pueblo hay una regla municipal aparentemente perfecta:
"El barbero afeita única y exclusivamente a los aldeanos que NO se afeitan a sí mismos."

EL PROBLEMA EN CÓDIGO:
Si modelamos al Barbero sin distinguir entre su regla sobre el conjunto de clientes
y su propia identidad individual (`self`), cuando el barbero se pregunta si debe
afeitarse a sí mismo (`russell.afeitar(russell)`), entra en un bucle infinito
de autorreferencia (`RecursionError`) y se corta el cuello.

TU MISIÓN:
1. Haz que `Barbero` herede de `Aldeano` (Jerarquía de Tipos: todo Barbero es un Aldeano).
2. En `Barbero.afeitar(self, cliente)`, resuelve la paradoja de autorreferencia:
   - Si `cliente is self` (el barbero frente a su propio espejo), rompe el bucle
      recursivo y márcalo como afeitado directamente (`self.afeitado = True`).
   - Si `cliente` es cualquier otro `Aldeano`, aplícale la regla municipal:
     solo aféitalo (`cliente.afeitado = True`) si `not cliente.se_afeita_solo`.
"""


class Aldeano:
    """Tipo Nivel 1: Molde para cualquier habitante del pueblo."""

    def __init__(self, nombre: str, se_afeita_solo: bool = False):
        self.nombre = nombre
        self.se_afeita_solo = se_afeita_solo
        self.afeitado = False


# Misión 1: Barbero hereda de Aldeano (Jerarquía de Tipos)
class Barbero(Aldeano):
    """
    El único barbero del municipio.
    Hereda de Aldeano y controla su autorreferencia mediante `self`.
    """

    def __init__(self, nombre: str):
        super().__init__(nombre, se_afeita_solo=False)

    def afeitar(self, cliente) -> bool:
        """
        Regla municipal con Teoría de Tipos y control de identidad (`self`).
        """
        # Misión 2: Condición base de identidad frente al espejo (`cliente is self`)
        if cliente is self:
            self.afeitado = True
            return True

        if not cliente.se_afeita_solo:
            cliente.afeitado = True
            return True
        return False


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("🪒 Ejecutando simulación en Richmond Park (1901)...")
    herrero = Aldeano("Herrero", se_afeita_solo=False)
    panadero = Aldeano("Panadero", se_afeita_solo=True)
    russell = Barbero("Bertrand")

    russell.afeitar(herrero)
    print(f"• ¿Herrero afeitado por el barbero?: {herrero.afeitado}")

    russell.afeitar(panadero)
    print(f"• ¿Panadero afeitado por el barbero?: {panadero.afeitado}")

    print("• Bertrand Russell se mira al espejo y levanta la navaja (`russell.afeitar(russell)`)...")
    russell.afeitar(russell)
    print(f"• ¿Bertrand Russell afeitado sin paradoja?: {russell.afeitado}")
