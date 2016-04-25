#Programa que, dados cinco números enteros, determina cuál de los cuatro últimos números es más cercano al primero.

a = int(raw_input('Valor del primer numero: '))
b = int(raw_input('Valor del segundo numero: '))
c = int(raw_input('Valor del tercer numero: '))
d = int(raw_input('Valor del cuarto numero: '))
e = int(raw_input('Valor del quinto numero: '))

ab=abs(a-b)
ac=abs(a-c)
ad=abs(a-d)
ae=abs(a-e)

candidato=b
if ab>ac:
    candidato=c
if ac>ad:
    candidato=d
if  ad>ae:
    candidato=e

print 'El mas cercano es ', candidato