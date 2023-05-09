"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
"""
C = float(input('Informe a temperatura em Celsius. '))
F = C * (9/5)+32
print(f'Temperatura em Celsius: {format(C)}º.')
print(f'Temperatura em Fahrenheit: {format(F)}º.')
