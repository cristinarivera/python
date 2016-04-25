#Programa para calcular el numero de combinaciones que podemos formar tomando m elementos de un conjunto con n elementos.

print 'El valor de n debe ser mayor o igual que m.'
n=int(raw_input('Dame valor de n, elementos de un conjunto : '))
m=int(raw_input('Dame valor de m, elementos que tomamos de ese conjunto: '))

fac_n=1
i_n=1
while i_n<=n:
    fac_n=fac_n*(i_n)
    i_n=i_n+1
#print fac_n

fac_m=1
i_m=1
while i_m<=m:
    fac_m=fac_m*(i_m)
    i_m=i_m+1
#print fac_m

fac_nm=1
i_nm=1
while i_nm<=(n-m):
    fac_nm=fac_nm*(i_nm)
    i_nm=i_nm+1
#print fac_nm

combinaciones = fac_n/(fac_nm*fac_m)
print combinaciones