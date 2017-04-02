class Calculadora (object):
	def __init__(self , num1, num2):
		self.op1 = num1
		self.op2 = num2

	def sumar(self):
		return self.op1 + self.op2
	def restar(self):
		return self.op1 - self.op2
	def multiplicar(self):
		return self.op1 * self.op2
	def dividir(self):
		return self.op1 / self.op2
