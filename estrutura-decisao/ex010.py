"""Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"
, conforme o caso.
"""
print("qual turno voce estuda:")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")

turno = input().upper()

if turno == "M":
    print("Matutino")
elif turno == "V":
    print("Vespertino")
elif turno == "N":
    print("Noturno")
else:
    print("Valor inválido!")
