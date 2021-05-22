'''Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.'''
num1 = 0
suma = 0
num = int(input('Digita un numero entero positivo: '))
while num != 0:
    num1 = num % 10
    num //= 10
    suma += num1
    print('La suma de los dígitos es: ',suma)