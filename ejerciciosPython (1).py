#Escribir un programa que pida al usuario una palabra 
#y la muestre por pantalla 10 veces.

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input('Edad: '))
for i in range(1,edad+1):
    print(i)

pal=input('Palabra: ')
cont=1
while cont<=10:
    print(pal)
    cont+=1

for i in range(2,11,2):#lista[], tupla(), cadena"", diccionario{}, rango
    print(i)

'''
x=1
while x <= 10: #< > <= >= != ==
    print('Repetir',x)
    x += 1

while True:
    opcion=input('Desea continuar (si/no): ')
    if opcion=='no':
        print('Adiós')
        break

print('Estoy fuera del while')

#while y for

'''
