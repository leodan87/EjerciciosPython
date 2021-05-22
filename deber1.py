'''Escriba un programa que pida el año actual y un año cualquiera 
y que escriba cuántos años han pasado desde ese año 
o cuántos años faltan para llegar a ese año'''
fechaActual = int(input('Digite un año actual: '))
fechaPasada = int(input('Digite un año cualquiera: '))
if fechaActual>fechaPasada:
    print('')
else:
    print('Ambos son el mismo Año')

