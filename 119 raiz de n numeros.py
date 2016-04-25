numero=float(raw_input('Dame un numero: '))

for n in range(2,101):
    print 'la raiz %d-esima de %3.0f es %f' % (numero, n, numero**(1.0/n))