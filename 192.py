cadena=raw_input('Introduce una cadena: ')

nuevacadena=''
for caracter in cadena:
    if caracter==' ':
        caracter=''
    nuevacadena=nuevacadena+caracter
        
inversion=''
for caracter in nuevacadena:   
    inversion=caracter+inversion
    
if inversion==nuevacadena:
    print 'La cadena es un palindromo.'
else:
    print 'La cadena no es un palindromo.'