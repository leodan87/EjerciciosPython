'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
'''
suma=0
while True:
    num=int(input('Número: '))
    if num > 0: #Suma solo los positivos
        suma+=num

    if num==0:
        print('Suma total de positivos =', suma)
        break