import enum

class Elemento(enum.Enum):
    AGUA = 1
    TIERRA = 2
    AIRE = 3
    FUEGO = 4

    @staticmethod
    def diccionario_orden():
        # El orden parcial del ataque es Agua > Fuego, 
        # Fuego > Tierra, Tierra > Aire y Aire > Agua
        # el orden parcial de la defensa es Agua > Fuego, 
        # Fuego > Aire, Aire > Tierra y Tierra > Agua
        return {"supera_en_ataque": {Elemento.AGUA: Elemento.FUEGO,
                                     Elemento.FUEGO: Elemento.TIERRA,
                                     Elemento.TIERRA: Elemento.AIRE,
                                     Elemento.AIRE: Elemento.AGUA},
            "supera_en_defensa": {Elemento.AGUA: Elemento.FUEGO,
                                  Elemento.FUEGO: Elemento.TIERRA,
                                  Elemento.TIERRA: Elemento.AIRE,
                                  Elemento.AIRE: Elemento.AGUA}}

    def supera_en_ataque(self, other):
        return other == Elemento.diccionario_orden()["supera_en_ataque"][self]

    def supera_en_defensa(self, other):
        return other == Elemento.diccionario_orden()["supera_en_defensa"][self]
