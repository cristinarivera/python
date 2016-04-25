cadena=raw_input('Dame una cadena para codificar: ')
n=raw_input('Dame el valor de n: ')

nuevapalabra=''
for caracter in cadena:
    nuevocaracter=chr(ord(caracter)+2)
    if nuevocaracter=='[':
        nuevocaracter='A'
    if nuevocaracter=='\\':
        nuevocaracter='B'        
    if nuevocaracter=='{':
        nuevocaracter='a'        
    if nuevocaracter=='|':
        nuevocaracter='b'        
    if nuevocaracter==':':
        nuevocaracter='0'
    if nuevocaracter==';':
        nuevocaracter='1'

    nuevapalabra=nuevapalabra+nuevocaracter
    
print nuevapalabra