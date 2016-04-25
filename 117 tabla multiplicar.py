# Programa para escribir la tabla de multiplicar de un número.

numero=int(raw_input('Dame un numero: '))

for tabla in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print '%d x %2d = %2d' % (numero, tabla, numero*tabla)