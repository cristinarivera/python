#Programa que nos dice si una letra es mayuscula o minuscula.

letra= raw_input('Dame una letra: ')

if letra>='a':
    if letra<='z':
        print 'Es minuscula'
if letra>='A':
    if letra<='Z':
        print 'Es mayuscula'
else:
    print 'No es una letra del alfabeto ingles'
        