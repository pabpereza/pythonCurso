#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11 feb. 2017

@author: pablo

'''

class Persona(object):
    
    def __init__(self, nombre, DNI, direccion, telefono, email,saldo):
        ''' Constructor '''
        self.nombre = nombre
        self.dni = DNI
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.saldo = saldo
        
    def mostrar(self):
        print("Nombre: %s DNI: %s Direccion: %s Telefono: %s Email: %s" % (self.nombre,self.dni,self.direccion,self.telefono,self.email))



''' Volcamos el fichero en una lista de personas '''
fd = open("personas.txt")
lineas = fd.readlines()
fd.close()

personas = []
for linea in lineas:
    slinea = linea.split(";")
    personas.append(Persona(slinea[0],slinea[1],slinea[2],slinea[3],slinea[4],slinea[5]))
    

for person in personas:
    person.mostrar()