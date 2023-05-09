# Os operadores lógicos são usados para combinar instruções condicionais:
# https://www.w3schools.com/python/python_operators.asp

"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""

"""
score1 = float(input('Digite a nota 1: '))
score2 = float(input('Digite a nota 2: '))

avg = (score1 + score2) / 2

if avg < 6:
    print(f"A média é {avg} - Reprovado.")
elif avg <= 9:
    print(f"A média é {avg} - Aprovado.")
else:
    print(f"A média é {avg} - Aprovado com louvor.")

"""

"""
Operator    Example
and         x < 5 and  x < 10
or          x < 5 or x < 4
not         not(x<5 and x <10)

"""

x = 7
if not (x < 5 and x < 4):
    print("Valor correto")
else:
    print("Valor errado")
