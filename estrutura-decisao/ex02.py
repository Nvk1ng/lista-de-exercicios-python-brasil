"""Faça um programa que peça um valor e mostre na tela se o valor é positivo ou 
negativo.
"""

valor = int(input("Digite um numero: "))

if valor >= 0:
    print(f"{valor} Não é um número negativo")
else:
    print(f"{valor} É um número negativo")