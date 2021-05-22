'''hacer un programa donde se debera imprimir por la consola la palabra con mas caracteres
de dos palabras dadas en el caso de que ambas palabras tengan la misma cantidad de caracteres
deberas mostrar el mensaje son iguales'''
pal1 = input('Digite la palabra: ')
pal2 = input('Digite la otra palabra: ')
if len(pal1) > len(pal2):
    print(f'\nTiene mas caracteres: {pal1}')
elif len(pal2)> len(pal1):
    print(f'\nTiene mas caracteres: {pal2}')
else:
    print('Son iguales en longitud')