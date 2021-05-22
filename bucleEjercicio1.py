#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra=input('Ingrese una palabra: ')
cont=1
'''
while cont <= 10:
    print('{0}. {1}'.format(cont, palabra))
    cont+=1 #Sumar 1 al contador
'''

while True:
    print('{0}. {1}'.format(cont, palabra))
    if cont==10:
        break
    cont+=1 #Sumar 1 al contador