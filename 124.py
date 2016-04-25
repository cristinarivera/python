#Programa para calcular el valor del sumatorio desde n a m. Hace el cálculo desde n a m-1 ambos incluidos.

n=int(raw_input('Dame valor de n: '))
m=int(raw_input('Dame valor de m: '))
      
sumatorio=0

for i in range(n,m):
    sumatorio+=i**2
    
print sumatorio