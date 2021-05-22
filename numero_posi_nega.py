'''Escriba un programa que pida primero un número par (positivo o negativo)
 y si el valor no es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo)
 y si el valor no es correcto, mostrará un aviso.'''
print('PAR E IMPAR')
numero = int(input('Digite un numero Par: '))
if numero%2==0:
    numero2 = int(input('Digite un numero Impar: '))
    if numero2%2!=0:
        print('Gracias por su colaboracion')
    else:
        print('No es un numero Impar')
        print('Ejecute de nuevo el Programa para volver a intentarlo')
else:
    print('No es un numero Par')
    print('Ejecute de nuevo el programa para volver a intentarlo')

