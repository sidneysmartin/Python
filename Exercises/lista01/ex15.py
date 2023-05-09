"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
wageHour = float(input('Informe o valor da hora: '))
amountHour = float(input('Informe a quantidade de horas: '))
salaryGross = wageHour * amountHour

txIR = salaryGross * 0.11
txINSS = salaryGross * 0.08
txSynd = salaryGross * 0.05
finalSalary = salaryGross - txIR - txINSS - txSynd

print(f'Salário Bruto: R$ {round(salaryGross, 2)}.')
print(f'IR 11%: R$ {round(txIR, 2)}.')
print(f'INSS 8%: R$ {round(txINSS, 2)}.')
print(f'Sindicato 5%: R$ {round(txSynd,2)}.')
print(f'Salário Liquido: R$ {round(finalSalary, 2)}.')
