# -*- coding: utf-8 -*-
"""Test unitarios para el módulo ataque."""

import unittest
from ataque import Ataque, Ataque_especial
from elemento import Elemento

class TestAtaque(unittest.TestCase):

    def setUp(self):
        pass

    def test_se_puede_crear_un_ataque_de_cada_elemento(self):
        a = Ataque(Elemento.FUEGO)
        b = Ataque(Elemento.AGUA)
        c = Ataque(Elemento.TIERRA)
        d = Ataque(Elemento.AIRE)

    def test_verificar_matriz_de_daño(self):
        elementos = [ Elemento.AGUA , Elemento.FUEGO , Elemento.TIERRA , Elemento.AIRE ]
        daños_esperados = [[10, 12, 8, 10],[8,10,12,10],[10,10,10,10],[12,8,10,10]]
        daños_calculados = []
        for elemento_ataque in range(0, 4):
            mi_ataque = Ataque(elementos[elemento_ataque])
            mi_ataque_daños = []
            for elemento_defensa in range(0, 4):
                mi_ataque_daños.append(mi_ataque.calcular_danio([elementos[elemento_defensa]]))	
            daños_calculados.append(mi_ataque_daños)
        assert daños_esperados == daños_calculados, 'algun calculo de daño esta fallando'
	

    def test_se_puede_crear_un_ataque_especial_de_cada_elemento(self):
        a = Ataque_especial(Elemento.FUEGO)
        b = Ataque_especial(Elemento.AGUA)
        c = Ataque_especial(Elemento.TIERRA)
        d = Ataque_especial(Elemento.AIRE)


    def test_verificar_matriz_de_daño_especial(self):
        elementos = [ Elemento.AGUA , Elemento.FUEGO , Elemento.TIERRA , Elemento.AIRE ]
        daños_esperados = [[15, 18, 12, 15],[12,15,18,15],[15,15,15,15],[18,12,15,15]]
        daños_calculados = []
        for elemento_ataque in range(0, 4):
            mi_ataque = Ataque_especial(elementos[elemento_ataque])
            mi_ataque_daños = []
            for elemento_defensa in range(0, 4):
                mi_ataque_daños.append(mi_ataque.calcular_danio([elementos[elemento_defensa]]))	
            daños_calculados.append(mi_ataque_daños)
        assert daños_esperados == daños_calculados, 'algun calculo de daño esta fallando'

if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
