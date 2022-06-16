#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

from cmath import pi

# Área de un Triángulo
def areaTriangulo(base, altura):
    return base * altura / 2

print(areaTriangulo(5, 4))

# Área de un Círculo
def areaCirculo(radio):
    return pi * radio ** 2

print(areaCirculo(5))