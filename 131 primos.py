num=int(raw_input('Numero para averiguar si es primo: '))

creo_que_es_primo=True
for divisor in range (2,num):
    if num%divisor==0:
        creo_que_es_primo=False
        break
    
if creo_que_es_primo:
    print 'El numero' , num, 'es primo'
else:
    print 'El numero' , num, 'no es primo'