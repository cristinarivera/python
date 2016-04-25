#Programa para calcular el sumatorio de i desde i=n a m.

inicial=int(raw_input('Dame i inicial: '))
final=int(raw_input('Dame i final: '))

if inicial>final:
    print 'El valor inicial debe ser menor o igual que el final'

else:
    sumatorio=0
    while inicial<=final:
        sumatorio+=inicial
        inicial+=1
    print sumatorio