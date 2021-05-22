import wikipedia
wikipedia.set_lang('es')

busqueda=input('Buscar en Wikiedia: ')
parrafos=int(input('Nro. de párrafos: '))
print('### RESULTADO ###')
try:
    resultado = wikipedia.summary(busqueda, sentences=parrafos)
    print(resultado)
except:
    print('Hubo un problema.')