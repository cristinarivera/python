# Programa para calcular las palabras de una frase introducida por el usuario.
# El programa finaliza cuando damos a intro sin escribir ninguna frase.
cadena=raw_input('Escribe una frase: ')
while cadena!='':
    cambios = 0
    posterior = ' '
    for caracter in cadena:
        if caracter == ' ' and posterior != ' ':
            cambios+=1
        posterior = caracter
        
    if cadena[-1] == ' ':
        cambios=cambios - 1
        
    palabras = cambios +1 
    print 'Palabras:', palabras
    
    cadena=raw_input('Escribe una frase: ')