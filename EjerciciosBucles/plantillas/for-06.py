#! /usr/bin/env python

""" A partir de dos listas de enteros, 'numeros1' y 'numeros2' de igual tamano,
    generar otra cuyo primer elemento es el producto del primer elemento de
    las listas 'numeros1' y 'numeros2', y asi sucesivamente. """


numeros1 = [1, 7, 13, 21, 27]
numeros2 = [4, 6, 10, 18, 23]

lista = []

for x in range(6):
	lista.append(numeros1[x] * numeros2[x] )