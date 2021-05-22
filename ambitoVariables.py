num=2 #Global

def sumar():
    a=2 #Locales
    b=3
    suma=a+b
    return suma

suma=sumar()
print(suma)
a='Diego'
print(a)
if False:
    num1=20 #Local
    print('Dentro del if')
    print(num)
    print(num1)

print('Fuera')
print(num)
#print(num1)