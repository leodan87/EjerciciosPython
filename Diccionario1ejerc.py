'''Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''
moneda = {'Euro':'€','Dollar':'$','Yen':'¥'}
divisa = input('Digite el Tipo de divisa: ')
print('',moneda.get(divisa,'No existe esa Divisa en el Diccionario'))