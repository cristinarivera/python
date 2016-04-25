#Programa para calcular el máximo de 5 numeros enteros.

a = int(raw_input('Valor del primer numero: '))
b = int(raw_input('Valor del segundo numero: '))
c = int(raw_input('Valor del tercer numero: '))
d = int(raw_input('Valor del cuarto numero: '))
e = int(raw_input('Valor del quinto numero: '))

candidato=a
if b>candidato:
    candidato=b
if c>candidato:
    candidato=c
if d>candidato:
    candidato=d
if  e>candidato:
    candidato=e

print 'El maximo es ', candidato