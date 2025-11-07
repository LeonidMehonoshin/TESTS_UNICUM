#1
print('#1')
n = int(input('n = '))

def rec0(n, resault=[]):
    if n != 0:
        resault.append(n)
        n -= 1
        rec0(n,resault)
    else:
        resault.pop(0)
        print(*resault[::-1], sep = ', ')
rec0(n)

#2
print('#2')
a = int(input('a = '))
b = int(input('b = '))

def rec1(a, b, resault=[]):
    resault.append(a)
    if a == b:
        if len(resault) == 1: resault.append(a)
        print(*resault, sep = ', ')
    elif a < b: rec1(a + 1, b, resault)
    elif a > b: rec1(a - 1, b, resault)
rec1(a, b)

#3
print('#3')
n = int(input('n = '))
def rec2(n):
    if n <= 0: print("NO")
    elif n == 1: print("YES")
    elif n % 2 == 0: rec2(n // 2)
    else: print("NO")
rec2(n)

#4
print('#4')
n = int(input('n = '))
def rec3(n, a=0, b=1):
    if n == 0: print(0)
    elif n == 1: print(a)
    else:
        print(a, end=', ')
        rec3(n - 1, b, a + b)
rec3(n)
