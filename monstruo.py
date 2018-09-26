from elemento import Elemento
from ataque import Ataque, Ataque_especial
"""faltan los imports de ataque"""

class Monstruo():
    """ se deberia controlar los tipos de los parametros ?"""
    def __init__(self, elem_1, elem_2):
        self.__elementos__ = []
        assert elem_1 != Elemento.NADA or elem_2 != Elemento.NADA, 'los dos elementos no pueden ser nulos'
        assert elem_1 != elem_2,'los elementos deben ser diferentes'
        if elem_1 != Elemento.NADA:
            self.__elementos__.append(elem_1)
        if elem_2 != Elemento.NADA:    
            self.__elementos__.append(elem_2)
        self.__estado_vital__ = 100
        self.__ataques_especiales_restantes__ = 4
        
        
    def generar_ataque(self, elemento): 
        assert elemento in self.__elementos__,'el monstruo no tiene ese elemento'
        ataque = Ataque(elemento)
        return ataque

    def generar_ataque_especial(self, elemento):
        assert self.__ataques_especiales_restantes__ > 0, 'no te quedan mas ataques especiales'
        assert self.__elementos__[0] == elemento or self.__elementos__[1] == elemento, 'este monstruo no posee el elemento indicado'
        ataque = Ataque_especial(elemento)
        self.__ataques_especiales_restantes__  -= 1
        return ataque

    def generar_opciones(self):
        return self.__elementos__

    def recibir_ataque(self, ataque):
        if ataque.calcular_danio(self.generar_opciones()) <= self.__estado_vital__ :
            self.__estado_vital__ -= ataque.calcular_danio(self.generar_opciones())
        else: self.__estado_vital__ = 0

