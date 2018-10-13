# -*- coding: utf-8 -*-
"""Test unitarios para la clase jugador."""

import unittest
from batalla.jugador import Jugador
from batalla.monstruo import Monstruo
from batalla.elemento import Elemento

class TestJugador(unittest.TestCase):

    def setUp(self):
    	#Se crea un jugador generico para realizar las pruebas
    	self.player = Jugador("Unnamed",Elemento.AGUA,Elemento.FUEGO)

    def test_verificando_nombre_unnamed_correctamente(self):
        self.assertEqual("Unnamed", self.player.__nombre__)

    def test_verificando_monstruo_creado_por_unnamed(self):
        self.assertIsInstance(self.player.__monstruo__, Monstruo)

    def test_error_al_crear_elementos_iguales(self):
        self.assertRaises(Exception, Jugador, "Bad", Elemento.AIRE, Elemento.AIRE)
        
    def test_error_al_crear_sin_elementos(self):
        self.assertRaises(Exception, Jugador, "Human1", Elemento.TIERRA)
        self.assertRaises(Exception, Jugador, "Human2")
        
    def test_error_al_crear_sin_nombre(self):
        self.assertRaises(Exception, Jugador, "", Elemento.AIRE, Elemento.TIERRA)

if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)