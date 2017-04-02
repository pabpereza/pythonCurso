'''
Created on 12 feb. 2017

@author: pablo
'''
import math

class Punto(object):

    def __init__(self, x,y,ox,oy):
        self.x = x
        self.y = y
        self.ox = ox
        self.oy = oy
    
    def distancia(self):
        print(math.sqrt ((self.x- self.ox)**2 + (self.y-self.oy)**2))
    
    def muestra_punto(self):
        print("(%s,%s)" % (self.x , self.y))
        

punto1 = Punto(3,4,0,0)
punto2 = Punto(7,2,0,0)

punto1.distancia()
punto2.distancia()