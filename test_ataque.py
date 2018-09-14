# -*- coding: utf-8 -*-
"""
Test unitarios para el módulo ataque.
"""
import unittest
from ataque import Ataque
from elemento import Elemento

class TestAtaque(unittest.TestCase):

    def setUp(self):
        pass
"""
        Ataque:
        
        @Test
	public void sePuedeCrearUnAtaqueDeAgua() throws ParametroNuloException {
		new Ataque(new Agua());
	}
	
	@Test
	public void sePuedeCrearUnAtaqueDeFuego() throws ParametroNuloException {
		new Ataque(new Fuego());
	}

	@Test
	public void sePuedeCrearUnAtaqueDeAire() throws ParametroNuloException {
		new Ataque(new Aire());
	}
	
	@Test
	public void sePuedeCrearUnAtaqueDeTierra() throws ParametroNuloException {
		new Ataque(new Tierra());
	}
	
	@Test(expected=Exception.class)
	public void noSePuedeCrearUnAtaqueNulo() throws ParametroNuloException {
		new Ataque(null);
	}
	
	@Test
	public void verificarMatrizDeDaño() throws ParametroNuloException {
		Elemento[] elementos = {new Agua(), new Fuego(), new Tierra(), new Aire()};
		float[][] dañosEsperados = {{10, 12, 8, 10},{8,10,12,10},{10,10,10,10},{12,8,10,10}};
		float[][] dañosCalculados = new float[4][4];
		for(int elementoAtaque = 0; elementoAtaque < 4; elementoAtaque++) {
			Ataque miAtaque = new Ataque(elementos[elementoAtaque]);
			for(int elementoDefensa = 0; elementoDefensa < 4; elementoDefensa++) {
				dañosCalculados[elementoAtaque] [elementoDefensa]
						= miAtaque.calcularDaño(new Elemento[] {elementos[elementoDefensa]});	
			}
		}
		assertTrue(Arrays.deepEquals(dañosEsperados, dañosCalculados));
	}
	---------------------------
	public class AtaqueEspecialTest {
	

	@Test
	public void sePuedeCrearUnAtaqueEspecialDeAgua() throws ParametroNuloException {
		new AtaqueEspecial(new Agua());
	}
	
	@Test
	public void sePuedeCrearUnAtaqueEspecialDeFuego() throws ParametroNuloException {
		new AtaqueEspecial(new Fuego());
	}

	@Test
	public void sePuedeCrearUnAtaqueEspecialDeAire() throws ParametroNuloException {
		new AtaqueEspecial(new Aire());
	}
	
	@Test
	public void sePuedeCrearUnAtaqueEspecialDeTierra() throws ParametroNuloException {
		new AtaqueEspecial(new Tierra());
	}
	
	@Test
	public void unAtaqueEspecialEsUnAtaque() throws ParametroNuloException {
		Ataque miAtaque = new AtaqueEspecial(new Agua());
	}

	@Test(expected=ParametroNuloException.class)
	public void noSePuedeCrearUnAtaqueEspecialNulo() throws ParametroNuloException {
		new AtaqueEspecial(null);
	}
	
	@Test
	public void verificarMatrizDeDaño() throws ParametroNuloException {
		Elemento[] elementos = {new Agua(), new Fuego(), new Tierra(), new Aire()};
		float[][] dañosEsperados = {{15, 18, 12, 15},{12,15,18,15},{15,15,15,15},{18,12,15,15}};
		float[][] dañosCalculados = new float[4][4];
		for(int elementoAtaque = 0; elementoAtaque < 4; elementoAtaque++) {
			Ataque miAtaque = new AtaqueEspecial(elementos[elementoAtaque]);
			for(int elementoDefensa = 0; elementoDefensa < 4; elementoDefensa++) {
				dañosCalculados[elementoAtaque][elementoDefensa] 
						= miAtaque.calcularDaño(new Elemento[] {elementos[elementoDefensa]});	
			}
		}
		assertTrue(Arrays.deepEquals(dañosEsperados, dañosCalculados));
	}
"""
