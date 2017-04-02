cadena = "Cabeza grande, ojos hermosos"

''' Tamaño de la cadena '''
print(len(cadena))

''' Primeros cinco caracteres '''
print(cadena[:5])

''' Los siete ultimos caracteres '''
print(cadena[-7:])

''' Los cinco primeros caracteres de dos en dos '''
print(cadena[:5:2])

''' Los ultimos trece caracteres de tres en tres '''
print(cadena[-13::3])

''' En mayuscula los caracteres en posiciones multiplo de tres '''
print(cadena[::3].upper())

''' De dos en dos del caracter en la posicion 4 al del la 17 '''
print(cadena[4:17:2])

''' Esta el caracter "x" en la cadena '''
print(cadena.find("x"))

''' Buscar "o" en mayuscula o miniscula '''
print(cadena.find("o"))