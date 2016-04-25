print 'Programa para calcular ecuaciones de primer grado'

a= float(raw_input('Valor de a: '))
b= float(raw_input('Valor de b: '))

if a!=0:
    x=-b/a
    print 'Solucion: ', x
if a==0:
    if b!=0:
        print 'La ecuacion no tiene solucion.'
    if b==0:
        print 'La ecuacion tiene infinitas soluciones.'