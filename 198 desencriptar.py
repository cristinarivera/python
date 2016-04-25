cadena=raw_input('Dame una cadena para descodificar: ')
n=int(raw_input('Dame el valor de n: '))

nuevapalabra=''
for caracter in cadena:
    numcar=ord(caracter)    
    if numcar >=65 and numcar<=90:
        codifnum=numcar-n
        if codifnum<65 or codifnum>90:
            codifnum=26+codifnum
    if numcar >=97 and numcar<=122:
        codifnum=numcar-n
        if codifnum<97 or codifnum>122:
            codifnum=26+codifnum    
    if numcar >=48 and numcar<=57:
        codifnum=numcar-n
        if codifnum<48 or codifnum>57:
            codifnum=10+codifnum    
    nuevocaracter=chr(codifnum)
    nuevapalabra=nuevapalabra+nuevocaracter
    
print nuevapalabra