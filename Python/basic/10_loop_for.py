"""
O loop for é usados para iterar sobre uma sequência em que sabemos o tamanho
pode ser uma lista, uma tupla, um dicionário um conjunto ou uma string

"""

"""
for i in range(0, 11):
    print(f'3 x {i} = {5*i}')
"""
# o padrão da função range() pode receber 3 parâmetros

"""
for i in range (0,101, 25):
    print(i)
"""

for i in range (0, 101):
    if i % 2 == 0:
        print(f'{i} é um número par')
    else:
        print(f'{i} é um número ímpar')