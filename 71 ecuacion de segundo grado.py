#Programa para calcular ecuaciones de segundo grado dados a, b y c (ax2 +bx +c = 0 )
from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if a == 0 and b== 0 and c== 0:
    print 'La ecuacion tiene infinitas soluciones.'
else:
    if a== 0 and b== 0:
        print 'La ecuacion no tiene solucion.'
    else:
        if a== 0:
            x= -c/b
            print 'Solucion de la ecuacion: x=%4.3f' %x
        else:
            x1 = (-b+sqrt(b**2-4*a*c)) / (2*a)
            x2 = (-b-sqrt(b**2-4*a*c)) / (2*a)
            print 'Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f' % (x1,x2)