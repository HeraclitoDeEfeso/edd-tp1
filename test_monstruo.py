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
        self.assertEqual(Elemento.AGUA, self.monster.__elementos__[0])
        self.assertEqual(Elemento.FUEGO, self.monster.__elementos__[1])

    #Aun no entiendo que hace esta funcion. Leandro Amodey
    def test_verificando_opciones_iniciales(self):
        opciones_monster = self.monster.generar_opciones()

    def test_verificando_generar_ataque_basico(self):
        ataque_basico = self.monster.generar_ataque(Elemento.FUEGO)
        self.assertIsInstance(ataque_basico, Ataque)

    def test_verificando_generar_ataque_especial(self):
        ataque_especial = self.monster.generar_ataque_especial(Elemento.FUEGO)
        self.assertIsInstance(ataque_especial, Ataque_especial)

    def test_verificando_recibir_ataque_disminuye_vida(self):
        ataque_impactado = Ataque(Elemento.AGUA)
        self.monster.recibir_ataque(ataque_impactado)
        self.assertLess(100, self.monster.__estado_vital__)