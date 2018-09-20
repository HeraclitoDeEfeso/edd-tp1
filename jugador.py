from monstruo import Monstruo

class Jugador():

    def __init__(self, name, elem_1, elem_2):
        self.__monstruo__ = Monstruo(elem_1, elem_2)
        self.__nombre__ = name
        
