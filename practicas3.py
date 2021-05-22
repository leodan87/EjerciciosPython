# Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia
import math


radio = float(input('Digite el radio :'))

area = math.pi * radio**2
longitud = 2 * math.pi * radio
print('El valor del area es :',area)
print('El valor de la circunferencia es :',longitud)