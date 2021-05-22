'''hacer un programa para detectar si una frase introducida
por el usuario finaliza con punto '.' o no. Deberas imprimir
por la consola una de las siguientes opciones:Termina con
punto o por el contrario no termina con punto.'''
frase = input('Digita la frase: ')
if frase.endswith('.'):
    print('Termina con punto')
else:
    print('No termina con punto')
