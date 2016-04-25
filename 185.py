bits=raw_input('Dame un numero octal sin decimales: ')

n=len(bits)
valor=0
for bit in bits:
    valor=valor+int(bit)*8**(n-1)
    n-=1
print 'Su valor decimal es' , valor