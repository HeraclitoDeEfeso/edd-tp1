from jugador import Jugador
from elemento import Elemento
from ataque import Ataque
from monstruo import Monstruo

class Batalla():

    def __init__(self, nombrePrimerJugador, primerElementoPrimerJugador, segundoElementoPrimerJugador, nombreSegundoJugador, primerElementoSegundoJugador, segundoElementoSegundoJugador):
        try:
            self.elementos = [Elemento.FUEGO, Elemento.TIERRA, Elemento.AIRE, Elemento.AGUA]
            self.atacante = Jugador(nombrePrimerJugador, Monstruo(primerElementoPrimerJugador, segundoElementoPrimerJugador))
            self.defensor = Jugador(nombreSegundoJugador, Monstruo(primerElementoSegundoJugador, segundoElementoSegundoJugador))
            if (nombrePrimerJugador == nombreSegundoJugador):
                raise ValueError("Nombres de monstruo idénticos")
                raise Exception("Nombres idénticos")
        except Exception as error:
            print("Error detectado : " + repr(error))

    def __str__(self):
        return str(self.__dict__)

    def obtenerJugadorAtacante(self):
        self.atacante.__str__()

    def obtenerJugadorDefensor(self):
        self.defensor.__str__()

    def termino(self):
        return (self.atacante.__estado_vital__ <= 0 
                or self.defensor.__estado_vital__ <= 0)

    def obternerGanador(self):
        ganador = None
        if (self.termino()):
            ganador = self.defensor
        return ganador

    def jugada(self, ataque):
        try:
            if (ataque.__elemento__ == None):
                raise ValueError("Todos los ataques deben tener un elemento")
                raise Exception("Ataque no elemental")
            elif (not self.termino()):
                self.defensor.recibirAtaque(ataque)
                auxiliar = self.atacante
                self.atacante = self.defensor
                self.defensor = auxiliar
        except Exception as error:
            print("Error detectado : " + repr(error))

