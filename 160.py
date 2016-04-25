a=raw_input('Dame una cadena: ')
mayuscula=0
for i in range(len(a)):
    if a[i]>='A' and a[i]<='Z':
        mayuscula+=1
print mayuscula
