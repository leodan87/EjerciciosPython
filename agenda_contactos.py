'''Hacer un programa que simule una agenda de contactos.Crear un
diccionario donde la clave sea el nombre del usuario y el valor sea
el telefono, el programa tendra el siguiente menu de opciones:
1.Nuevo contacto
2.Borrar contacto
3.Ver contactos existentes
4.Salir
'''
agenda = {}
while True:
    print('\tMENU DE OPCIONES')
    print('1.Nuevo contacto')
    print('2.Borrar contacto')
    print('3.Ver contactos existentes')
    print('4.Salir')
    opcion = int(input('Digite una opcion de menu: '))

    print()

    if opcion == 1:
        nombre = input('Nombre del contacto: ')
        telefono = input('numero de telefono: ')

        if nombre not in agenda:
            agenda[nombre]= telefono
            print('Contacto agregado')
        else:
            print('Ese nombre de Contacto ya Existe')

    elif opcion == 2:
        nombre = input('Nombre del Contacto: ')

        if nombre in agenda:
            del(agenda[nombre])
            print('Contacto Eliminado')
        else:
            print('Ese Contacto ya Existe')

    elif opcion == 3:
        print('Agenda de contactos: ')
        for clave,valor in agenda.items():
            print(f'Nombre: {clave},Telefono: {valor}')

        
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contacto')
        break
    else:
        print('Se equivoco de opcion de menu')



