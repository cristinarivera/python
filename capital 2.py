print 'Programa para el calculo del capital'
euros=float(raw_input('Cantidad de capital en euros: '))
tasa=float(raw_input('Que tasa de interes: '))
anos=float(raw_input('Dame anos: '))

capital=round((euros*(1+(tasa/100))**anos),2)
if tasa>=0:
    print str(capital) + u' euros'