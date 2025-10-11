print('\nЗадача 1:')
while True:
    print('Число должно быть целым и больше 0')
    try:
        n = int(input('n='))
    except ValueError:
        print('Введите число!')
    if n>0:break
matrix2 = [1,0]
for i in range(n*n):
    matrix2.insert(-1,0)
print(*matrix2)
while matrix2[-1] != 1:
    matrix2.pop(-1)
    matrix2.insert(0,2)
    print(*matrix2)

print('\nЗадача 2:')
while True:
    try:
        n = int(input('n='))
    except ValueError:
        print('Введите число!')
    if n>0:break
matrix2 = []
for i in range(n):
    matrix2.append(n)
    n-=1
matrix2.append(0)
b = 1
print(*matrix2)
while matrix2[0]!=0:
    matrix2.pop(0)
    matrix2.append(b)
    b+=1
    print(*matrix2)

print('\nЗадача 3:')
while True:
    print('Число должно быть целым и больше 0')
    try:
        n = int(input('n='))
    except ValueError:
        print('Введите число!')
    if n>0:break
while True:
    print('Число должно быть целым и больше 0')
    try:
        m = int(input('m='))
    except ValueError:
        print('Введите число!')
    if m>0:break
matrix2 = ['.','*','.','*','.','*']
for i in range(n*m-1):
    if matrix2[0] == '.':
        matrix2.append('.')
    else: matrix2.append('*')
    matrix2.pop(0)
    print(*matrix2)

print('Задача 4:')
while True:
    print('Число должно быть не четным и целым и больше 2')
    try:
        n = int(input('n='))
    except ValueError:
        print('Введите число!')
    if n%2!=0 and n>2:break

matrix2 = []
for i in range(n*n):
    matrix2.append([])
for i in range(n*n):
    for i in range(n*n):
        matrix2[i-1].append('.')
matrix2[len(matrix2)//2] = []
for i in range(n*n):
    matrix2[len(matrix2)//2].append('*')
for i in range(n*n):
    for i in range(n*n):
        matrix2[i][len(matrix2)//2]='*'
for i in range(n*n):
    for i in range(n*n):
        matrix2[i][i]='*'
        matrix2[i][-i-1] = '*'
for i in range(len(matrix2)):
    print(matrix2[i])
    i+=1

print('\nЗадача 5:')
print('Я хз как это реализовать')

print('\nЗадача 6:')
while True:
    ababa = input('a-нарисовать квадрат\n'
          'b-нарисовать треугольник\n'
          'c-нарисовать круг\n'
          'd-выход\n\n')
    if ababa == 'a':
        print('*****\n'
              '*   *\n'
              '*****\n')
    elif ababa == 'b':
        print('  *\n'
              ' * *\n'
              '*****\n')
    elif ababa == 'c':
        print(' ***\n'
              '*   *\n'
              ' ***\n')
    elif ababa == 'd': break
