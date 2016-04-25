#Programa para calcular el valor del sumatorio desde n a m siempre que sean pares. Hace el cálculo desde n a m-1 ambos incluidos.

n=int(raw_input('Dame valor de n: '))
m=int(raw_input('Dame valor de m: '))

if n%2==0:
    sumatorio=0
    for i in range(n,m+1,2):
        sumatorio+=i
    print sumatorio
else: 
    n+=1
    sumatorio=0
    for i in range(n,m+1,2):
        sumatorio+=i
    print sumatorio    
