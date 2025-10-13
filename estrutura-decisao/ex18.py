"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'
"""

data = input("Digite uma data (dd/mm/aaaa): ")

if '/' not in data:
    print("Data inválida")
else:
    partes = data.split('/')
    
    if len(partes) != 3:
        print("Data inválida")
    else:
        try:
            dia = int(partes[0])
            mes = int(partes[1])
            ano = int(partes[2])
            
            if mes < 1 or mes > 12:
                print("Data inválida")
            elif dia < 1:
                print("Data inválida")
            else:
                if mes in [1, 3, 5, 7, 8, 10, 12]:
                    dias_max = 31
                elif mes in [4, 6, 9, 11]:
                    dias_max = 30
                else:
                    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
                        dias_max = 29
                    else:
                        dias_max = 28
                
                if dia <= dias_max:
                    print("Data válida")
                else:
                    print("Data inválida")
        except:
            print("Data inválida")