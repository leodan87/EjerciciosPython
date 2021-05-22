'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa 
donde <mes> es el nombre del mes.
'''
meses={'01':'Enero', '02':'Febrero','03':'Marzo',
    '04':'Abril', '05':'Mayo','06':'Junio',
    '07':'Julio', '08':'Agosto','09':'Septiembre',
    '10':'Octubre', '11':'Noviembre','12':'Diciembre'}
fecha=input('Fecha (dd-mm-aaaa): ')
flista = fecha.split('-')
print(flista)
print('{0} de {1} de {2} donde {1} es el nombre de mes'.format(
        flista[0], meses[flista[1]], flista[2]
    )
)