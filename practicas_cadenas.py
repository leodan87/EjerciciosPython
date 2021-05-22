'''Escriba un programa que permita crear una lista de palabras y que
a continuacion,pida una palabra y diga cuantas veces aparece esa
palabra en la lista.'''
nroPalabras = int(input('Digite cuantas palabras tiene la lista: '))
if nroPalabras >0:
    lista = list()
    cont = 1
    while cont <= nroPalabras:
        pal = input('Digame la Palabra {}:'.format(cont))
        lista.append(pal)
        cont +=1
    print('La lista creada es: ',lista)
else:
    print('Imposible!')
buscar = input('Digame la Palabra a buscar: ')
contador = 0
for i in lista:
    if i == buscar:
        contador +=1
if contador == 0:
    print('La Palabra {} no aparece en la lista '.format(buscar))
elif contador == 1:
    print('La Palabra {} aparece una sola vez en la lista '.format(buscar))
else:
    print('La Palabra {} aparece {} veces en la lista '.format(buscar,contador))