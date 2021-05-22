#'x' * 'y' = 'x'*'y'

x=1
while x<=10: #Cuenta del 1 al 10
    print('Tabla del', x)
    y=1
    while y<=12: #Cuenta del 1 al 12        
        print('{} x {} = {}'.format(x, y, x*y))
        y+=1
    print('--------------')    
    x+=1