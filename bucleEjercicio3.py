#Escribir un programa que pida al usuario un número entero positivo y 
#muestre por pantalla todos los números impares desde 1 hasta ese 
#número separados por comas.
#10 -> 1,3,5,7,9
#5 -> 1,3,5
num=int(input('Ingrese un número: '))
if num>0: #Si es positivo
    cont=1
    res=''
    while cont<=num:
        res+=str(cont)+','
        cont+=2
    print(res[0:len(res)-1])
else: #Si son negativos
    print('Error, debe ingresar un número positivo.')