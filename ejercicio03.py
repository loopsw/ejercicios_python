print("Programa para calcular el área del triangulo")
try:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = base*altura/2
    print("El área del triangulo es : {}".format(area))
except:
    print("Error: Los datos no son númericos")
