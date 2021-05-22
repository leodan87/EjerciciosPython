#Pregunta al usuario por un número hasta que introduce 0.
num=None
'''
while num!=0:
    print('No es 0, repito.')
    num=int(input('Ingresa un número: '))
print('Fin del bucle1')
'''
while True:
    num=int(input('Ingresa un número: '))
    if num==0:
        print('Ya es 0, detengo.')
        break
    print('No es 0, repito.')

print('Fin del bucle2')