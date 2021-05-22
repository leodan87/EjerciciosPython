'''Hacer un programa que simule un cajero automatico
con un saldo inicial de $1000 y tendra el siguiente 
menu de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta.
3. Mostrar dinero disponible.
4. Salir.'''
saldo = 1000
while True:
    print('\tMENU OPCIONES:')
    print('1. Ingresar Dinero en la Cuenta:')
    print('2. Retirar Dinero de la Cuenta: ')
    print('3. Mostrar Dinero Disponible: ')
    print('4. Salir: ')
    opcion = int(input('Digite una opcion de Menu: '))

    print()

    if opcion==1:
        extra = float(input('Cuanto Dinero desea Ingresar en la Cuenta: '))
        saldo += extra
        print('Dinero en la cuenta:$',saldo)
    elif opcion==2:
        retirar = float(input('Cuanto Dinero desea Retirar de la Cuenta: '))
        if retirar>saldo:
            print('No tiene esa Cantidad de Dinero: ')
        else:
            saldo -= retirar
            print('Dinero en la Cuenta: $',saldo)
    elif opcion==3:
        print('Dinero en la Cuenta: $',saldo)
    elif opcion==4:
        print('Gracias por Utilizar su cajero automatico')
        break
    else:
        print('Se a equivocado de opcion de menu')

    print()

