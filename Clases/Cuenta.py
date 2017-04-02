#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Cree una clase llamada Cuenta. Como atributo tendr� un n�mero float llamado saldo, con una cantidad inicial de 0 euros.
Tendr� dos m�todos: 
ingresar, con un par�metro que indica la cantidad a sumar al saldo.
retirar, con un par�metro que ser� un n�mero float de euros a restar del saldo.

@author: pablo
'''

class Cuenta (object):
    '''
    Clase que gestiona el dinero de una cuenta corriente
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        self.saldo = 0
   
    ''' Metodo para ingresar dinero en la cuenta '''
    def ingresar(self,num):
        self.saldo += num
        
    ''' Metodo para retirar dinero de la cuenta '''
    def retirar(self,num):
        self.saldo -= num
        print(self.saldo)
        
'''if __name__ == '__main__':'''           
cuenta = Cuenta()
cuenta.ingresar(200)
cuenta.retirar(100)