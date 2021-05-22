'''Hacer un programa donde el usuario ingrese una frase, se le
devolvera la misma frase pero sin espacios en blanco y ademas un
contador de cuantos caracteres tiene la frase (sin contar los 
espacos en blanco)'''
frase = input('Ingrese una frase: ')
frase2 = ''
for i in frase:
    if i!= ' ':
        frase2 += i

frase = frase2
print(f'\nfrase final: {frase}')
print(f'Numero de Caracteres: {len(frase)}')