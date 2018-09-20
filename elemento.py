import enum

class Elemento(enum.Enum):
    # El orden parcial del ataque es Agua > Fuego, 
    # Fuego > Tierra, Tierra > Aire y Aire > Agua
    # El orden parcial de la defensa es Agua > Fuego, 
    # Fuego > Aire, Aire > Tierra y Tierra > Agua
    AGUA = ("FUEGO", "FUEGO")
    TIERRA = ("AIRE", "AGUA")
    AIRE = ("AGUA", "FUEGO")
    FUEGO = ("TIERRA", "AIRE")

    def supera_en_ataque(self, other):
        return other == Elemento[self.value[0]]

    def supera_en_defensa(self, other):
        return other == Elemento[self.value[1]]

    def __repr__(self):
        return "Elemento %s: supera en ataque al %s, supera en defensa al %s"\
                % (self.name, self.value[0], self.value[1])