from math import pi

opcion=''
while opcion!='d':
     radio = float(raw_input('Dame el radio de un circulo: '))
     print 'Escoge una opcion:'
     print 'a) Calcular el diametro.'
     print 'b) Calcular el perimetro.'
     print 'c) Calcular el area.'
     print 'd) Finalizar'
     opcion = raw_input('Teclea a, b o c y pulsa el retorno del carro')
     if opcion == 'a': # Calculo del diametro.
          diametro = 2 * radio
          print 'El diametro es', diametro
     elif opcion == 'b': # Calculo del perimetro.
          perimetro = 2 * pi * radio
          print 'El perimetro es', perimetro
     elif opcion == 'c': # Calculo del area.
          area = pi * radio ** 2
          print 'El area es', area
     elif opcion!='d':
          print 'Solo hay cuatro opciones: a, b o c. Tu has tecleado', opcion
print 'Gracias por usar el programa'