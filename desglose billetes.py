print 'Programa para el desglose de cantidad de euros'
#Programa para calcular el desglose de una cantidad de dinero en billetes de euros
euros=float(raw_input('Cantidad de euros: ')) #Solicitud de la cantidad a calcular

#Cálculo de las cantidades de cada uno de los billetes:
quin=int(euros/500)
dosc=int((euros%500)/200)
cien=int((euros-quin*500-dosc*200)/100)
cincu=int((euros-quin*500-dosc*200-cien*100)/50)
veint=int((euros-quin*500-dosc*200-cien*100-cincu*50)/20)
diez=int((euros-quin*500-dosc*200-cien*100-cincu*50-veint*20)/10)
cinco=int((euros-quin*500-dosc*200-cien*100-cincu*50-veint*20-diez*10)/5)
dos=int((euros-quin*500-dosc*200-cien*100-cincu*50-veint*20-diez*10-cinco*5)/2)
un=int((euros-quin*500-dosc*200-cien*100-cincu*50-veint*20-diez*10-cinco*5-dos*2)/1)

if  quin>1:
    print str(quin) +  ' billetes de 500 euros'
if quin==1:
    print str(quin) +  ' billete de 500 euros'

if  dosc>1:
    print str(dosc) +  ' billetes de 200 euros'
if dosc==1:
    print str(dosc) +  ' billete de 200 euros'

if  cien>1:
    print str(cien) +  ' billetes de 100 euros'
if cien==1:
    print str(cien) +  ' billete de 100 euros'

if cincu>1:
    print str(cincu) +  ' billetes de 50 euros'
if cincu==1:
    print str(cincu) +  ' billete de 50 euros'

if  veint>1:
    print str(veint) +  ' billetes de 20 euros'
if veint==1:
    print str(veint) +  ' billete de 20 euros'

if diez>1:
    print str(diez) +  ' billetes de 10 euros'
if diez==1:
    print str(diez) +  ' billete de 10 euros'

if cinco>1:
    print str(cinco) +  ' billetes de 5 euros'
if cinco==1:
    print str(cinco) +  ' billete de 5 euros'

if dos>1:
    print str(dos) +  ' monedas de 2 euros'
if dos==1:
    print str(dos) +  ' moneda de 2 euros'

if un>1:
    print str(un) +  ' monedas de 1 euros'
if un==1:
    print str(un) +  ' moneda de 1 euros'
