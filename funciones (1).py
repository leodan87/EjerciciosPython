def saludar():
    print('Hola mundo, soy una función.')

def saludar2():
    return 'Hola, soy un valor retornado.'

def sumar(num1, num2):
    suma = num1 + num2
    return suma

def mensaje(texto):
    return 'Mi mensaje es: ' + texto

def calcular_area(base, altura):
    return base * altura / 2

print(calcular_area(23, 4.3))

#saludar()
#print(saludar2())
#print(sumar(2, 3))
#print(sumar(200, 344))
print(mensaje('¿Hola cómo estás?'))