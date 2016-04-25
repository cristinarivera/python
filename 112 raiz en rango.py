from math import sqrt

x=float(raw_input('Introduce un numero entre 0 y 10: '))
while 10<x or x<0:
    x=float(raw_input('Introduce un numero entre 0 y 10: '))
    
print 'La raiz cuadrada de %.2f es %.2f' % (x, sqrt(x))