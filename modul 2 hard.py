import random

n = random.randint(3, 20)

def answer():
    print()
    print(*stone_1)
    for i in stone_2:
        print('  ', *i)

def proverka():
    if (nambe1 + nambe2) % n == 0: 
        kombinaciya = 0
        print('ВЫ молодец!')
    
stone_1 = [n]
stone_2 = [['-', '-'], ['-', '-']]
var = n
print('Начнём игру -_*')
answer()
for i in range(1, n):
    for j in range(1, n):
        var = (i + j) % n
        if var == 0:
            print(i, j)