class Perro:
    def __init__(self, nombre, raza, color, edad): #Contructor
        self.nombre=nombre
        self.raza=raza
        self.color=color
        self.edad=edad
    
    def ladrar(self):
        return "Ladrando"

    

class Estudiante:
    def __init__(self, cedula, nombres, notas):
        self.cedula=cedula
        self.nombres=nombres
        self.notas=notas

    def estaAprobado(self):
        suma=0
        for i in self.notas:
            suma+=i
        prom=suma/len(self.notas)
        if prom>=7:
            return True
        else:
            return False

    def __str__(self):
        return self.nombres

class Galleta:
    def __init__(self, sabor, forma, tamanio):
        self.sabor=sabor
        self.forma=forma
        self.tamanio=tamanio

    def __str__(self):
        return 'Galleta de ' + self.sabor

g1=Galleta('Chocolate', 'redonda', 'grande')
g2=Galleta('Vainilla', 'redonda', 'pequeña')
g3=Galleta('Fresa', 'cuadrada', 'grande')
g4=Galleta('Frutilla', 'triangural', 'extragrande')
print(g3)


p1=Perro('Peluchin','Labrador','negro',2) #Crear un objeto
print(p1.nombre)
print(p1.ladrar())

p2=Perro('Cocki','Labrador','blanco y negro',1)


e1=Estudiante('1900787910', 'Diego Cuenca', [4.3, 5.7, 9.9, 10, 8.9])
e2=Estudiante('0706829504', 'Juan Loja', [4.3, 5.7, 4.9, 5, 1.9])
print(e1)
print(e1.estaAprobado())
print(e2.estaAprobado())