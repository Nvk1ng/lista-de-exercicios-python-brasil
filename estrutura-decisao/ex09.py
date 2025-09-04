"""Faça um programa que leia três números e mostre-os em ordem decrescente:
"""

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))


if a >= b and a >= c:
    if b >= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a >= b:
        print(c, a, b)
    else:
        print(c, b, a)
