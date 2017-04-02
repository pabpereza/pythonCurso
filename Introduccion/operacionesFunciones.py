'''Funcion que recibe una lista de enteros y devuelve la suma de todos sus elementos. '''
def sumatorio(lista):
	total = 0
	for x in lista:
		total += x
	return total


'''Funcion que recibe tres parametros (x, y, z) y devuelve x ** y ** z .'''
def potencias(x , y, z):
	return(x**y**z)


'''Funcion que recibe una lista de enteros y devuelve otra lista con aquellos que son pares y >= 113''' 
def filtrarPares(lista):
	listaPares = []
	for x in lista:
		if(x%2==0):
			listaPares.append(x)
	return listaPares


'''Funcion que recibe una lista de enteros y calcula su media aritmetica'''
def media(lista):
	total = 0
	for x in lista:
		total += x
	return total/len(lista)


''' Funcion que calcula el factorial de un numero '''
def factorial(num):
	factorial = 1
	for x in range(1,num+1):
		factorial*=x
	return factorial


''' Funcion que recibe un numero y devuelve una lista con todos sus divisores''' 
def divisores(num):
	lista = []
	for x in range(1,int(num/2+1)):
		if(num%x == 0):
			lista.append(x)
	lista.append(num)
	return lista

print(divisores(120))

'''Funcion que determina si un numero es primo o no (devuelve True o False)'''
def primos(num):
	contador = 0
	for x in range(2,int(num/2+1)):
		if(num%x == 0):
			contador+=1
	if(contador==0):
		return "Es primo"
	else:
		return "No es primo"

