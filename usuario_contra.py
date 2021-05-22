'''Escribir un programa que almacene la cadena de caracteres usuario y contraseña, y
pregunte al usuario por su usuario y contraseña hasta que introduzca el usuario y la contraseña correcta.
y que muestre primer intento error, segundo intento error y Agotado'''
print("'BIENVENIDO A SU BANCA ELECTRONICA DEL BANCO PICHINCHA'")
i = 0
while i<3:
    usuario = input('Ingrese su Nombre de Usuario: ')
    i=i +1
    if str(usuario)=='Leodangarcia':
        clave = input('Ingrese su Clave: ')
        if str(clave)=='python2021':
            print('Bienvenido Leodan a La Banca Electronica')
            break
        else:
            print('Clave Incorrecta')
            if i==1:
                print('Primer Intento Erroneo')
            elif i==2:
                print('Segundo Intento Erroneo')
            elif i==3:
                print('Intentos Agotados')
                break
    else:
        print('Usuario Incorrecto')
        if i==1:
            print('Primer Intento Erroneo')
        elif i==2:
            print('Segundo Intento Erroneo')
        elif i==3:
            print('Intentos Agotados')


    
    


