print 'Programa para indicar la calificación cualitativa'

calific=float(raw_input('Indica la calificacion numerica: '))

if calific<5.0:
    print 'Suspenso'
if calific>=5 and calific<7:
    print 'Aprobado'
if calific>=7 and calific<8.5:
    print 'Notable'
if calific>=8.5 and calific<10:
    print 'Sobresaliente'
if calific==10:
    print 'Matricula de honor'