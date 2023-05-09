"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    - o produto do dobro do primeiro com metade do segundo .
    - a soma do triplo do primeiro com o terceiro.
    - o terceiro elevado ao cubo.
"""
import math
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = float(input('Digite o 3º valor: '))

res1 = (num2 * 2)*(num1/2)
res2 = (num1 * 3) + num3
res3 = math.pow(num3,3)

print(f'O produto de {num1} * 2 com {num2}/2 = {res1}.')
print(f'A soma do triplo {num1}* 3 + {num3} = {res2}.')
print(f'Resultado de {num3}³ = {round(num3)}')
