
#    Operator |   Name            |   Exemple
#    +     |   Addition        |   x + y
#    -     |   Subtraction     |   x - y
#    *     |   Multiplication  |   x y
#    /     |   Division        |   x / y
#    %     |   Modulus         |   x % y
#    **    |   Exponentiation  |   x ** y
#    //    |   Floor division  |   x//y
# python assim como todas as linguagens de programação respeitam as precedências de operações da matemática.
#

score1 = int(input('Digite a nota 1: '))
score2 = int(input('Digite a nota 2: '))

addiction = score1 + score1
sub = score1 - score2
multi = score1 * score2
div = score1 / score2
mod = score1 % score2
expo = score1 ** score2
floorDiv = score1 // score2
avg = (score1 + score2) / 2

print(f" {score1} + {score2} = {addiction}")
print(f" {score1} avg {score2} = {avg}")
print(f" {score1} - {score2} = {sub}")
print(f" {score1} * {score2} = {multi}")
print(f" {score1} / {score2} = {div}")
print(f" {score1} % {score2} = {mod}")
print(f" {score1} ** {score2} = {expo}")
print(f" {score1} // {score2} = {floorDiv}")
