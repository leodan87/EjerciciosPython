'''Hacer un  programa donde se reemplacen todos los espacios de una cadena
por asteriscos y ademas cada palabra comienze con mayusculas.'''
cadena = input('Digita una cadena: ')
cadena = cadena.replace(' ','*')
print(cadena.title())