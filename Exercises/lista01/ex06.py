"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""
import math
r = float(input('Informe o raio: '))
# area = math.pi * math.pow(r, 2)
area = math.pi * r ** 2

print(f'Raio informado: {r}.\nA área do circulo é: {round(area, 2)}.')
