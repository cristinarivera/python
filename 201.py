# Diseña un programa que, dados una cadena c, un indice i y un numero n, muestre la subcadena de c formada por los n caracteres que empiezan en la posicion de indice i.

cadena=raw_input('Dame una cadena: ')
i=int(raw_input('Dame un indice: '))
n=int(raw_input('Dame un numero: '))

subcadena=''
j=n+i
if j>len(cadena):
    final=len(cadena)
else:
    final=j
    
for k in range(i,final):
    subcadena+=cadena[k]
    
print 'La subcadena entre %d y %d + %d es %s.' % (i,i,n,subcadena)