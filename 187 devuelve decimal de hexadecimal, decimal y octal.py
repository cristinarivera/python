#Falta que calcule decimales, fracciones y que cuando introduzcas un número erróneo te lo indique
#si la cadena empieza por 0x o 0X se interpretar´a como un n´umero hexadecimal (ejemplo: ’0xff’ es 255); si no, si el primer car´acter es 0, la cadena se interpretar´a como un n´umero octal (ejemplo: ’017’ es 15); y si no, se interpretar´a como un n´umero decimal (ejemplo: ’99’ es 99).
bits=raw_input('Dame un numero: ')

n=len(bits)
valor=0
if bits[0]=='0':
    if bits[1]=='x' or bits[1]=='X':
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
            if bit== '0':
                bit=0
            if bit=='X':
                bit=0    
    
            valor=valor+int(bit)*16**(n-1)
            n-=1
    else:
        for bit in bits:
            valor=valor+int(bit)*8**(n-1)
            n-=1        
else:
    valor=bits
        
        
        
print 'Su valor decimal es' , valor