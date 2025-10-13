"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""
resp1 = input("Telefonou para a vítima? ")
resp2 = input("Esteve no local do crime? ")
resp3 = input("Mora perto da vítima? ")
resp4 = input("Devia para a vítima? ")
resp5 = input("Já trabalhou com a vítima? ")

respostas_sim = 0

if resp1.lower() == 'sim':
    respostas_sim += 1
if resp2.lower() == 'sim':
    respostas_sim += 1
if resp3.lower() == 'sim':
    respostas_sim += 1
if resp4.lower() == 'sim':
    respostas_sim += 1
if resp5.lower() == 'sim':
    respostas_sim += 1

if respostas_sim == 5:
    print("Assassino")
elif respostas_sim >= 3:
    print("Cúmplice")
elif respostas_sim == 2:
    print("Suspeito")
else:
    print("Inocente")