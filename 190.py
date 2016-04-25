palabra=raw_input('Dame una palabra:')

anterior="a"
for letra in palabra:
    if letra>=anterior:
        anterior=letra
        texto='La palabra es alfabetica.'
    else:
        texto='La palabra no es alfabetica.'
        
print texto