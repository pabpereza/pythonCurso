#-------Variables------------#
#----------------------------#
abecedario = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mensaje = input("Introduce un mensaje \n")
clave = 5
auxcontador = 0
mensajeCifrado = ""

#--------Algoritmo------------#
#-----------------------------#
#Transformar la cadena a minusculas
mensaje = mensaje.lower()

#Se recorren todas las letras del mensaje
for caracter in mensaje:
	#Si es un espacio no se realiza accion
	if (caracter == " "):
		mensajeCifrado += " "
	else:
		contador=0
		#Se comprueba cada letra con todas las des abecedario
		for indexAbecedario in abecedario:
			if (caracter == indexAbecedario):
				auxcontador = contador
				#Si la posicion de la letra en el abecedario mas el valor de la clave es superior
				#al numero de letras de abecedario se corrige para no desbordar el array
				if((contador+clave)>27):
					auxcontador = contador - 26
				#Se concatena al mensaje cifrado la letra que le corresponde
				mensajeCifrado += abecedario[ auxcontador + clave ]
				break
			contador += 1

#Se muestra el mensaje cifrado
print(mensajeCifrado)


