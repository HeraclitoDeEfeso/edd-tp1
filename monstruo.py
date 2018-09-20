from elemento import Elemento
"""faltan los imports de ataque"""

class Mounstruo():
    """ se deberia controlar los tipos de los parametros ?"""
    def __init__(self, elem_1, elem_2): 
        self.__elementos__[0]= elem_1
        self.__elementos__[1]= elem_2
        self.__estado_vital__ = 100
        self.__ataques_especiales_restantes__ = 4
        assert self.elemento[0] != self.elemento[1],'los elementos deben ser diferentes'
        assert self.elemento[0] != None & self.elemento[1] != None, 'los dos elementos no pueden ser nulos'
        
    def generar_ataque(elemento): 
        assert self.elemento[0] == elemento | self.elemento[0] == elemento, 'este monstruo no posee el elemento indicado'
        ataque = Ataque(elemento)
        return ataque

    def generar_ataque_especial(elemento):
        assert self.__ataques_especiales_restantes__ >= 0, 'no te quedan mas ataques especiales'
        assert self.elemento[0] == elemento | self.elemento[0] == elemento, 'este monstruo no posee el elemento indicado'
        ataque = Ataque_especial(elemento)
        self.__ataques_especiales_restantes__  -= 1
        return ataque

    def general_opciones():
        return self.__elementos__

    def recibir_ataque(ataque):
        if ataque.calcular_danio(self.general_opciones()) <= self.__estado_vital__ :
            self.__estado_vital__ -= ataque.calcular_danio(self.general_opciones())
        else: self.__estado_vital__ = 0
        
