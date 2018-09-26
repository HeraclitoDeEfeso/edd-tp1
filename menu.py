
class Menu(object):

	opciones = {}
	titulo = "Titulo por defecto"

	def __init__(self, tituloIngresado, opcionesDadas = {}):
		self.titulo = tituloIngresado
		self.opciones = opcionesDadas


	def mostrar_y_pedir_input(self):
		print(self.titulo+"\n")
		for opc in self.opciones:
			print(opc+" - "+self.opciones[opc])

		return input("\nIngresar el numero de opcion deseado:")