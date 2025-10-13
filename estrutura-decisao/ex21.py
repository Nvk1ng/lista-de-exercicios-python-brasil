"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""

valor = int(input("Digite o valor do saque (1 a 600): "))

if valor < 1 or valor > 600:
    print("Valor inválido")
else:
    notas100 = valor // 100
    valor = valor % 100
    
    notas50 = valor // 50
    valor = valor % 50
    
    notas10 = valor // 10
    valor = valor % 10
    
    notas5 = valor // 5
    valor = valor % 5
    
    notas1 = valor
    
    resultado = []
    
    if notas100 > 0:
        if notas100 == 1:
            resultado.append("1 nota de R$ 100")
        else:
            resultado.append(f"{notas100} notas de R$ 100")
    
    if notas50 > 0:
        resultado.append("1 nota de R$ 50")
    
    if notas10 > 0:
        if notas10 == 1:
            resultado.append("1 nota de R$ 10")
        else:
            resultado.append(f"{notas10} notas de R$ 10")
    
    if notas5 > 0:
        resultado.append("1 nota de R$ 5")
    
    if notas1 > 0:
        if notas1 == 1:
            resultado.append("1 nota de R$ 1")
        else:
            resultado.append(f"{notas1} notas de R$ 1")
    
    if len(resultado) == 1:
        print(resultado[0])
    elif len(resultado) == 2:
        print(resultado[0] + " e " + resultado[1])
    else:
        saida = ", ".join(resultado[:-1]) + " e " + resultado[-1]
        print(saida)