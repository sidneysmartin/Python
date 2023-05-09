"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
height = float(input('Informe a sua altura em metros: '))
man = (72.7 * height) - 58
woman = (62.1 * height) - 44.7
print(f'Altura informada: {height}m.')
print(f'Peso ideal homem: {round(man,2)} kg.')
print(f'Peso ideal mulher: {round(woman,2)} kg.')
