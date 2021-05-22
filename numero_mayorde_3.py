#Hacer un programa que pide 3 numeros y determine cual es el mayor
num1 = int(input('Digite un numero :'))
num2 = int(input('Digite un numero :'))
num3 = int(input('Digite un numero :'))
if num1>=num2 and num1>=num3:
    print("El Numero mayor es :",num1)
elif num2>=num1 and num2>=num3:
    print('El Numero mayor es :',num2)
elif num3>=num1 and num3>=num2:
    print('El Numero numero mayor es :',num3)