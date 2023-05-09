"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
hourMouth = float(input('Informe a quantidade de horas trabalhadas no mês: '))
hourValue = float(input('Informe o valor da hora trabalhada: '))
wage = hourMouth * hourValue
print(
    f'Horas trabalhadas {hourMouth}.\nValor horas {hourValue}.\nSalário mês: R$ {wage}')
