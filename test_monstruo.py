# -*- coding: utf-8 -*-
"""Test unitarios para la clase monstruo."""

import unittest
from monstruo import Monstruo
from ataque import Ataque, Ataque_especial
from elemento import Elemento

class TestMonstruo(unittest.TestCase):

    def setUp(self):
        self.monster = Monstruo(Elemento.FUEGO,Elemento.AGUA)

    def test_verificando_monstruo_creado(self):
        self.assertEqual(100.0, self.monster.__estado_vital__)
        self.assertEqual(4, self.monster.__ataques_especiales_restantes__)
        self.assertEqual(Elemento.AGUA, self.monster.__elementos__[1])
        self.assertEqual(Elemento.FUEGO, self.monster.__elementos__[0])

    def test_verificando_opciones_iniciales(self):
        opciones_monster = self.monster.generar_opciones()
        self.assertEqual(opciones_monster[0], Elemento.FUEGO)
        self.assertEqual(opciones_monster[1], Elemento.AGUA)

    def test_verificando_generar_ataque_basico(self):
        ataque_basico = self.monster.generar_ataque(Elemento.FUEGO)
        self.assertIsInstance(ataque_basico, Ataque)

    def test_verificando_generar_ataque_especial(self):
        ataque_especial = self.monster.generar_ataque_especial(Elemento.FUEGO)
        self.assertIsInstance(ataque_especial, Ataque_especial)

    def test_verificando_generar_ataques_elemento_que_no_es_del_monstruo(self):
        self.assertRaises(AssertionError, self.monster.generar_ataque, Elemento.TIERRA)
        self.assertRaises(AssertionError, self.monster.generar_ataque_especial, Elemento.TIERRA)

    def test_verificando_recibir_ataque_basico_disminuye_vida(self):
        ataque_impactado = Ataque(Elemento.AGUA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertLess(self.monster.__estado_vital__, 100)

    def test_verificando_recibir_ataque_basico_aumentado(self):
        #El monstruo es tipo fuego y agua, por ende al recibir agua deberia recibir ataque de 10+20% = 12
        ataque_impactado = Ataque(Elemento.AGUA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertEqual(self.monster.__estado_vital__, 100-12)

    def test_verificando_recibir_ataque_basico_disminuido(self):
        #El monstruo es tipo fuego y agua, por ende al recibir agua deberia recibir ataque de 10-20% = 8
        ataque_impactado = Ataque(Elemento.TIERRA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertEqual(self.monster.__estado_vital__, 100-8)

    def test_verificando_recibir_ataque_especial_aumentado(self):
        #El monstruo es tipo fuego y agua, por ende al recibir agua deberia recibir ataque de 15+20% = 18
        ataque_impactado = Ataque_especial(Elemento.AGUA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertEqual(self.monster.__estado_vital__, 100-18)

    def test_verificando_recibir_ataque_especial_disminuido(self):
        #El monstruo es tipo fuego y agua, por ende deberia recibir ataque de 15-20% = 12
        ataque_impactado = Ataque_especial(Elemento.TIERRA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertEqual(self.monster.__estado_vital__, 100-12)        


    def test_verificando_recibir_ataque_no_elemental(self):
        #Chequeo que en caso de que pase un ataque con elemento NADA o NULO el ataque es 0
        #En nuestra implementacion esto nunca ocurre, ya que el jugador puede atacar solo con dos elementos o con uno.
        #Pero se verifica para que en caso de algun error al pasar el ataque no afecte el desarrollo del juego
        ataque_impactado = Ataque_especial(Elemento.NADA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertEqual(self.monster.__estado_vital__, 100)
    """
    Este test no tendria sentido ya que los elementos se crean internamente a partir de las opciones del menu.
    def test_error_al_crear_sin_elementos(self):
        self.assertRaises(AssertionError, Monstruo)
        self.assertRaises(AssertionError, Monstruo, Elemento.AGUA)
        """
if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
