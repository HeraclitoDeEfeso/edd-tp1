# -*- coding: utf-8 -*-
"""Test unitarios para la clase jugador."""

import unittest
from jugador import Jugador
from monstruo import Monstruo

class TestJugador(unittest.TestCase):

    def setUp(self):
    	#Se crea un jugador generico para realizar las pruebas
    	player = Jugador("Unnamed",Elemento.AGUA,Elemento.FUEGO)
        pass

    def verificando_nombre_unnamed_correctamente(self):
		self.assertEqual("Unnamed", jugador.__nombre__)
		

	def verificando_monstruo_creado_por_unnamed(self):
		self.assertIsInstance(player.__monstruo__, Monstruo)

	def error_al_crear_elementos_iguales(self):
		player_bad = Jugador("Bad",Elemento.AIRE,Elemento.AIRE)
		assertRaises(Exception)

	def error_al_crear_sin_elementos(self):
		player_noelemental1 = Jugador("Human1",Elemento.TIERRA)
		assertRaises(Exception)
		player_noelemental2 = Jugador("Human2")
		assertRaises(Exception)

	def error_al_crear_sin_nombre(self):
		player_noname = Jugador("",Elemento.AIRE,Elemento.TIERRA)
		assertRaises(Exception)



    if __name__=="__main__":

    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)