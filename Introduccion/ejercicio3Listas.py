lista = ["primero", 2, "3.5", 4.0, "ultimo"]

print("Lista completa: %s" %lista)
print("----------------------------")

''' Tamaño de la lista '''
print("Tamaño de la lista: %s" %(len(lista)))

''' Tamaño de la lista por el valor de su segunda posición '''
print("Tamaño de la lista por el valor de su segunda posición: %s" %(len(lista)*lista[1]))

''' El producto del segundo por el tercer elemento de la lista '''
print("El producto del segundo elemento de la lista por el tercero: %s" %(lista[1] * float(lista[2])))

''' Buscar el número dos en la lista '''
print("¿Esta el 2 en lista: %s ?¿Y 2.0? %s" %(2 in lista , 2.0 in lista))

''' Eliminar el primer valor '''
del(lista[0])
print("Lista sin el primer valor: %s" %lista)

''' Eliminar los dos últimos valores '''
del(lista[-2:])
print("Lista sin los dos últimos valores: %s" %lista)

''' Comprobar si la lista esta vacía '''
print("¿Contiene la lista elementos? %s" %(bool(lista)))

''' Añadir un nuevo elemento a la lista '''
lista.append("Nuevo último")
print("Lista con un nuevo registro: %s" %(lista))

