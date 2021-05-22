'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad)'''
edad = int(input('Ingrese su Edad: '))
cont = 1
while cont <= edad:
    print('Usted cumplio' ,cont,'años de Edad')
    cont+=1

