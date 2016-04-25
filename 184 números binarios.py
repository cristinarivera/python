bits=raw_input('Dame un numero binario: ')

valor=0

for bit in bits:
    if bit!='1' or bit!='0':
        print 'Numero binario mal formado'
        break    

    if bit=='1' or bit=='0':
        valor+=valor+int(bit)
        print 'Su valor decimal es' , valor

bits=raw_input('Dame un numero binario: ')        