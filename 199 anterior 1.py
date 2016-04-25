cadena=raw_input('Dame una cadena: ')
i=int(raw_input('Dame un numero: '))
j=int(raw_input('Dame otro numero: '))

subcadena=''
for k in range(i,j):
    subcadena+=cadena[k]
    
print 'La subcadena entre %d y %d es %s.' % (i,j,subcadena)