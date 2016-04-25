#Programa que nos dice si una letra es mayuscula o minuscula.

letra= raw_input('Dame un caracter: ')


if letra>='a':
    if letra=='a' or (letra=='e' or (letra=='i' or (letra=='o' or letra=='u'))):
        print 'Es vocal minuscula'    
    else:
        if letra<='z':
            print 'Es minuscula'
if letra>='A':
    if letra=='A' or (letra=='E' or (letra=='I' or (letra=='O' or letra=='U'))):
        print 'Es vocal mayuscula'    
    else:
        if letra<='Z':
            print 'Es mayuscula'
else:
    print 'Es otro tipo de caracter'
        