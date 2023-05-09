"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em m²
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 m²
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
area = float(input('Informe a área a ser pintada em metros: '))
litros = area / 3.0
latas = litros / 18
galoes = litros / 3.6
priceList = latas * 80
priceGaloes = galoes * 25
print(f'Área: {round(area,2)}m².')
print(f'Litros: {round(litros,2)}l.')
print(f'Total em latas: R$ {round(priceList,2)}.')
print(f'Total em galões: R$ {round(priceGaloes,2)}')
