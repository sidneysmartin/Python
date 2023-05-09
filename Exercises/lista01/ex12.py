"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
height = float(input('Informe a sua altura em metros: '))
weight = (72.7 * height) - 58

print(f'Altura = {round(height,2)}m.\nPeso ideal = {round(weight,2)}kg.')
