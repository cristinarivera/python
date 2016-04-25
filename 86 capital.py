from math import log
print 'Programa para el calculo de años para obtener un capital final a partir del inicial'
cap_ini=float(raw_input('Indica capital inicial: '))
cap_fin=float(raw_input('Indica capital final: '))
tasa=float(raw_input('Dame tasa de interes: '))

anos=(log(cap_fin)-log(cap_ini)) / log(1+tasa/100)
print str(anos) + ' anyos'