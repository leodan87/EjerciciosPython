'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no y en la 
funcion de su respuesta le muestre un menu con los ingredientes disponibles para que elija.
solo se puede elejir un ingrediente ademas de la mozzarella y el tomate que estan en todas las pizzas
al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''
print("'BIENVENIDOS A LA PIZZERIA LUCIA GARCIA'")
tipo = input('Introduce el Numero a la Clase de Pizza que Desea: \n1.Pizza Vegetariana: 2.Pizza No Vegetariana: ')
if tipo == '1':
    print('Pizza Vegetariana\n\t1-Pimiento\n\t2-Tofu\n')
    ingrediente = input('Introduce el Ingrediente que Deseas: ')
    print('Pizza Vegetariana con Mozzarella y Queso')
    if ingrediente =='1':
        print('Pimiento')
    else:
        print('Tofu')
else:
    print('Pizza No Vegetariana\n\t1-Peperoni\n\t2-Jamon\n\t3-Salmon\n')
    ingrediente = input('Introduce el Ingrediente que Deseas: ')
    print('Pizza No Vegetariana con Mozzarella y Queso')
    if ingrediente == '1':
        print('Peperoni')
    elif ingrediente == '2':
        print('Jamon')
    else:
        print('Salmon')



