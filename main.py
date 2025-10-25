import random

#Мехоношин Леонид ИИ-71
#variant C
#1

print(
    '\nМехоношин Леонид ИИ-71\n'
    'Вариант C\n\n'
    'Задача 1\n'
)

matrix = [
    [' ', ' ', ' ', '*'],
    [' ', ' ', '*', '*', '*'],
    [' ', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*']
]

for line in matrix:
    for column in line:
        print(column, end='')
    print()

while True:
    num = input('\n1-перейти к следующей задаче\n:')
    if num == '1': break

#2
print('\nЗадача 2\n')
while True:
    try:
        num = float(input('Введите любое число, чтобы определить принадлежит ли оно отрезку [a,b]\n:'))
        a = float(input('Число a\n:'))
        b = float(input('Число b\n:'))
        if a <= b: break
        else: print('a не может быть больше b')
    except ValueError:
        print('Неверный формат записи данных! Повторите попытку...')
if a <= num <= b: print('данное число принадлежит отрезку [a,b]!')
else: print('данное число НЕ принадлежит отрезку [a,b]!!!')

while True:
    num = input('\n1-перейти к следующей задаче\n:')
    if num == '1': break

#3
print('\nЗадача 3\n')

n = random.randint(8, 30)
matrix = [[random.randint(0,9) for _ in range(n//2)] for _ in range(n//4)]

print('Было:')
for line in matrix:
    for column in line:
        print(column, end='')
    print()

print('\nСтало:')
for line in matrix:
    backup_line0 = line[0]
    del line[0]
    line.append(backup_line0)
    for column in line:
        print(column, end='')
    print()
