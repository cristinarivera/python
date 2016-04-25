cadena=raw_input('Introduce el nombre del archivo: ')

invertida=''
for caracter in cadena:
    invertida=caracter+invertida

extension=''
for caracter in invertida:
    if caracter=='.':
        break      
    extension=caracter+extension
    
print extension    