'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números ingresados.
'''
suma=0
while True:
    num=int(input('Número: '))
    suma+=num
    if num==0:
        print('Suma total =', suma)
        break

val=[]
while True:
    num=int(input('Número: '))
    val.append(num)
    if num==0:
        print('Suma total =', sum(val))
        break