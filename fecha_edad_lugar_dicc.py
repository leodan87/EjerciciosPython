#Escribir un programa que pregunte al usuario su nombre, edad, dirección y 
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla 
#el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
# teléfono es <teléfono>.
nom=input('NOMBRE: ')
edad=int(input('EDAD: '))
dire=input('DIRECCIÓN: ')
tel=input('TELÉFONO: ')

datPer={'nombre':nom, 'edad':edad, 'direccion':dire, 'telefono':tel}

print(datPer)
print('{0} tiene {1} años, vive en {2} y su número de teléfono es {3}'.format(
    datPer['nombre'], datPer['edad'], datPer['direccion'], datPer['telefono']
    ))