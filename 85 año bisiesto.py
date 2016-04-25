anyo=int(raw_input('Dame un anyo: '))

if anyo%4==0 and (anyo%100!=0 or anyo%400==0):
    print 'El anyo %d es bisiesto.' %anyo
else:
    print 'El anyo %d no es bisiesto.' %anyo