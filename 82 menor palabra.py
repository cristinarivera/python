#Programa para calcular la menor de cinco palabras, siendo las may�sculas mayores que las min�sculas.
from  string import lower

a = raw_input('Primera palabra: ')
b = raw_input('Segunda palabra: ')
c = raw_input('Tercera palabra: ')
d = raw_input('Cuarta palabra: ')
e = raw_input('Quinta palabra: ')

a=lower(a)
b=lower(b)
c=lower(c)
d=lower(d)
e=lower(e)

candidato=a
if b<candidato:
    candidato=b
if c<candidato:
    candidato=c
if d<candidato:
    candidato=d
if  e<candidato:
    candidato=e

print 'El menor palabra es ', candidato