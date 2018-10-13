# Batallas de Monstruos

Trabajo Práctico Nº 1 para la materia Estructuras de Datos de la Universidad Nacional de Tres de Febrero (segundo cuatrimestre de 2018)

## Integrantes del grupo

- Amodey, Leandro. Legajo N° 35868
- Araneda, Alejandro. Legajo N° 46618
- Fraccini, Franco. Legajo N° 
- Monti, Matías. Legajo N° 45924

## Enunciado

> La idea de este primer trabajo práctico es reeditar la lucha de monstruos que realizaron
como primer trabajo de Algoritmos y Programación II, pero esta vez en python
para que puedan comparar las diferentes construcciones que proporciona el lenguaje.
Se recomienda que reescriban el TP desde cero y que no se limiten a una mera traducción
desde java a python. La idea es que utilicen las ventajas de un lenguaje como
python que soporta distintos paradigmas de programación. Para la resolución deberán
utilizar algo de introspección, persistencia y manejo de excepciones. La documentación
del TP se debe realizar en Jupyter, con copia de los módulos individuales y los tests unitarios.
También vamos a agregar persistencia, para que en cualquier momento se pueda
guardar una partida en disco y luego recuperarla y continuar.

Consultar el resto en https://sites.google.com/site/estructurasdedatosuntref/trabajos-practicos

## Instrucciones

### Ejecucion

El proyecto aún no es instalable automáticamente. Después de clonar el repositorio 
y hubicarse en el directorio raiz del proyecto, ejecutar en la línea de comandos
(python debe estar instalado):

    python -m batalla.aplicacion

Este comando ejecuta el módulo aplicación pero manteniendo en el `path` de python 
el direcitorio raiz del proyecto lo que permite resolver correctamente las direcciones
relativas de los `import`

### Test

Para correr los test unitarios, posicionarse en el directorio raiz del proyecto 
ya clonado y ejecutar en la línea de comandos:

   python -m unittest discover
   
Este comando correrá todos los modulos que empiecen con "test" en el paquete con
nombre "test" mientras que mantendrá el directorio raiz del proyecto en el `path`
de python permitiendo resolver correctamente los `import` relativos.

## Resolución

### Diagrama de clases

![Diagrama de clases](doc/batalla.png)

### Clase `Elemento`

Detalles de implementación en la Jupyter Notebook del [módulo `elemento`](doc/elemento.ipynb)

### Clases `Ataque` y `Ataque_especial`

Detalles de implementación en la Jupyter Notebook del [módulo `ataque`](doc/ataque.ipynb)

### Clase `Monstruo`

Detalles de implementación en la Jupyter Notebook del [módulo `monstruo`](doc/monstruo.ipynb)

### Clase `Batalla`

Detalles de implementación en la Jupyter Notebook del [módulo `batalla`](doc/batalla.ipynb)

### Clase `Jugador`

Detalles de implementación en la Jupyter Notebook del [módulo `jugador`](doc/jugador.ipynb)