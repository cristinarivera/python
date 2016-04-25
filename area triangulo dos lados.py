from math import sin, pi

print 'Programa para el calculo del área de un triangulo'
a=float(raw_input('Dame lado a: '))
b=float(raw_input('Dame lado b: '))
zeta=float(raw_input('Dame angulo entre los lados: '))

area=(1/2.)*a*b*sin(zeta*pi/180)

print 'El area del triangulo es: ' + str(area) + ' metros cuadrados'