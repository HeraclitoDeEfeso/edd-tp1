# -*- coding: utf-8 -*-
"""
Módulo que testea la persistencia para nuestras clases
"""
import unittest
import pickle
import test_batalla
from batalla import Batalla
from elemento import Elemento

class TestPersistenciaIniciada(test_batalla.TestBatalla):

    @classmethod
    def setUpClass(cls):
        with open("batalla-store", "wb") as archivo:
            pickle.dump(Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA), archivo)

    def setUp(self):
        with open("batalla-store", "rb") as archivo:
            self.batalla = pickle.load(archivo)

class TestPersistenciaTerminada(test_batalla.TestBatallaTerminada):

    @classmethod
    def setUpClass(cls):
        batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        while not batalla.termino():
            mi_monstruo = batalla.__jugador_atacante__.__monstruo__
            batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        with open("batalla-store", "wb") as archivo:
            pickle.dump(batalla, archivo)    

    def setUp(self):
        with open("batalla-store", "rb") as archivo:
            self.batalla = pickle.load(archivo)

if __name__=="__main__":

    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)