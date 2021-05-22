'''Escribir un programa que pregunte al usuario por una frase
y una letra y muestre por pantalla el numero de veces que aparece 
la letra en la frase'''
frase = input('Digite la Frase: ')
letra = input('Digite la letra: ')
cont = 0
for i in frase:
    if i == letra:
        cont += 1
print('La letra',letra,'aparece',cont,'veces')