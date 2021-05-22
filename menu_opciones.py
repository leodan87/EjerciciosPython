'''Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.'''
print('\t MENU OPCIONES')
print('1. Comenzar Programa')
print('2. Imprimir Saldo')
print('3. Finalizar Programa')
while True:
    opcion = int(input('Digite una opcion de menu: '))
    print()
    if opcion ==1:
        print('Comenzando el Programa')
    elif opcion ==2:
        print('Imprimiendo el Saldo