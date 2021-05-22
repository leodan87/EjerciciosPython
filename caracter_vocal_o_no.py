#Hacer un programa que pida un caracter e indique si es una vocal o no
letra = input('Digite un caracter: ').lower()
if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print('Es una Vocal')
else:
    print('No es una Vocal')
