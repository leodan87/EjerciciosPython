'''
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
num=int(input('Ingrese un número: '))
cont1,cont2=1,1
while cont1<=num:
    auxCont1=cont1 #Add
    while cont2<=cont1:
        numImpar=auxCont1*2-1 #Add
        auxCont1-=1 #Add
        print(numImpar, end=' ')
        cont2+=1
    print() #Hacemos un salto de línea
    cont2=1 #Reinicio el contador 2
    cont1+=1