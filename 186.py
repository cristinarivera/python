bits=raw_input('Dame un numero hexadecimal sin decimales: ')

n=len(bits)
valor=0
for bit in bits:
    if bit=='A':
        bit=10
    if bit=='B':
        bit=11
    if bit=='C':
        bit=12
    if bit=='D':
        bit=13
    if bit== 'E':
        bit=14
    if bit=='F':
        bit=15
    
    valor=valor+int(bit)*16**(n-1)
    n-=1
print 'Su valor decimal es' , valor