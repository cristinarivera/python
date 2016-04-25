
print 'Programa para el calculo del capital'
euros=float(raw_input('Dame euros: '))
tasa=float(raw_input('Dame tasa de interes: '))
anos=float(raw_input('Dame anos: '))

capital=round((euros*(1+(tasa/100))**anos),2)

print str(capital) + u' euros'