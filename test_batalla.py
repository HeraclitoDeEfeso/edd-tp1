# -*- coding: utf-8 -*-
"""
Test unitarios para el módulo batalla.
"""
import unittest
from batalla import Batalla
from elemento import Elemento

class TestBatalla(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_se_puede_crear_una_batalla(self):
        Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)

    def test_creada_una_batalla_el_primer_jugador_definido_inicia(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        self.assertEqual("Natalia", mi_batalla.__jugador_atacante__.__nombre__)

    def test_creada_una_batalla_el_primer_turno_tiene_ataque_especial(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        mi_monstruo = mi_batalla.__jugador_atacante__.__monstruo__
        self.assertTrue(Elemento.FUEGO in mi_monstruo.generar_opciones() and mi_monstruo.__ataques_especiales_restantes__)

    def test_creada_una_batalla_si_un_jugador_aire_y_tierra_recibe_ataque_especial_de_fuego_su_vida_restante_es_82(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        mi_ataque = mi_batalla.__jugador_atacante__.__monstruo__.generar_ataque_especial(Elemento.FUEGO)
        mi_batalla.jugada(mi_ataque)
        self.assertEqual(82, mi_batalla.__jugador_atacante__.__monstruo__.__estado_vital__)

    def test_creada_una_batalla_si_un_jugador_agua_y_fuego_recibe_ataque_especial_de_aire_su_vida_restante_es_85(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        mi_ataque = mi_batalla.__jugador_atacante__.__monstruo__.generar_ataque_especial(Elemento.FUEGO)
        mi_batalla.jugada(mi_ataque)
        mi_ataque = mi_batalla.__jugador_atacante__.__monstruo__.generar_ataque_especial(Elemento.AIRE)
        mi_batalla.jugada(mi_ataque)
        self.assertEqual(85, mi_batalla.__jugador_atacante__.__monstruo__.__estado_vital__)

    def test_no_se_puede_crear_una_batalla_con_cadena_vacia_como_nombre_del_primer_jugador(self):
        self.assertRaises(Exception, Batalla, "", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)

    def test_no_se_puede_crear_una_batalla_con_cadena_vacia_como_nombre_del_segundo_jugador(self):
        self.assertRaises(Exception, Batalla, "Natalia", Elemento.AGUA, Elemento.FUEGO, "", Elemento.AIRE, Elemento.TIERRA)

    def test_no_se_puede_crear_una_batalla_con_los_mismo_nombres_de_jugadores(self):
        self.assertRaises(Exception, Batalla, "Natalia", Elemento.AGUA, Elemento.FUEGO, "Natalia", Elemento.AIRE, Elemento.TIERRA)

    def test_despues_de_una_jugada_avanza_el_turno(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        mi_jugador_atacante = mi_batalla.__jugador_atacante__
        mi_ataque = mi_jugador_atacante.__monstruo__.generar_ataque_especial(Elemento.FUEGO)
        mi_batalla.jugada(mi_ataque)
        self.assertNotEqual(mi_jugador_atacante, mi_batalla.__jugador_atacante__)

    def test_terminada_una_batalla_el_ganador_es_el_defensor_porque_el_ultimo_ataque_avanzo_el_turno(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        while not mi_batalla.termino():
            mi_monstruo = mi_batalla.__jugador_atacante__.__monstruo__
            mi_batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        self.assertEqual(mi_batalla.__jugador_defensor__, mi_batalla.ganador())

    def test_terminada_una_batalla_si_se_intenta_otra_jugada_sigue_terminada(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        while not mi_batalla.termino():
            mi_monstruo = mi_batalla.__jugador_atacante__.__monstruo__
            mi_batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        mi_monstruo = mi_batalla.__jugador_atacante__.__monstruo__
        mi_batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        self.assertTrue(mi_batalla.termino())
        
    def test_terminada_una_batalla_si_se_intenta_otra_jugada_no_cambia_el_turno(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        while not mi_batalla.termino():
            mi_monstruo = mi_batalla.__jugador_atacante__.__monstruo__
            mi_batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        mi_jugador = mi_batalla.__jugador_atacante__
        mi_monstruo = mi_jugador.__monstruo__
        mi_batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        self.assertEqual(mi_jugador, mi_batalla.__jugador_atacante__)

    def test_terminada_una_batalla_si_se_intenta_otra_jugada_no_tiene_efecto_en_la_vida_de_los_monstruos(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        while not mi_batalla.termino():
            mi_monstruo = mi_batalla.__jugador_atacante__.__monstruo__
            mi_batalla.jugada(mi_monstruo.generar_ataque(mi_monstruo.generar_opciones()[0]))
        jugador_atacante = mi_batalla.__jugador_atacante__
        jugador_defensor = mi_batalla.__jugador_defensor__
        monstruo_atacante = jugador_atacante.__monstruo__
        monstruo_defensor = jugador_defensor.__monstruo__
        estado_vital_monstruo_atacante = monstruo_atacante.__estado_vital__
        estado_vital_monstruo_defensor = monstruo_defensor.__estado_vital__
        mi_batalla.jugada(monstruo_atacante.generar_ataque(monstruo_atacante.generar_opciones()[0]))
        self.assertTrue(estado_vital_monstruo_atacante, monstruo_atacante.__estado_vital__)
        self.assertTrue(estado_vital_monstruo_defensor, monstruo_defensor.__estado_vital__)

if __name__=="__main__":

    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)