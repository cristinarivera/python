cadena=raw_input('Introduce una cadena: ')

nuevacadena=''
for caracter in cadena:
    if caracter=='a' or (caracter=='e' or  (caracter=='i' or (caracter=='o' or caracter=='u' ))):
        caracter='.'
    nuevacadena=nuevacadena+caracter

print nuevacadena