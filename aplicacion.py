from menu import Menu
from batalla import Batalla
from elemento import Elemento
import os

CANTIDAD_DE_JUGADORES = 2
CANTIDAD_DE_ELEMENTOS_POR_JUGADORES = 2
NOMBRE_ARCHIVO_BATALLA = "batalla-store"

def main():
    #Limpio Pantalla
    os.system('cls')
    while True:
        menu_inicial = Menu("Bienvenido a la batalla de monstruos. Seleccione una opcion:",{"1":"Crear Partida","2":"Cargar Partida Iniciada","3":"Salir"})
        opcionMenu = menu_inicial.mostrar_y_pedir_input()
        if opcionMenu=="1":
            while True:
                try:
                    batallaEnJuego = Batalla(*[
                            arg for i in range(CANTIDAD_DE_JUGADORES)
                                for arg in __cargar_jugador__(i + 1)])
                    break
                except Exception as e:
                    print("Surgio un problema: %s" % e)
            break
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
            input("Saliendo de la batalla. \n Hasta luego!")
            return
        else:
            input("De verdad no podes ingresar un simple numero...?\nPulsa una tecla cualquiera para reintentar")
    __jugar_turno__(batallaEnJuego)
        
def __cargar_jugador__(indice):
    print ("Creando jugador numero %d" % indice)
    return  (input("Ingresa el nombre del jugador 1 y luego presiona [Enter]: "),
            *(__elegir_elemento__(
                    Menu("Selecciona el %d° elemento para tu monstruo:" % (i + 1),
                         {"1" : "AGUA",
                          "2" : "FUEGO",
                          "3" : "TIERRA",
                          "4" : "AIRE",
                          "5" : "Sin elemento"}))
                    for i in range(CANTIDAD_DE_ELEMENTOS_POR_JUGADORES)))

def __elegir_elemento__(menu):
    while True:
        opcionElemento = menu.mostrar_y_pedir_input()
        if opcionElemento=="1":
            return Elemento.AGUA
        elif opcionElemento=="2":
            return Elemento.FUEGO
        elif opcionElemento=="3":
            return Elemento.TIERRA
        elif opcionElemento=="4":
            return Elemento.AIRE
        elif opcionElemento=="5":
            return Elemento.NADA
        else:
            print("No se ingreso ninguna opcion valida. Reintentando.")

def __jugar_turno__(batalla):
    pass

if __name__ == '__main__':
    main()