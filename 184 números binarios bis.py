bits=raw_input('Dame un numero binario: ')

for bit in bits:
    valor=0
    if bit!='1' or bit!='0':
        print 'Numero binario mal formado'
          
    bits=raw_input('Dame un numero binario: ')

    if bit=='1' or bit=='0':
        valor+=valor+int(bit)
        print 'Su valor decimal es' , valor

    