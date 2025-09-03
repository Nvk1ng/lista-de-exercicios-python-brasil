"""Faça um programa que leia três números e mostre o maior deles:
"""

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é o maior numero")
elif numero2 > numero3:
    print(f"{numero2} é o maior numero")
else:
    print(f"{numero3} é o maior numero")