'''
Created on 10 feb. 2017

@author: pablo
'''

class Fichero(object):
    '''
    Clase que lee y muestra ficheros
    '''

    def __init__(self):
        ''' Constructor '''
        self.ruta = "personas.txt"
        self.texto = ""
        
    def leerFichero(self):
        self.fd = open(self.ruta,"r")
        self.texto = self.fd.read()
    
    def mostrarTexto(self):
        print(self.texto)


fichero = Fichero()
fichero.leerFichero()
fichero.mostrarTexto()