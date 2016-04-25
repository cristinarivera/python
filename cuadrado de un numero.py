m = int(raw_input ('Dame un numero: '))
n = int(raw_input ('Dame otro numero: '))

if m**2==n:
    print 'El segundo es el cuadrado exacto del primero.'
if m**2>n:
    print 'El segundo es menor que el cuadrado del primero.'
if m**2<n:
    print 'El segundo es mayor que el cuadrado del primero.'