'''Hacer un programa que determine si una palabra o frase
es palindroma. Una cadena palindroma se lee igual de izquierda
a derecha que de derecha a izquierda ejem: oso, reconocer
anita lava la tina'''
frase = input('Digite una cadena: ')
frase = frase.replace(' ','')#Quitamos los espacios en blanco

frase2 = frase[::-1]#Invertimos la cadena
print(f'La cadena invertida es: {frase2}')
if frase == frase2:
    print('Es una Palindroma')
else:
    print('No es Palindroma')

