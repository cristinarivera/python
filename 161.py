a=raw_input('Dame una cadena: ')
digito=0
for i in range(len(a)):
    if a[i]>='0' and a[i]<='9':
        digito+=1
if digito>0:
    print 'Contiene digito'
else:
    print 'No contiene digito'
