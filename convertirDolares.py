'''
Escribir un programa que pregunte por consola el precio de un producto 
en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.
'''
#2.34, 1.50, 10.75
precio = input('Ingrese precio: $')
preLista = precio.split('.')
print(preLista[0],'dólar(es) con',preLista[1],'centavos')
#2 dólar(es) con 34 centavos, 
#1 dólar(es) con 50 centavos, 
#10 dólar(es) con 75 centavos 