binario1=raw_input('Primer numero binario:')
binario2=raw_input('Segundo numero binario:')

b1=len(binario1)
b2=len(binario2)

sumabit=int(binario1[-1])+int(binario2[-1])
if sumabit==2:
    sumabit=1
    acarreo=1
else:
    acarreo=0
print sumabit
print acarreo
