#Programa para determinar que un texto no contiene letras mayúsculas.
from string import lower

a=raw_input('Texto en minusculas: ')

a_min=lower(a)

while a<a_min:
    a=raw_input('Texto en minusculas: ')
    