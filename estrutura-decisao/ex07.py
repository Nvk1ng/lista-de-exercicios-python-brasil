"""Faça um programa que leia três números e mostre o maior e o menor deles:
"""

a= int(input("Digite o primeiro numero: "))
b= int(input("Digite o segundo numero:"))
c= int(input("Digite o terceiro numero:"))

maior = a 
menor = a

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if b < a and b < c :
    menor = b
elif c < a and c < b:
    menor = c

print(f"o maior foi {maior}")
print(f"o menor foi {menor}")