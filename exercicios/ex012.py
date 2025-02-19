import math

def calcular_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

# Exemplo de uso:
cateto1 = float(input("Digite o primeiro cateto: "))
cateto2 = float(input("Digite o segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print(f"A hipotenusa é: {hipotenusa:.2f}")
