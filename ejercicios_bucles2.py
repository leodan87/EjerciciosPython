'''Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.'''
suma = []
while True:
    num = int(input('Digite el numero: '))
    suma.append(num)
    if num==0:
        print('La suma Total de los numeros es:',sum(suma))
        break