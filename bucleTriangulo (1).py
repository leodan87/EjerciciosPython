#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo,
# de altura el número introducido.

'''
*
**
***
****
*****
******
*******
'''
num=int(input('Ingrese un número: '))
cont1,cont2=1,1
while cont1<=num:
    while cont2<=cont1:
        print('*', end=' ')
        cont2+=1
    print() #Hacemos un salto de línea
    cont2=1 #Reinicio el contador 2
    cont1+=1