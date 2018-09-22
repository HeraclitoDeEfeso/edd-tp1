from jugador import Jugador
from elemento import Elemento
from ataque import Ataque

class Batalla(object):

    def __init__(self, nombrePrimerJugador, primerElementoPrimerJugador, segundoElementoPrimerJugador, nombreSegundoJugador, primerElementoSegundoJugador, segundoElementoSegundoJugador):
        try:
            self.elementos = [Elemento.FUEGO, Elemento.TIERRA, Elemento.AIRE, Elemento.AGUA]
            self.__jugador_atacante__ = Jugador(nombrePrimerJugador, primerElementoPrimerJugador, segundoElementoPrimerJugador)
            self.__jugador_defensor__ = Jugador(nombreSegundoJugador, primerElementoSegundoJugador, segundoElementoSegundoJugador)
            if (nombrePrimerJugador == nombreSegundoJugador):
                raise ValueError("Nombres de monstruo idénticos")
                raise Exception("Nombres idénticos")
        except Exception as error:
            print("Error detectado : " + repr(error))

    def __str__(self):
        return str(self.__dict__)

    def obtenerJugadorAtacante(self):
        self.__jugador_atacante__.__str__()

    def obtenerJugadorDefensor(self):
        self.__jugador_defensor__.__str__()

    def termino(self):
        return (self.__jugador_atacante__.__monstruo__.__estado_vital__ <= 0 
                or self.__jugador_defensor__.__monstruo__.__estado_vital__ <= 0)

    def ganador(self):
        ganador = None
        if (self.termino()):
            ganador = self.__jugador_defensor__
        return ganador

    def jugada(self, ataque):
        try:
            if (ataque.__elemento__ == None):
                raise ValueError("Todos los ataques deben tener un elemento")
                raise Exception("Ataque no elemental")
            elif (not self.termino()):
                self.__jugador_defensor__.__monstruo__.recibir_ataque(ataque)
                auxiliar = self.__jugador_atacante__
                self.__jugador_atacante__ = self.__jugador_defensor__
                self.__jugador_defensor__ = auxiliar
        except Exception as error:
            print("Error detectado : " + repr(error))

