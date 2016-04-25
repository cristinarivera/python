cadena=raw_input('Introduce una cadena: ')

inversion=''
for caracter in cadena:
    inversion=caracter+inversion
    
if inversion==cadena:
    print 'La cadena es un palindromo.'
else:
    print 'La cadena no es un palindromo.'