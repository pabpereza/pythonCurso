'''
Created on 23 feb. 2017

@author: pablo
'''

lista = [1, 5, 3, 7, 6, 3, 2, 4]

a = list(map(lambda x: x ** 2,lista ))

a = list(filter( lambda x: x>20 , a ))

print(a)