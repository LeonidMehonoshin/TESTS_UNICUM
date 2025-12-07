import random, time

#0
def test0():
    n = 0
    while not (1 <= n and n <= 1000):
        try:
            n = int(input())
        except ValueError: print('Неверный тип данных!')
    a = [random.randint(0, 10000) for i in range(n)]
    b = 0
    for i in range(n-1):
        if a[i] * a[i+1] % 58 == 0: b += 1
    return b

def test1():
    n = 0
    while not (1 <= n and n <= 1000):
        try:
            n = int(input())
        except ValueError: print('Неверный тип данных!')
    a = [random.randint(0, 10000) for i in range(n)]
    b = 0
    for i in range(n-1):
        if (a[i] * a[i+1] % 29 == 0 and
            a[i] * a[i+1] % 2 == 0): b += 1
    return b

def test2():
    n = 0
    while not (1 <= n and n <= 1000):
        try:
            n = int(input())
        except ValueError: print('Неверный тип данных!')
    a = [random.randint(0, 10000) for i in range(n)]
    b = 0
    for i in range(n-1):
        if a[i] % 58 == 0 and a[i+1] % 58 == 0: b += 1
    return b

start = time.time()
print(f'test0: {test0()}')
end = time.time()
print(f'Время выполнения: {round(end - start, 2)}')

start = time.time()
print(f'test1: {test1()}')
end = time.time()
print(f'Время выполнения: {round(end - start, 2)}')

start = time.time()
print(f'test2: {test2()}')
end = time.time()
print(f'Время выполнения: {round(end - start, 2)}')

#1
def test0_0():
    a = [[random.randint(0,2147483647), random.randint(0,2147483647)] for i in range(3)]
    if a[0][0]+a[1][0]+a[2][0] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][0], a[2][0]}')
    elif a[0][1]+a[1][0]+a[2][0] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][1], [1][0], a[2][0]}')
    elif a[0][0]+a[1][1]+a[2][0] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][1], a[2][0]}')
    elif a[0][0]+a[1][0]+a[2][1] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][0], a[2][1]}')
    elif a[0][1]+a[1][1]+a[2][0] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][0], a[2][0]}')
    elif a[0][1]+a[1][0]+a[2][1] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][0], a[2][0]}')
    elif a[0][1]+a[1][0]+a[2][1] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][0], a[2][0]}')
    elif a[0][1]+a[1][1]+a[2][1] == 2147483647:
        print(f'Спсиок: {a}\n'
              f'Выбранные числа: {a[0][0], [1][0], a[2][0]}')
    else: print(0)

def test0_1():
    a = [[random.randint(0,2147483647), random.randint(0,2147483647)] for i in range(3)]
    run = 1
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if a[0][i] + a[1][j] + a[2][k] == 2147483647:
                    print(f'Список: {a}\n'
                          f'Выбранные числа: {a[0][i]}, {a[1][j]}, {a[2][k]}')
                    run = 0
                    break
            if run == 0: break
        if run == 0: break
    if run == 1: print(0)

print('test0_0')
start = time.time()
test0_0()
end = time.time()
print(f'Время выполнения: {round(end - start, 2)}')


print('test0_1')
start = time.time()
test0_1()
end = time.time()
print(f'Время выполнения: {round(end - start, 2)}')
