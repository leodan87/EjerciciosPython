import os
#os.mkdir('carpeta1')#Crea Carpetas

#os.rmdir('carpeta1')#Elimina Carpetas

#file = 'test.txt'
#f = open(file,'xt')#Creas el Archivo
#f.close()

file = 'test.txt'
f = open(file,'at')#Introduces Palabras al Archivo
f.write('\nEsta es otra cadena insertada')
f.close()

file = 'test.txt'
file = open(file,'rt')#Lees el Archivo
print(file.read())
file.close()

#file = 'test.txt'
#f = open(file,'wt')#Se Borra todo el Contenido
#f.close()