import random

#1
n = int(input('\n1) Число n: '))
result = ["четное" if _ % 2 == 0  else "нечетное" for _ in [random.randint(0,n) for i in range(n)]]
print(result)

#2
print('\n2) 1-100')
result = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)]
print(result)

#3
n = int(input('\n3) Размер рандомного списка: '))
result = [i if i > 10 else 0 for i in [random.randint(-_, _) for _ in range(n)]]
print(result)

#4
n = int(input('\n4) Число n: '))
result = {i: "even" if i % 2 == 0 else "odd" for i in range(1, n + 1)}
print(result)

#5
n = int(input('\n5) Размер рандомного списка: '))
m = int(input('\n5) Максимальный размер строк: '))
result = [5 if len(x) > 5 else len(x) for x in [str(random.randint(0, m+1)) for _ in range(m)]]
print(result)

#6
n = input('\n6) Напишите исходный список через ', ' (запятая с пробелом): ')
result = [0 if _ < 0 else _ for _ in [int(i) for i in n.split(', ')]]
print(result)

#7
n = int(input('\n7) Размер рандомного списка: '))
result = [n ** 0.5 if n >= 0 else 0 for n in [random.randint(-_, _) for _ in range(n)]]
print(result)

#8
n = input('\n8) Напишите исходный список через ', ' (запятая с пробелом): ')
result = [x**2 if x % 2 == 0 else x**3 for x in [int(_) for _ in n.split(', ')]]
print(result)

#9
n = int(input('\n9) Размер рандомного списка: '))
result = ["High" if x > 50 else "Medium" if x >=20 and x<=50 else "Low" for x in [random.randint(-_ // 2, _ // 2) if _ % 2 == 0 else random.randint(-_ // 2, _ // 2+1) for _ in range(n)]]
print(result)
