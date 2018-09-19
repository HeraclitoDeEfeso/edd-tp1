# -*- coding: utf-8 -*-
"""Test unitarios para el módulo ataque."""

import unittest
from ataque import Ataque
from elemento import Elemento

class TestAtaque(unittest.TestCase):

    def setUp(self):
        pass

    def test_se_puede_crear_un_ataque_de_cada_elemento(self):
        a = Ataque(Elemento.Fuego)
        b = Ataque(Elemento.Agua)
        c = Ataque(Elemento.Tierra)
        d = Ataque(Elemento.Aire)

    def test_verificar_matriz_de_daño(self):
        elementos = [ Elemento.Agua , Elemento.Fuego , Elemento.Tierra , Elemento.Aire ]
        daños_esperados = [[10, 12, 8, 10],[8,10,12,10],[10,10,10,10],[12,8,10,10]]
        daños_calculados = [[]]
        for elemento_ataque in range(0, 4):
            mi_ataque = Ataque(elmentos[elemento_ataque])
            for elemento_defensa in range(0, 4):
                daños_calculados[elemento_ataque][elemento_defensa] = miAtaque.calcularDaño(Elemento.elementos[elementoDefensa]);	
                assert daños_esperados == daños_calculados, 'algun calculo de daño esta fallando'
	

    def test_se_puede_crear_un_ataque_especial_de_cada_elemento(self):
        a = Ataque_especial(Elemento.Fuego)
        b = Ataque_especial(Elemento.Agua)
        c = Ataque_especial(Elemento.Tierra)
        d = Ataque_especial(Elemento.Aire)


    def test_verificar_matriz_de_daño_especial(self):
        elementos = [ Elemento.Agua , Elemento.Fuego , Elemento.Tierra , Elemento.Aire ]
        daños_esperados = [[15, 18, 12, 15],[12,15,18,15],[15,15,15,15],[18,12,15,15]]
        daños_calculados = [[]]
        for elemento_ataque in range(0, 4):
            mi_ataque = Ataque_especial(elmentos[elemento_ataque])
            for elemento_defensa in range(0, 4):
                daños_calculados[elemento_ataque][elemento_defensa] = miAtaque.calcularDaño(Elemento.elementos[elementoDefensa]);	
                assert daños_esperados == daños_calculados, 'algun calculo de daño esta fallando'

if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
