#suma de binarios. primero pasamos los numeros binarios a decimal. hacemos la suma y pasamos la suma a binario.

binario1=raw_input('Primer numero binario:')
binario2=raw_input('Segundo numero binario:')

valor1=0
for bit in binario1:
    valor1+=valor1+int(bit)
    
valor2=0
for bit in binario2:
    valor2+=valor2+int(bit)
    
suma=valor1+valor2

sumabin=' ' 
while suma>0:
    resto=suma%2
    suma=suma/2
    sumabin=str(resto)+sumabin
print sumabin