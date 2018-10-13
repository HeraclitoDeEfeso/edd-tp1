from elemento import Elemento

class Ataque(object):
    def __init__(self, elemento):
        self.__elemento__ = elemento
        self.__danio__ = 10 
        
    def calcular_danio(self, elementos_enemigo):
        if self.__elemento__ == Elemento.NADA:
            self.__danio__ = 0
        return self.__danio__ \
            + self.__calcular_ventaja__(elementos_enemigo,
                                        self.__ventaja_en_ataque__) \
            - self.__calcular_ventaja__(elementos_enemigo,
                                        self.__desventaja_en_defensa__)

    def __calcular_ventaja__(self, elementos_enemigo, metodo):
        return self.__danio__ * 0.20 if metodo(elementos_enemigo) else 0
    
    def __ventaja_en_ataque__(self, elementos_enemigo):
        return any(self.__elemento__.supera_en_ataque(un_elemento)
                   for un_elemento in elementos_enemigo)

    def __desventaja_en_defensa__(self, elementos_enemigo):
        return any(un_elemento.supera_en_defensa(self.__elemento__)
                   for un_elemento in elementos_enemigo)

class Ataque_especial(Ataque):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.__danio__ = 15 
