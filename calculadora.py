'''Construir un programa que simule el funcionamiento de una calculadora que puede realizar
las cuatro operaciones aritmeticas basicas (suma,resta,multiplicacion y division).El usuario debe especificar
la operacion con el primer caracter del nombre de la operacion.'''
num1 = float(input('Digite un numero: '))
num2 = float(input('Digite un numero: '))

operacion = input('Digite el caracter de la operacion que desea realizar: ')
operacion = operacion.upper()
if operacion=='S':
    suma = num1+num2
    print('La suma es ',suma)
elif operacion=='R':
    resta = num1-num2
    print('La resta es ',resta)
elif operacion=='M':
    mult = num1*num2
    print('La multiplicacion es ',mult)
elif operacion=='D':
    div = num1/num2
    print('La Division es ',div)
else:
    print('Se equivoco de operacion')

