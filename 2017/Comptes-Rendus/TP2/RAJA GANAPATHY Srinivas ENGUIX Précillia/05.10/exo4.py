
#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock
#from exo1 import f

def f(x):
	return sqrt(1 - x**2)

def simpson(f, a, b, n):
	h = (b - a) / n
	k = 0.0
	x = a + h
	for i in range(1, n/2 + 1):
		x += 4*f(x)
		k += 2*h
	x = a + 2*h
	for i in range(1, n/2):
		x += 2 * h
		k += 2 * f(x)
	return (h/3) * (f(a) + f(b) + k)


print('Methode de Simpson')
a = -0.5
b = 0.5
n = 10
x = simpson(f, a, b, n)
print(x)
