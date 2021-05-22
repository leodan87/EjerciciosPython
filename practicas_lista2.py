'''Escriba un programa que permita crear una lista de palabras y que
a continuacion,pida una palabra y diga cuantas veces aparece esa
palabra en la lista.'''
numero = int(input('Digite cuantas Palabras tiene la Lista: '))
if numero < 1:
    print('Imposible!')
else:
    lista = []
    for i in range(numero):
        print('Digame la Palabra',str(i+1)+': ',end='')
        palabra = input()
        lista += [palabra]
    print('La lista creada es: ',lista)
buscar = input('Digame la palabra a buscar: ')
contador = 0
for i in lista:
    if i == buscar:
        contador += 1;
if contador == 0:
    print('La Palabra' ,buscar, 'no aparece en la lista')
elif contador == 1:
    print('La Palabra' ,buscar, 'aparece una vez en la lista')
else:
    print('La Palabra' ,buscar, 'aparece' ,contador, 'veces en la lista')