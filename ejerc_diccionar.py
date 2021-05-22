'''Escribir un programa que cree un diccionario vacío y lo vaya llenando con informacion
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido
del diccionario.'''
datPersonales = {}
nombre2 = 'nombre'
nombre1 = input('Digite su nombre: ')
datPersonales[nombre2]=nombre1
print(datPersonales)
edad2 = 'edad'
edad1 = int(input('Digita su Edad: '))
datPersonales[edad2]=edad1
print(datPersonales)
sexo2 = 'sexo'
sexo1 = input('Digita tu sexo: ')
datPersonales[sexo2]=sexo1
print(datPersonales)
telefono2 = 'telefono'
telefono1 = int(input('Digita tu Nro de telefono: '))
datPersonales[telefono2]=telefono1
print(datPersonales)
email2 = 'email'
email1 = input('Digita tu correo electronico: ')
datPersonales[email2]=email1
print(datPersonales)