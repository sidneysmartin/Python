#https://www.w3schools.com/python/python_dictionaries.asp
# Os dicionários são usados para armazenar valores de dados em pares chave:valor
# Um dicionário é uma coleção que é ordenada, mutável e não permiti duplicatas.
# A partir da versão 3.7 do Python, os dicionários são ordenados, No python 3.6 e anteriores
# os dicionários não são ordenados.
"""
person = {
    'mago': "Zend",
    'habilidades': ['Fogo', 'Arcano', 'Gelo']
}
print(person['habilidades'])
"""

"""
person = [
    {
        'nome':'Ana Clara',
        'idade': '9',
        'sexo': 'feminino',
        'parentesco': 'sobrinha'
    },
    {
        'nome':'Carlos Eduardo',
        'idade': '2',
        'sexo': 'masculino',
        'parentesco': 'sobrinho'
    }
]

for i in person:
    # print('Nome', i['nome'])
    # print('Idade', i['idade'])
    # print('Sexo', i['sexo'])
    # print('parentesco',i['parentesco'])
    print(i)
"""

values = [
    [1,3,5,7,9],
    [0,2,4,6,8]
]
for i in values:
   print(i)
