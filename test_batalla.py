# -*- coding: utf-8 -*-
"""
Test unitarios para el módulo batalla.
"""
import unittest
from batalla import Batalla
from elemento import Elemento

class TestBatalla(unittest.TestCase):
    
    def setUp(self):
        self.batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)

    def test_se_puede_crear_una_batalla(self):
        self.assertIsInstance(self.batalla, Batalla)

    def test_se_puede_crear_una_batalla_con_primer_jugador_con_un_solo_elemento_1(self):
        Batalla("Natalia", Elemento.AGUA, Elemento.NADA, "Pedro", Elemento.AIRE, Elemento.TIERRA)

    def test_se_puede_crear_una_batalla_con_primer_jugador_con_un_solo_elemento_2(self):
        Batalla("Natalia", Elemento.NADA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)

    def test_se_puede_crear_una_batalla_con_segundo_jugador_con_un_solo_elemento_1(self):
        Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.NADA)

    def test_se_puede_crear_una_batalla_con_segundo_jugador_con_un_solo_elemento_2(self):
        Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.NADA, Elemento.TIERRA)

    def test_no_se_puede_crear_una_batalla_con_cadena_vacia_como_nombre_del_primer_jugador(self):
        self.assertRaises(Exception, Batalla, "", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)

    def test_no_se_puede_crear_una_batalla_con_cadena_vacia_como_nombre_del_segundo_jugador(self):
        self.assertRaises(Exception, Batalla, "Natalia", Elemento.AGUA, Elemento.FUEGO, "", Elemento.AIRE, Elemento.TIERRA)

    def test_no_se_puede_crear_una_batalla_con_los_mismo_nombres_de_jugadores(self):
        self.assertRaises(Exception, Batalla, "Natalia", Elemento.AGUA, Elemento.FUEGO, "Natalia", Elemento.AIRE, Elemento.TIERRA)

    def test_creada_una_batalla_el_primer_jugador_definido_inicia(self):
        self.assertEqual("Natalia", self.batalla.__jugador_atacante__.__nombre__)

    def test_creada_una_batalla_el_primer_turno_tiene_ataque_especial(self):
        self.assertTrue(self.batalla.__jugador_atacante__.__monstruo__.__ataques_especiales_restantes__ > 0)

    def test_despues_de_una_jugada_avanza_el_turno(self):
        mi_jugador_atacante = self.batalla.__jugador_atacante__
        mi_ataque = mi_jugador_atacante.__monstruo__.generar_ataque_especial(Elemento.FUEGO)
        self.batalla.jugada(mi_ataque)
        self.assertNotEqual(mi_jugador_atacante, self.batalla.__jugador_atacante__)

    def test_creada_una_batalla_si_un_jugador_aire_y_tierra_recibe_ataque_especial_de_fuego_su_vida_restante_es_82(self):
        mi_ataque = self.batalla.__jugador_atacante__.__monstruo__.generar_ataque_especial(Elemento.FUEGO)
        self.batalla.jugada(mi_ataque)
        self.assertEqual(82, self.batalla.__jugador_atacante__.__monstruo__.__estado_vital__)

    def test_creada_una_batalla_si_un_jugador_agua_y_fuego_recibe_ataque_especial_de_aire_su_vida_restante_es_85(self):
        mi_ataque = self.batalla.__jugador_atacante__.__monstruo__.generar_ataque_especial(Elemento.FUEGO)
        self.batalla.jugada(mi_ataque)
        mi_ataque = self.batalla.__jugador_atacante__.__monstruo__.generar_ataque_especial(Elemento.AIRE)
        self.batalla.jugada(mi_ataque)
        self.assertEqual(85, self.batalla.__jugador_atacante__.__monstruo__.__estado_vital__)

class TestBatallaTerminada(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        while not batalla.termino():
            mi_monstruo = batalla.__jugador_atacante__.__monstruo__
            batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        cls.batalla = batalla

    def test_terminada_una_batalla_el_ganador_es_el_defensor_porque_el_ultimo_ataque_avanzo_el_turno(self):
        self.assertEqual(self.batalla.__jugador_defensor__, self.batalla.ganador())

    def test_terminada_una_batalla_si_se_intenta_otra_jugada_sigue_terminada(self):
        mi_monstruo = self.batalla.__jugador_atacante__.__monstruo__
        self.batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        self.assertTrue(self.batalla.termino())
        
    def test_terminada_una_batalla_si_se_intenta_otra_jugada_no_cambia_el_turno(self):
        mi_jugador = self.batalla.__jugador_atacante__
        mi_monstruo = mi_jugador.__monstruo__
        self.batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        self.assertEqual(mi_jugador, self.batalla.__jugador_atacante__)

    def test_terminada_una_batalla_si_se_intenta_otra_jugada_no_tiene_efecto_en_la_vida_de_los_monstruos(self):
        jugador_atacante = self.batalla.__jugador_atacante__
        jugador_defensor = self.batalla.__jugador_defensor__
        monstruo_atacante = jugador_atacante.__monstruo__
        monstruo_defensor = jugador_defensor.__monstruo__
        estado_vital_monstruo_atacante = monstruo_atacante.__estado_vital__
        estado_vital_monstruo_defensor = monstruo_defensor.__estado_vital__
        self.batalla.jugada(monstruo_atacante.generar_ataque(monstruo_atacante.generar_opciones()[0]))
        self.assertEqual(estado_vital_monstruo_atacante, monstruo_atacante.__estado_vital__)
        self.assertEqual(estado_vital_monstruo_defensor, monstruo_defensor.__estado_vital__)

if __name__=="__main__":

    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)
