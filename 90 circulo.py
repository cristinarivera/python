from math import pi

radio = float(raw_input('Dame el radio de un circulo: '))

print 'Escoge una opcion'
print 'a) Calcular el diametro.'
print 'b) Calcular el perimetro.'
print 'c) Calcular el area.'
opcion = raw_input('Teclea a, b o c y pulsa el retorno del carro')

if opcion == 'a' or opcion=='A': # Calculo del diametro.
    diametro = 2 * radio
    print 'El diametro es', diametro
else:
    if opcion == 'b' or opcion=='B': # Calculo del perimetro.
        perimetro = 2 * pi * radio
        print 'El perimetro es', perimetro
    else:
        if opcion == 'c' or opcion=='C': # Calculo del area.
            area = pi * radio ** 2
            print 'El area es', area
        else:
            print 'Solo hay tres opciones: a, b o c.'
            print 'Tu has tecleado', opcion