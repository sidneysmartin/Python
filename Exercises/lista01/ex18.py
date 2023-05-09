"""
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
size = float(input('Informe o tamanho do arquivo em (MB): '))
speed = float(input('Informe a velocidade da internet: (Mbps): '))
result = size / (speed * 60)
print(f'Tamanho do arquivo: {round(size,2)}mb.')
print(f'Velocidade da internet: {speed}Mbps.')
print(f'Tempo de download: {round(result,2)}s')
