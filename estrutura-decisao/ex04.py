"""Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogais = ["a","e","i","o", "u"]

letra_digita = input("Digite uma letra: ").lower()

if letra_digita in vogais:
    print(f"{letra_digita} é uma vogal")
else:
    print(f"{letra_digita} não é uma vogal")
