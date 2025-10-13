"""Programa para calcular as raízes de uma equação do segundo grau na forma ax² + bx + c = 0

O programa faz as seguintes verificações:
- Se a = 0, não é equação do segundo grau
- Se delta < 0, não possui raízes reais
- Se delta = 0, possui uma raiz real
- Se delta > 0, possui duas raízes reais
"""

import math

print("=== CALCULADORA DE EQUAÇÕES DO SEGUNDO GRAU ===")
print("Equação na forma: ax² + bx + c = 0\n")

# Solicitar o valor de 'a'
a = float(input("Digite o valor de a: "))

# Verificar se é uma equação do segundo grau
if a == 0:
    print("\nERRO: O valor de 'a' não pode ser zero!")
    print("Para a = 0, a equação não é do segundo grau.")
    print("Programa encerrado.")
else:
    # Solicitar os demais valores
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    # Exibir a equação
    print(f"\nEquação: {a}x² + {b}x + {c} = 0")
    
    # Calcular o delta (discriminante)
    delta = b**2 - 4*a*c
    
    print(f"Delta (Δ) = b² - 4ac = {b}² - 4×{a}×{c} = {delta}")
    
    # Analisar o delta e calcular as raízes
    if delta < 0:
        print("\nResultado: A equação NÃO possui raízes reais.")
        print("Delta negativo indica raízes complexas.")
        
    elif delta == 0:
        print("\nResultado: A equação possui UMA raiz real (raiz dupla).")
        raiz = -b / (2*a)
        print(f"x = -b/2a = -{b}/(2×{a}) = {raiz}")
        
    else:  # delta > 0
        print("\nResultado: A equação possui DUAS raízes reais distintas.")
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        
        print(f"x₁ = (-b + √Δ)/2a = ({-b} + √{delta})/(2×{a}) = {raiz1}")
        print(f"x₂ = (-b - √Δ)/2a = ({-b} - √{delta})/(2×{a}) = {raiz2}")

print("\nPrograma finalizado!")