#! /usr/bin/env python

""" Recibe una lista de enteros y calcula la media aritmetica """

enteros = [1, 5, 9, 12, 13, 19, 23, 27, 29, 30, 57, 59, 67, 83, 92, 98, 100]
media = 0

for x in enteros:
	media += x

print(media/len(enteros))
