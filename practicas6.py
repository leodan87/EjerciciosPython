#CONDICIONALES COMBINADOS
edad = int(input('Digite su edad :'))
if edad>0 and edad<100:
    print('Edad correta')
    if edad>=18:
        print('Es mayor de edad')
else:
    print('Edad incorrecta')