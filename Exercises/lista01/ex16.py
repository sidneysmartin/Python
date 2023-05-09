"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em m²
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 m²
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
area = float(input('Informe a área a ser pintada em metros: '))
litros = area / 3.0
latas = litros / 18
price = latas * 80
print(f'Área: {round(area,2)}m².\nLitros: {round(litros,2)}l.\nTotal: R$ {round(price,2)}')
