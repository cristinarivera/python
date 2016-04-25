print 'MAXIMO COMUN DIVISOR'

a = int(raw_input('Primer entero para calcular el mcd: '))
b = int(raw_input('Segundo entero para calcular el mcd: '))
c = int(raw_input('Tercer entero para calcular el mcd: '))

mcd = 0

if c < a > b:
  if b < c:
    for i in range(1, b+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    
  elif c < b:
    for i in range(1, c+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
      

if c < b > a:
  if a < c:
    for i in range(1, a+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    
  elif c < a:
    for i in range(1, c+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
      


if b < c > a:
  if a < b:
    for i in range(1, a+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    
  elif b < a:
    for i in range(1, b+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
        
print 'mcd:', mcd