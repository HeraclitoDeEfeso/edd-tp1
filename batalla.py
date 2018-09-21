from jugador import Jugador
from elemento import Elemento
from ataque import Ataque

class Batalla():

    def __init__(self, nombrePrimerJugador, primerElementoPrimerJugador, segundoElementoPrimerJugador, nombreSegundoJugador, primerElementoSegundoJugador, segundoElementoSegundoJugador):
        try:
            elementos = [Elemento.FUEGO, Elemento.TIERRA, Elemento.AIRE, Elemento.AGUA]
            atacante = Jugador(nombrePrimerJugador, Monstruo(primerElementoPrimerJugador, segundoElementoPrimerJugador))
            defensor = Jugador(nombreSegundoJugador, Monstruo(primerElementoSegundoJugador, segundoElementoSegundoJugador))
            if (nombrePrimerJugador == nombreSegundoJugador):
                raise ValueError("Nombres de monstruo idénticos")
                raise Exception("Nombres idénticos")
            except Exception as error:
                print("Error detectado : " + repr(error))

    def __str__(self):
        return str(self.__dict__)

    def obtenerJugadorAtacante(self):
        atacante.__str__()

    def obtenerJugadorDefensor(self):
        defensor.__str__()

    def termino(self):
        return (atacante.__estado_vital__ <= 0 or defensor.__estado_vital__ <= 0)

    def obternerGanador():
        ganador = None
        if (termino()):
            ganador = defensor
        return ganador

    def jugada(ataque):
        try:
            if (ataque.__elemento__ == None):
                raise ValueError("Todos los ataques deben tener un elemento")
                raise Exception("Ataque no elemental")
            except Exception as error:
                print("Error detectado : " + repr(error))
            elif (!termino()):
                defensor.recibirAtaque(ataque)
                auxiliar = atacante
                atacante = defensor
                defensor = auxiliar

