'''Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectangulo como el de mas abajo
1 
3 1
5 3 1 
7 5 3 1
9 7 5 3 1'''
num = int(input('Digite un numero: '))
for i in range(1, num+1, 2):#Si Empieza en 1 numeros Impares
    for j in range(i, 0, -2):
        print(j, end=' ')
    print(' ')
num = int(input('Digite un numero: '))
for i in range(0, num+1, 2):#Si empieza en 0 numeros Pares
    for j in range(i, 0, -2):
        print(j, end= ' ')
    print(' ')

