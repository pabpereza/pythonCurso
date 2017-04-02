def saludar():
    print("Hola!")


def resta(a= None , b = None):
    if a == None or b == None:
        print("Error, debes enviar dos numeros")
        return
    else:
        return a-b


def indeterminados(*args):
    for arg in args:
        print(arg)


def indeterminados_nombre(**kwargs):
   for kwarg in kwargs:
       print(kwarg," ", kwargs[kwarg])


def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminador es",t)
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])


''' Funciones recursivas '''

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Booooom!")




''' Funciones integradas '''
n = int("10")
f = float("10.5")
c = "Un texto y un numero " + str(10)

binario = bin(10)
hexadecimal = hex(10)
entero = int('0b1010',2)
hexadecimal = int('0xa',16)

abs(-10)
round(5.5)
eval('2+5')

n = 10
eval('n*10-5')





