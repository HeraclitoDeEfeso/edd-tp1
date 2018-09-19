from elemento import Elemento

class Mounstruo():
    def __init__(self, elem_1, elem_2):
        self.__elementos__[0]= elem_1
        self.__elementos__[1]= elem_2
        self.__estado_vital__ = 100
        self.__ataques_especiales_restantes__ = 4
        assert self.elemento[0] != self.elemento[1],'los elementos deben ser diferentes'
        assert self.elemento[0] == None & self.elemento[1] == None, 'los dos elementos no pueden ser nulos'
        
