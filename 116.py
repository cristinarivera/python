from math import acos
from math import sqrt
from math import pi

x1=1
x2=4

y1=2
y2=5

z1=3
z2=6

#angulo=(180/pi)*acos((x1*x2 + y1*y2 + z1*z2)/sqrt(x1**x1 + y1**y1 + z1**z1)*sqrt(x2**x2 + y2**y2 + z2**z2))

angulo=(x1*x2 + y1*y2 + z1*z2)/((sqrt(x1**2 + y1**2 + z1**2))*(sqrt(x2**2 + y2**2 + z2**2)))


print  angulo    

#longitud=sqrt(x1**x1 + y1**y1 + z1**z1)
#print longitud      