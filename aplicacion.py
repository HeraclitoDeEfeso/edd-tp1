from menu import Menu
from batalla import Batalla
from elemento import Elemento
import os

CANTIDAD_DE_JUGADORES = 2
CANTIDAD_DE_ELEMENTOS_POR_JUGADORES = 2

def main():
    while True:
        #Limpio Pantalla
        os.system('cls')
        menu_inicial = Menu("Bienvenido a la batalla de monstruos. Seleccione una opcion:",{"1":"Crear Partida","2":"Cargar Partida Iniciada","3":"Salir"})
        opcionMenu = menu_inicial.mostrar_y_pedir_input()

        if opcionMenu=="1":
   	        menu_creacion_elementos1 = Menu("Selecciona el primer elemento para tu monstruo:",{"1":"AGUA","2":"FUEGO","3":"TIERRA","4":"AIRE","5":"Sin elemento"})
        	menu_creacion_elementos2 = Menu("Selecciona el segundo elemento para tu monstruo:",{"1":"AGUA","2":"FUEGO","3":"TIERRA","4":"AIRE","5":"Sin elemento"})
            os.system('cls')
            print ("Creando jugador numero 1")
            nombrej1 = input("Ingresa el nombre del jugador 1 y luego presiona Enter.")
            elementoj1_1 = Elemento.NADA
            elementoj1_2 = Elemento.NADA

            while True:
                opcionElemento = menu_creacion_elementos1.mostrar_y_pedir_input()
                if opcionElemento=="1":
                    elementoj1_1 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elementoj1_1 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elementoj1_1 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elementoj1_1 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            os.system("cls")

            while True:
                opcionElemento = menu_creacion_elementos2.mostrar_y_pedir_input()
                if opcionElemento=="1":
                    elementoj1_2 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elementoj1_2 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elementoj1_2 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elementoj1_2 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            os.system('cls')
            print ("Creando jugador numero 2")
            nombrej2 = input("Ingresa el nombre del jugador 2 y luego presiona Enter.")
            elementoj2_1 = Elemento.NADA
            elementoj2_2 = Elemento.NADA

            while True:
                opcionElemento = menu_creacion_elementos1.mostrar_y_pedir_input()
                if opcionElemento=="1":
                    elemento2_1 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elemento2_1 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elemento2_1 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elemento2_1 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            os.system("cls")
            while True:
                opcionElemento = menu_creacion_elementos2.mostrar_y_pedir_input()
                if opcionElemento=="1":
                    elemento2_2 = Elemento.AGUA
                    break
                elif opcionElemento=="2":
                    elemento2_2 = Elemento.FUEGO
                    break
                elif opcionElemento=="3":
                    elemento2_2 = Elemento.TIERRA
                    break
                elif opcionElemento=="4":
                    elemento2_2 = Elemento.AIRE
                    break
                elif opcionElemento=="5":
                    break
                else:
                    print("No se ingreso ninguna opcion valida. Reintentando.")

            try:
            	batallaEnJuego = Batalla(nombrej1,elementoj1_1,elementoj1_2,nombrej2,elementoj2_1,elementoj2_2)

            except Exception:

            __jugar_turno__(batallaEnJuego)




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