#Programa para pasar de octal a binario
octal=raw_input('Dame un numero en octal para pasarlo a binario: ')

nbin=' ' 
for bit in octal:
    if bit=='0':
        bit='000'
    if bit=='1':
        bit='001'        
    if bit=='2':
        bit='010'
    if bit=='3':
        bit='011'
    if bit=='4':
        bit='100'
    if bit=='5':
        bit='101'        
    if bit=='6':
        bit='110'
    if bit=='7':
        bit='111'        
    nbin=nbin+bit

print nbin