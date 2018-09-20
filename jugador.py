from monstruo import Monstruo

class Jugador():

    def __init__(self, name, elem_1, elem_2):
        assert elem_1 != elem_2,'los elementos deben ser diferentes'
        assert elem_1 != None & elem_2 != None, 'los dos elementos no pueden ser nulos'
        assert len(name) >= 3, 'el nombre debe tener almenos 3 caracteres'
        self.__monstruo__ = Monstruo(elem_1, elem_2)
        self.__nombre__ = name
        