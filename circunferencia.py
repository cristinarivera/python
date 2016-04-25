print 'Programa para el calculo del area y perimetro de una circunferencia'

from math import pi

radio=float(raw_input('Dame el radio (en metros): '))

area=pi*radio**2
perimetro=2*pi*radio

print 'El area es de %.2f metros.' %area
print 'El perimetro es de %.2f metros.' %perimetro