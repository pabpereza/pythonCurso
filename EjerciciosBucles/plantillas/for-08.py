#! /usr/bin/env python

""" Para cada una de las cadenas de texto almacenadas en una lista, imprimir por
    pantalla el indice y la cadena en si e indicar si la palabra es demasiado
    corta (cinco o menos caracteres) o larga (mas de cinco caracteres) """


frase = """ Programmers are, in their hearts, architects, and the first thing
            they want to do when they get to a site is to bulldoze the place
            flat and build something grand """

listado = frase.split()    # listado = ["Programmers", "are", ",",...]

for x in listado:
	if(len(x)>5):
		print("La cadena: " + x + "  es larga")
	else:
		print("La cadena: " + x + "  es corta")
