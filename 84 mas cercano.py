#Programa que, dados cinco puntos, determina cuál de los cuatro últimos puntos es más cercano al primero.
from math import sqrt

x1 = int(raw_input('Valor de x1: '))
y1 = int(raw_input('Valor de y1: '))
x2 = int(raw_input('Valor de x2: '))
y2 = int(raw_input('Valor de y2: '))
x3 = int(raw_input('Valor de x3: '))
y3 = int(raw_input('Valor de y3: '))
x4 = int(raw_input('Valor de x4: '))
y4 = int(raw_input('Valor de y4: '))
x5 = int(raw_input('Valor de x5: '))
y5 = int(raw_input('Valor de y5: '))

p1p2=sqrt((x1-x2)**2 + (y1-y2)**2)
p1p3=sqrt((x1-x3)**2 + (y1-y3)**2)
p1p4=sqrt((x1-x4)**2 + (y1-y4)**2)
p1p5=sqrt((x1-x5)**2 + (y1-y5)**2)

candidato=(x2,y2)
if p1p2>p1p3:
    candidato=(x3,y3)
if p1p3>p1p4:
    candidato=(x4,y4)
if  p1p4>p1p5:
    candidato=(x5,y5)

print 'El punto mas cercano es ', candidato