"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> eh_ano_bissexto(400)
    True
    >>> eh_ano_bissexto(800)
    True
    >>> eh_ano_bissexto(2100)
    False
    >>> eh_ano_bissexto(2004)
    True
    >>> eh_ano_bissexto(2022)
    False
"""

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print("É bissexto")
elif ano % 100 == 0:
    print("Não é bissexto")
elif ano % 4 == 0:
    print("É bissexto")
else:
    print("Não é bissexto")
