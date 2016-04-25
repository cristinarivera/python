# Programa que nos dice cuántas palabras tienen una longitud de k caracteres.
cadena=raw_input('Escribe una frase: ')
num_k=int(raw_input('Numero de letras de las palabras buscadas: '))

while cadena!='':
    for i in range(0, len(cadena)):
        if cadena[i] == ' ' and cadena[i+num_k+1] == ' ':
            if (i+num_k+1)<len(cadena):
                palabra=cadena[i:i+num_k+1]
                print palabra
                
#            if cadena[i] == ' ' and cadena[i-1] != ' ':
  #          end_space=cadena[i]
    #    palabra=end_space-start_space-1
      #  if num_k == len(palabra):
        #    print palabra
       
#    if cadena[-1] == ' ':
  #      cambios=cambios - 1
        
    #palabras = cambios +1 
   # print 'Palabras:', palabras
