print 'MAXIMO COMUN DIVISOR'

a = int(raw_input('ingrese primer nro: '))
b = int(raw_input('ingrese segundo nro: '))
c = int(raw_input('ingrese tercer nro: '))

mcd = 0

if c < a > b:
  if b < c:
    for i in range(1, b+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    print 'mcd:', mcd
  elif c < b:
    for i in range(1, c+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
      print 'mcd:', mcd

if c < b > a:
  if a < c:
    for i in range(1, a+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    print 'mcd:', mcd
  elif c < a:
    for i in range(1, c+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
      print 'mcd:', mcd


if b < c > a:
  if a < b:
    for i in range(1, a+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    print 'mcd:', mcd
  elif b < a:
    for i in range(1, b+1):
      if a % i ==0 and b % i ==0 and c % i ==0:
        mcd = i
    print 'mcd:', mcd