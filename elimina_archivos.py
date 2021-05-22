import os
if os.path.exists('test.txt'):
    os.remove('test.txt')
    print('El archivo ha sido eliminado')
else:
    print('Archivo no encontrado')