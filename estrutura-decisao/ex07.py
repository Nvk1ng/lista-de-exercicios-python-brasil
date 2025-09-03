"""Faça um programa que leia três números e mostre o maior e o menor deles:
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = a
menor = a

# Verifica maior
if b > maior:
    maior = b
if c > maior:
    maior = c

# Verifica menor
if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"O maior foi {maior}")
print(f"O menor foi {menor}")
