# List are used to store multiple items in a single variables.
# List are created using square brackets.

#position [0, 1, 2, 3]
"""
grades  = [10, 20, 5, 3]

print(grades)
print(f'Nota na posição [0] {grades[0]}')
print(f'Nota na posição [1] {grades[1]}')
print(f'Nota na posição [2] {grades[2]}')
print(f'Nota na posição [3] {grades[3]}')
#print(f'Nota na posição [4] {grades[4]}')#vErro não existe a posição 4 nessa lista

print(f'tamanho da lista: {len(grades)}')
"""

"""
values = [27,35,42,28,9]
sum = 0
for i in values:
    sum = sum + i
    print(i)
print(f'{values}')
print(f'A soma dos valores é {sum}')
"""


grades = []

while True:
    grade = int(input("Digite uma nota ou -1 para sair: "))
    if grade == -1:
        break
    grades.append(grade)

sum = 0
for i in grades:
    sum+=i

print(f'Notas informadas - {grades}')
print(f'Média das notas: {sum/len(grades)}')


