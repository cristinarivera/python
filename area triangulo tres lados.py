from math import sqrt

a=float(raw_input('Dame lado a: '))
b=float(raw_input('Dame lado b: '))
c=float(raw_input('Dame lado c: '))
s=(a+b+c)/2.
area=sqrt(s*(s-a)*(s-b)*(s-c))

print area