'''Realizar un juego para adivinar un numero.Para ello generar
un numero aleatorio entre 0-100, y luego ir pidiendo numeros
indicando 'es mayor'o'es menor'segun sea mayor o menor con
respecto a N. El proceso termina cuando el usuario acierta y
mostrar el numero de intentos.'''

import random

aleatorio = random.randint(0,100)# Generamos un numero aleatorio
print('\nJuego Adivina el Numero: ')
contador = 0
while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero>aleatorio:
        print('\tNo es el Numero, digita un numero MENOR:')
    elif numero<aleatorio:
        print('\tNo es el Numero, digita un numero MAYOR')
    else:
        print(f'Felicidades,acabas de adivinar el numero {aleatorio}')
        break
print(f'Numero de Intentos: {contador}')



