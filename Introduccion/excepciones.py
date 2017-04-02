def mayorEntreMenor(num1,num2):
	try:
		if( num1 > num2 ):
			return (num1/num2)
		else:
			return num2/num1
	except ZeroDivisionError:
		return "No se puede dividir entre cero"

num1 = int(input())
num2 = int(input())
print(mayorEntreMenor(num1,num2))

	
""" Programa que lee nombres de fichero hasta que se introduce alguno que realmente existe """



""" Programa que busca un elemento en una lista y devuelve su índice """
def buscador(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1


numeros = range(30)
buscado = 18
print(encuentra(numeros, buscado))


""" Devuelve la suma de todos los elementos de la lista introducida"""
def suma(lista):
    try:
        return sum(lista)
    except TypeError:
        return None

a_sumar = [1, 4, 5, 3.2, 4.4, "2,3", 3.5]
print(suma(a_sumar))


""" Programa que devuelve un elemento de una lista a partir del indice introducido """
def extrae(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None

lista    = [2,3,4]
posicion = 13
print(extrae(lista, posicion))