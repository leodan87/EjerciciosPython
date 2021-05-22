'''Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''
num = int(input('Ingrese un numero: '))
if num>0:
    cont=num
    res =''
    while cont>=0:
        res+=str(cont)+','
        cont-=1
    print(res[0:len(res)-1])

else:
    print('Error, Ingresa un numero entero Positivo')