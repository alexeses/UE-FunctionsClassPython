class Poligono():
    def __init__(self, num_lados):
        self.num_lados = num_lados
        self.lados = [0] * num_lados

    def darlados(self):
        for i in range(self.num_lados):
            self.lados[i] = int(input("Introduce el lado " + str(i + 1) + ": "))

    def verlados(self):
        for i in range(self.num_lados):
            print("Lado " + str(i + 1) + ": " + str(self.lados[i]))

class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)

    def area(self):
        # Calcular semiperímetro
        s = sum(self.lados) / 2
        # Calcular área utilizando fórmula de Herón
        area = (s * (s - self.lados[0]) * (s - self.lados[1]) * (s - self.lados[2])) ** 0.5
        print("El área del triángulo es:", area)

    def perimetro(self):
        perimetro = sum(self.lados)
        print("El perímetro del triángulo es:", perimetro)

# Crear dos objetos de la clase Triangulo
triangulo1 = Triangulo()
triangulo2 = Triangulo()

# Asignar lados al primer triangulo
triangulo1.darlados()

# Mostrar lados del primer triangulo
print("Lados del primer triangulo:")
triangulo1.verlados()

# Calcular y mostrar área y perímetro del primer triangulo
print("\nCalculos del primer triangulo:")
triangulo1.area()
triangulo1.perimetro()

# Asignar lados al segundo triangulo
triangulo2.darlados()

# Mostrar lados del segundo triangulo
print("\nLados del segundo triangulo:")
triangulo2.verlados()

# Calcular y mostrar área y perímetro del segundo triangulo
print("\nCalculos del segundo triangulo:")
triangulo2.area()
triangulo2.perimetro()
