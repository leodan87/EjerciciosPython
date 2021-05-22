'''Hacer un programa que pida 2 numeros y se de cuenta cual de ellos
es par, o si ambos lo son'''
num1 = int(input('Digite el primer numero :'))
num2 = int(input('Digite el segundo numero :'))
if num1%2==0 and num2%2==0:
    print('Ambos numeros son pares')
elif num1%2==0 and num2%2!=0:
    print(num1,'Es par')
elif num1%2!=0 and num2%2==0:
    print(num2,'Es par')
else:
    print('Ambos numeros son impares')
    
