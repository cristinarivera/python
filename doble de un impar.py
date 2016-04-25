m = int(raw_input ('Dame un numero: '))

n=m/2
if m%n==0:
    if n%2.0==0:
        print str(m) + ' no es el doble de ningun impar ' 
    else:
        print str(m) + ' es el doble del impar ' + str(n)