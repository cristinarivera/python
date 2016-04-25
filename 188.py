#Programa para pasar de decimal a octal.
dec=int(raw_input('Dame un numero: '))

octal=' ' 
while dec>0:
    resto=dec%8
    dec=dec/8
    octal=str(resto)+octal
print octal