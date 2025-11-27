import random
#1
n = int(input('1) Число: '))
result = ['FizzBuzz' if x % 3 + x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else 0  for x in [random.randint(0, n) for _ in range(100)]]
print(result)
#2
n = int(input('2) Число: '))
result = [0 if x <= 10 else x for x in [random.randint(0, n) for _ in range(n)]]
print(result)
#3
n = int(input('3) Число: '))
result = {i: "even" if random.randint(0, n) % 2 else "odd" for i in range(n)}
print(result)
#4
n = int(input('4) Число: '))
result = [5 if len(x) > 5 else len(x) for x in [str(random.randint(0, n)) for _ in range(n)]]
print(result)