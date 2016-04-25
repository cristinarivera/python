bits=raw_input('Dame un numero binario: ')

for bit in bits:
    
    if bit=='1' or bit=='0':
        valor=0
        for bit in bits:
            valor+=valor+int(bit)
        print 'Su valor decimal es' , valor
    else:
        print 'Numero binario mal formado'
        break       
    bits=raw_input('Dame un numero binario: ')   