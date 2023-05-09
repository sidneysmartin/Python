"""
https://www.w3schools.com/python/python_while_loops.asp
Python tem dois comandos de loop primitivos
while loops
for loops
---
O loop while
Com o loop while , podemos executar um conjunto de instruções, desde que uma condição seja verdadeira.
"""

"""
Tabuada exemplo
i = 1
while i <= 10:
    print(f"{3} * {1} = {i * 3}")
    i += 1
"""

# else
# com a instrução else, podemos executar um bloco de código uma vez quando a condição não for mais verdadeira:
"""
i = 1
while i < 6:
  print(i)
  i += 1
else:
    print('A condição não é mais inferior a 6')
"""

#break
#Com a instrução break podemos parar o loop mesmo se a condição while for verdadeira:
"""
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i+=1
"""

#continue
#Com a instrução continue , podemos interromper a iteração atual e continuar com a próxima:

"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
"""
avg = 0
while avg != -1:
    avg = int(input("Digite uma nota ou -1 para sair. "))
    print(f'A média digitada é {avg}')
    if avg == -1:
        break
print("Valores inseridos.")