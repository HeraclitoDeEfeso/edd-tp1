from enum import Enum

class Elemento(Enum):
    # El orden parcial del ataque es Agua > Fuego, 
    # Fuego > Tierra, Tierra > Aire y Aire > Agua
    # El orden parcial de la defensa es Agua > Fuego, 
    # Fuego > Aire, Aire > Tierra y Tierra > Agua
    AGUA = ("FUEGO", "FUEGO")
    TIERRA = ("AIRE", "AGUA")
    AIRE = ("AGUA", "TIERRA")
    FUEGO = ("TIERRA", "AIRE")
    NADA = ()

    def supera_en_ataque(self, other):
        return self != Elemento.NADA and other == Elemento[self.value[0]]

    def supera_en_defensa(self, other):
        return self != Elemento.NADA and other == Elemento[self.value[1]]

    def __repr__(self):
        return "Elemento nulo" if self == Elemento.NADA else \
                "Elemento %s: supera en ataque a %s, supera en defensa a %s"\
                % (self.name, self.value[0], self.value[1])