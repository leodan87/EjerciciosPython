'''
Escribir un programa que pida al usuario que introduzca una frase 
en la consola y una vocal, y después muestre por pantalla la misma
frase pero con la vocal introducida en mayúscula.
'''
#Hola mundo como estas
#o
#HOla mundO cOmO estas
frase = input('Ingrese frase: ')
vocal = input('Ingrese vocal: ')
res = frase.replace(vocal, vocal.upper())
print(res)