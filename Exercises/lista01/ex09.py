"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9
"""
F = float(input("Informe a temperatura em Fahrenheit: "))
C = 5 * ((F-32)/9)

print(f'{round(F,2)}Fº\n{round(C,2)}Cº')
