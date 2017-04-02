v = "otro texto"
n = 10
print("Un texto",v,"y un numero",n)

c = "Un texto '{}' y un número '{}'".format(v,n)
print(c)


c = "Un texto '{1}' y un número '{0}'".format(v,n)
print(c)


c = "Un texto '{t}' y un número '{n}'".format(n=n,t=v)
print(c)

''' Alinear salida a la derecha segun el numero de caracteres'''
print( "{:>30}".format("palabra"))

''' Alinear salida a la izquierda segun el numero de caracteres'''
print( "{:30}".format("palabra"))

''' Alinear salida al centro segun el numero de caracteres'''
print( "{:^30}".format("palabra"))


''' Truncamiento '''
print("{:.5}".format("palabra"))


''' Truncamiento con alineacion '''
print("{:>30.5}".format("palabra"))


''' Formateo de numeros rellenando espacios '''
print( "{:4d}".format(10) )
print( "{:4d}".format(100) )
print( "{:4d}".format(1000) )


''' Formateo de numeros rellenando espacios con numeros '''
print( "{:04d}".format(10) )
print( "{:04d}".format(100) )
print( "{:04d}".format(1000) )


''' Formateo de números flotantes, rellenados por espacios '''
print( "{:7.3f}".format(3.1415926) )
print( "{:7.3f}".format(152.21) )

''' Formateo de números flotantes, rellenados por caracteres '''
print( "{:07.3f}".format(3.1415926) )
print( "{:07.3f}".format(152.21) )