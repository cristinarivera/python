num=int(raw_input('Numero para averiguar si es primo: '))

creo_que_es_primo=True
divisor=2
while divisor<num and creo_que_es_primo:
    if num%divisor==0:
        creo_que_es_primo=False
    divisor +=1    
        
if creo_que_es_primo:
    print 'El numero' , num, 'es primo'
else:
    print 'El numero' , num, 'no es primo'