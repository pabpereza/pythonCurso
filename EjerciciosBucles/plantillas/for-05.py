#! /usr/bin/env python

""" A partir de dos listas de enteros, 'numeros1' y 'numeros2', crea una lista
    que contiene aquellos valores de la primera que tambien estan en la segunda
    e imprimela por pantalla. Es decir, calcula la interseccion de ambas listas. """


numeros1 = [1, 7, 13, 21, 27, 29, 34, 48, 50, 51, 53, 61, 68, 74, 82, 83, 84, 87, 92, 94]
numeros2 = [4, 6, 10, 18, 23, 29, 30, 32, 43, 54, 55, 55, 71, 76, 77, 82, 88, 92, 94, 95]
lista = []


for x in numeros1:
	try:
		lista.append(numeros2[numeros2.index(x)])
		break
	except ValueError:
		break
		
print(lista) 