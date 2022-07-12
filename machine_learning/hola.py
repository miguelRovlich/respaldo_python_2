# crea un perceptron
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self,n):
        self.pesos = np.random.rand(n)
        self.n = n

    def propagacion(self,entradas):
        self.salida = 1*(self.pesos.dot(entradas)>0)
        self.entradas = entradas
    
    def actualizacion(self,alfa,salidas):
        for i in range(self.pesos):
            self.pesos[i] = self.pesos[i] + alfa*(salidas-self.salida)*self.entradas[i]




perceptron_3_entradas = Perceptron(3)
print(perceptron_3_entradas.pesos)
print(perceptron_3_entradas.propagacion([1,0,1]))
