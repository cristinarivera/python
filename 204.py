cadena=raw_input('Dame una cadena: ')

prefijo=1
while prefijo<1+len(cadena):
    print cadena[:prefijo]
    prefijo+=1