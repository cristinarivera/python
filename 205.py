cadena=raw_input('Dame una cadena: ')

prefijo=0
final=prefijo + 3
while prefijo<1+len(cadena):
    print cadena[prefijo:final]
    prefijo+=1
    final+=1