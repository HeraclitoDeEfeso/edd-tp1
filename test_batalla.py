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

    def test_si_se_crea_una_batalla_el_primer_jugador_inicia(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        self.assertEqual("Natalia", mi_batalla.jugador_atacante)

    def test_si_se_crea_una_batalla_el_primer_turno_tiene_ataque_especial(self):
        mi_batalla = Batalla("Natalia", Elemento.AGUA, Elemento.FUEGO, "Pedro", Elemento.AIRE, Elemento.TIERRA)
        mi_monstruo = mi_batalla.jugador_atacante.monstruo
        self.assertTrue(Elemento.FUEGO in mi_monstruo.generar_opciones() and mi_monstruo.ataques_especiales_restantes)

if __name__=="__main__":

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

"""
public class BatallaTest {

    def test_siSeCreaUnaBatallaConUnJugadorNataliaDeAguaYFuegoYOtroDeAireYTierraDespuesDeAtaqueEspecialDeFuegoLaVidaRestanteEs82():
        Batalla miBatalla = new Batalla("Natalia", new Agua(), new Fuego(), "Pedro", new Aire(), new Tierra());
        Ataque miAtaque = miBatalla.obtenerJugadorAtacante().obtenerMonstruo().generarAtaqueEspecial(new Fuego());
        miBatalla.jugada(miAtaque);
        assertEquals(82, miBatalla.obtenerJugadorAtacante().obtenerMonstruo().obtenerEstadoVital(), 0.1);
    }

    def test_siSeCreaUnaBatallaConUnJugadorDeAguaYFuegoYOtroPEdroDeAireYTierraSiASuTurnoPedroAtacaConEspecialDeAireAlOtroLeResta85DeVida():
        Batalla miBatalla = new Batalla("Natalia", new Agua(), new Fuego(), "Pedro", new Aire(), new Tierra());
        Ataque ataqueNatalia = miBatalla.obtenerJugadorAtacante().obtenerMonstruo().generarAtaqueEspecial(new Fuego());
        miBatalla.jugada(ataqueNatalia);
        Ataque ataquePedro = miBatalla.obtenerJugadorAtacante().obtenerMonstruo().generarAtaqueEspecial(new Aire());
        miBatalla.jugada(ataquePedro);
        assertEquals(85, miBatalla.obtenerJugadorAtacante().obtenerMonstruo().obtenerEstadoVital(), 0.1);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConNombreNuloDelPrimerJugador() :
        new Batalla(null, new Agua(), null, "Pedro", new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConNombreNuloDelSegundoJugador() :
        new Batalla("Natalia", new Agua(), null, null, new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConNombresNulosDeJugadores() :
        new Batalla(null, new Agua(), null, null, new Aire(), null);
    }
    
    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConNombreVacioDelPrimerJugador() :
        new Batalla("", new Agua(), null, "Pedro", new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConNombreVacioDelSegundoJugador() :
        new Batalla("Natalia", new Agua(), null, "", new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConNombresVaciosDeJugadores() :
        new Batalla("", new Agua(), null, "", new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConLosMismoNombresDeJugadores() :
        new Batalla("Natalia", new Agua(), null, "Natalia", new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConElementosNulosDelPrimerJugador() :
        new Batalla("Natalia", null, null, "Pedro", new Aire(), null);
    }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConElementosNulosDelSegundoJugador() :
        new Batalla("Natalia", new Agua(), null, "Pedro", null, null);
        }

    @Test(expected=Exception.class)
    def noSePuedeCrearUnaBatallaConElementosNulosDeJugadores() :
        new Batalla("Natalia", null, null, "Pedro", null, null);
        }

    @Test(expected = ParametroNuloException.class)
    def noSePuedeJugarUnAtaqueNulo() :
        Batalla miBatalla = new Batalla("Natalia", new Agua(), null, "Pedro", new Aire(), null);
        miBatalla.jugada(null);
        }

    def test_despuesDeUnaJugadaAvanzaElTurno() :
        Batalla miBatalla = new Batalla("Natalia", new Agua(), null, "Pedro", new Aire(), null);
        Jugador jugadorAtacante = miBatalla.obtenerJugadorAtacante();
        Monstruo monstruoAtacante = jugadorAtacante.obtenerMonstruo();
        miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
        assertTrue(jugadorAtacante == miBatalla.obtenerJugadorDefensor());
        }
    def test_unaVezTerminadaUnaBatallaElGanadorEsElDefensorPorqueAvanzaElTurno() :
        Batalla miBatalla = new Batalla("Natalia", new Agua(), null, "Pedro", new Aire(), null);
        do {
                Monstruo monstruoAtacante = miBatalla.obtenerJugadorAtacante().obtenerMonstruo();
                miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
        } while (!miBatalla.termino());
        assertTrue(miBatalla.obtenerJugadorDefensor() == miBatalla.obtenerGanador());
        }

    def test_unaVezTerminadaUnaBatallaDespuesDeUnaJugadaSigueTerminada() :
        Batalla miBatalla = new Batalla("Natalia", new Agua(), null, "Pedro", new Aire(), null);
        do {
                Monstruo monstruoAtacante = miBatalla.obtenerJugadorAtacante().obtenerMonstruo();
                miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
            } while (!miBatalla.termino());
            Jugador atacante = miBatalla.obtenerJugadorAtacante();
            Monstruo monstruoAtacante = atacante.obtenerMonstruo();
            miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
            assertTrue(miBatalla.termino());
            }

    def test_unaVezTerminadaUnaBatallaUnaNuevaJugadaNoVuelveACambiarElTurno() :
        Batalla miBatalla = new Batalla("Natalia", new Agua(), null, "Pedro", new Aire(), null);
        do {
                Monstruo monstruoAtacante = miBatalla.obtenerJugadorAtacante().obtenerMonstruo();
                miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
            } while (!miBatalla.termino());
        Jugador atacante = miBatalla.obtenerJugadorAtacante();
        Monstruo monstruoAtacante = atacante.obtenerMonstruo();
        miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
        assertTrue(atacante == miBatalla.obtenerJugadorAtacante());
        }

    def test_unaVezTerminadaUnaBatallaUnaNuevaJugadaNoTieneEfectoEnLaVidaDeLosMonstruos() :
        Batalla miBatalla = new Batalla("Natalia", new Agua(), null, "Pedro", new Aire(), null);
        do {
                Monstruo monstruoAtacante = miBatalla.obtenerJugadorAtacante().obtenerMonstruo();
                miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
                } while (!miBatalla.termino());
        Jugador atacante = miBatalla.obtenerJugadorAtacante(), defensor = miBatalla.obtenerJugadorDefensor();
        Monstruo monstruoAtacante = atacante.obtenerMonstruo(), monstruoDefensor = defensor.obtenerMonstruo();
        float vidaAtacate = monstruoAtacante.obtenerEstadoVital(), vidaDefensor = monstruoDefensor.obtenerEstadoVital();
        miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
        assertTrue(vidaAtacate == miBatalla.obtenerJugadorAtacante().obtenerMonstruo().obtenerEstadoVital()
        && vidaDefensor == miBatalla.obtenerJugadorDefensor().obtenerMonstruo().obtenerEstadoVital());
        }

    def test_todasLasPosiblesBatallasDeJuguadoresConUnElementoDebenTerminarEnHasta20Jugadas() :
        Elemento[] elementos = { new Agua(), new Fuego(), new Tierra(), new Aire() };
        boolean es20elLimiteDeJugadas = true;
        for (Elemento elementoAtacante : elementos) {
                for (Elemento elementoDefensor : elementos) {
                        Batalla miBatalla = new Batalla("Natalia", elementoAtacante, null, "Pedro", elementoDefensor, null);
                        for (int i = 0; i < 20; i++) {
                                Monstruo monstruoAtacante = miBatalla.obtenerJugadorAtacante().obtenerMonstruo();
                                miBatalla.jugada(monstruoAtacante.generarAtaque(monstruoAtacante.generarOpciones()[0]));
                                }
                        es20elLimiteDeJugadas &= miBatalla.termino();
                        }
                        }
                        assertTrue(es20elLimiteDeJugadas);
                        }
                        }

"""