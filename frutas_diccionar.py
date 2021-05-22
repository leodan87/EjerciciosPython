'''Escribir un programa que guarde en un diccionario los precios de las frutas
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre 
por pantalla el precio de ese número de kilos de fruta. Si la fruta no está 
en el diccionario debe mostrar un mensaje informando de ello.'''
precios = {'pera':1,'banano':0.50,'uva':1.25,'sandia':1.50,'melon':0.75}
fruta = input('Que fruta desea comprar: ')
if fruta not in precios:
    print('Informando de ello')
else:
    kilos = int(input('Cuantos kilos de fruta desea comprar: '))
    print('El Precio es de:$',kilos*precios[fruta])
