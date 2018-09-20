# -*- coding: utf-8 -*-
"""Test unitarios para la clase monstruo."""

import unittest
from monstruo import Monstruo
from ataque import Ataque
from ataque_especial import Ataque_especial

class TestMonstruo(unittest.TestCase):

    def setUp(self):
    	monster = Monstruo(Elemento.FUEGO,Elemento.AGUA)
	pass

    def verificando_monstruo_creado(self):
		self.assertEqual(100.0, monster.__estado_vital__)
		self.assertEqual(4, monster.__ataques_especiales_restantes__)
		self.assertEqual(Elemento.AGUA, monster.__elementos__[0])
		self.assertEqual(Elemento.FUEGO, monster.__elementos__[1])

	#Aun no entiendo que hace esta funcion. Leandro Amodey
	def verificando_opciones_iniciales(self):
		opciones_monster = monster.generar_opciones()

	def verificando_generar_ataque_basico(self):
		ataque_basico = monster.generar_ataque(Elemento.FUEGO)
		assertIsInstance(ataque_basico, Ataque)

	def verificando_generar_ataque_especial(self):
		ataque_especial = monster.generar_ataque_especial(Elemento.FUEGO)
		assertIsInstance(ataque_especial, Ataque_especial)

	def verificando_recibir_ataque_disminuye_vida(self):
		ataque_impactado = Ataque(Elemento.AGUA)
		monster.recibir_ataque(ataque_impactado)
		assertLess(100, monster.__estado_vital__)