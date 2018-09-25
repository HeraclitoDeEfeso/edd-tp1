from batalla import Batalla
from elemento import Elemento
import os

CANTIDAD_DE_JUGADORES = 2
CANTIDAD_DE_ELEMENTOS_POR_JUGADORES = 2

class Menu(object):
    def __init__(self, titulo, opciones):
        pass

def main():
    #titulo = None
    #opciones = None
    #m_inicial = Menu(titulo, opciones)
    #m_turno = Menu(titulo, opciones)

    while True:
        #Limpio Pantalla
        os.system('cls')
        print("Bienvenido a la batalla de monstruos. Seleccione una opcion:")
        print ("\t1 - Crear Partida")
        print ("\t2 - Cargar Partida Iniciada")
        print ("\t3 - Salir")

        opcionMenu = input("Inserta el numero de opcion >> ")

        if opcionMenu=="1":

            os.system('cls')
            print ("Creando jugador numero 1")
            nombrej1 = input("Ingresa el nombre del jugador 1 y luego presiona Enter.")
            elementoj1_1 = Elemento.NADA
            elementoj1_2 = Elemento.NADA
            print("Seleccionando el primer tipo de elemento de tu monstruo:\n")
            print("\t1 - AGUA")
            print("\t2 - FUEGO")
            print("\t3 - TIERRA")
            print("\t4 - AIRE")
            print("\t5 - Sin elemento")

            while True:
                opcionElemento = input("Inserta el numero de opcion:")
                if opcionElemento=="1":
                    elemento1 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elemento1 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elemento1 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elemento1 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            os.system("cls")
            print("Seleccionando el segundo tipo de elemento de tu monstruo:\n")
            print("\t1 - AGUA")
            print("\t2 - FUEGO")
            print("\t3 - TIERRA")
            print("\t4 - AIRE")
            print("\t5 - Sin elemento")

            while True:
                opcionElemento = input("Inserta el numero de opcion:")
                if opcionElemento=="1":
                    elemento2 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elemento2 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elemento2 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elemento2 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            os.system('cls')
            print ("Creando jugador numero 2")
            nombrej2 = input("Ingresa el nombre del jugador 1 y luego presiona Enter.")
            elementoj2_1 = Elemento.NADA
            elementoj2_2 = Elemento.NADA
            print("Seleccionando el primer tipo de elemento de tu monstruo:\n")
            print("\t1 - AGUA")
            print("\t2 - FUEGO")
            print("\t3 - TIERRA")
            print("\t4 - AIRE")
            print("\t5 - Sin elemento")

            while True:
                opcionElemento = input("Inserta el numero de opcion:")
                if opcionElemento=="1":
                    elemento1 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elemento1 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elemento1 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elemento1 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            os.system("cls")
            print("Seleccionando el segundo tipo de elemento de tu monstruo:\n")
            print("\t1 - AGUA")
            print("\t2 - FUEGO")
            print("\t3 - TIERRA")
            print("\t4 - AIRE")
            print("\t5 - Sin elemento")

            while True:
                opcionElemento = input("Inserta el numero de opcion:")
                if opcionElemento=="1":
                    elemento2 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elemento2 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elemento2 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elemento2 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")


        elif opcionMenu=="2":

            print ("")

            input("Has pulsado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu=="3":
            input("Saliendo de la batalla. \n Hasta luego!")
            break

        else:
            input("De verdad no podes ingresar un simple numero...?\nPulsa una tecla cualquiera para reintentar")




def __crear_batalla__():
    pass

def __guardar_partida__(batalla):
    pass

def __jugar_partida__(batalla):
    pass

def __mostrar_resultado_final__(batalla):
    pass

def __mostrar_resultado_parcial__(batalla):
    pass

def __menu_de_elementos__(elementos=[]):
    pass

def __menu_de_ataques__(jugador):
    pass

def __quedan_ataques_especiales__():
    pass

if __name__ == '__main__':
    main()