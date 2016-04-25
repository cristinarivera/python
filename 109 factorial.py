#Programa para calcular n factorial.

n=int(raw_input('Dame valor de n para calcular n!: '))

fac=1
i=1
while i<=n:
    fac=fac*(i)
    i=i+1
   
print fac