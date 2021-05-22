'''Hacer un programa pra sumar numeros pares
dentro de un rango,ejemplo:
suma de numeros pares del 2 al 30
suma = 240'''
a = int(input('Digite desde donde quiere comenzar a sumar: '))
b = int(input('Digite hasta donde quiere llegar a sumar: '))
suma = 0
for i in range(a,b+1):
    if i%2==0:
        suma +=i
print(f'La suma de numeros pares dentro del rango es: {suma}')