#Programa para calcular el mcd de dos números enteros aplicando el algoritmo de euclides tradicional.
num_1=int(raw_input('Primer entero para calcular el mcd: '))
num_2=int(raw_input('Segundo entero para calcular el mcd: '))
num_3=int(raw_input('Tercer entero para calcular el mcd: '))


if num_1==0:
    print 'El mcd es ', num_2
if num_2==0:
    print 'El mcd es ', num_1
while num_1!=0 and num_2!=0:
    q=num_1 / num_2
    r=num_1 % num_2
    num_1=num_2
    num_2=r

if num_1==0:
    print 'El mcd es: ', num_2
if num_2==0:
    print 'El mcd es: ', num_1    