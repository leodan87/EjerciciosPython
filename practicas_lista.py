'''Escriba un programa que permita crear una lista de palabras.
para ello el programa tiene que pedir un numero y luego solicitar 
ese numero de palabras para crear la lista.Por ultimo el programa
tiene que escribir la lista.'''
numero = int(input('Digame cuantas palabras tiene la lista: '))
if numero<1:
    print('Imposible!')
else:
    lista = []
    for i in range(numero):
        print('Digame la Palabra',str(i+1)+':',end=' ')
        palabra = input()
        lista += [palabra]
    print('La Lista creada es:',lista)


