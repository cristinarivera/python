#Programa para realizar operaciones básicas con vectores. 
#Cada vez que se ejecute el programa hay que introducir los vectores seleccionando las opciones 1 y 2.
#Después ya podemos elegir la opción de la operación que deseamos conocer.

from math import acos
from math import sqrt
from math import pi

opcion=''
while opcion!='9':
     print '1) Introducir el primer vector.'
     print '2) Introducir el segundo vector.'
     print '3) Calcular la suma.'
     print '4) Calcular la diferencia.'
     print '5) Calcular el producto escalar.'
     print '6) Calcular el producto vectorial.'     
     print '7) Calcular el ángulo (en grados) entre ellos.'
     print '8) Calcular la longitud.'
     print '9) Finalizar'
     opcion = raw_input('Escoge la opcion y pulsa el retorno del carro ')
     if opcion == '1': 
          x1=int(raw_input('x1: '))
          y1=int(raw_input('y1: '))
          z1=int(raw_input('z1: '))
     elif opcion == '2': 
          x2=int(raw_input('x2: '))
          y2=int(raw_input('y2: '))
          z2=int(raw_input('z2: '))
     elif opcion == '3': 
          suma=(x1+x2, y1+y2, z1+z2)
          print 'La suma de ambos vectores es ', suma
     elif opcion == '4': #Al seleccionar esta opción se elegirá entre la opción 1 y la opción 2, dependiendo de la resta que se pretenda averiguar.
          opcion_4=' '
          while opcion_4!='1' and opcion_4!='2':
               print '1) Vector v1 menos vector v2.'
               print '2) Vector v2 menos vector v1.'
               opcion_4=raw_input('Escoge una opcion: ')
               if opcion_4=='1':
                    resta_v1v2=(x1-x2, y1-y2, z1-z2)
                    print 'La resta del vector v1 menos el vector v2 es', resta_v1v2
               if opcion_4=='2':
                    resta_v2v1=(x2-x1, y2-y1, z2-z1)
                    print 'La resta del vector v2 menos el vector v1 es', resta_v2v1  
     elif opcion == '5': 
          p_escalar=x1*x2 + y1*y2 + z1*z2
          print 'El producto escalar de ambos vectores es', p_escalar
     elif opcion == '6': 
          p_vectorial=(y1*z2-z1*y2, z1*x2-x1*z2, x1*y2-y1*x2)
          print 'El producto vectorial de ambos vectores es', p_vectorial      
     elif opcion == '7': 
          angulo=(180/pi)*acos((x1*x2 + y1*y2 + z1*z2)/((sqrt(x1**2 + y1**2 + z1**2))*(sqrt(x2**2 + y2**2 + z2**2))))
          print 'El angulo entre ambos vectores es', angulo                
     elif opcion == '8': # En este caso introduciremos la opción 8 y a continuación el vector del que deseamos conocer la longitud.
          opcion_8=' '          
          while opcion_8!='v1' and opcion_8!='v2':
               opcion_8=raw_input('Para que vector, escribe v1 o v2: ')
               if opcion_8=='v1':
                    longitud_v1=sqrt(x1**2 + y1**2 + z1**2)
                    print 'La longitud del vector v1 es', longitud_v1      
               if opcion_8=='v2':
                    longitud_v2=sqrt(x2**2 + y2**2 + z2**2)
                    print 'La longitud del  vector v2 es', longitud_v2                 
     elif opcion!='9':
          print 'Solo hay nueve opciones: 1, 2, 3, 4, 5, 6, 7, 8 o 9. Tu has tecleado', opcion
print 'Gracias por usar este programa'