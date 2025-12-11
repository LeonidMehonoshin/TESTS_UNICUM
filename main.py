import random, time
def main():
    def test0():
        n = int(input('Число n: '))
        k = int(input('Число k: '))
        tic = time.perf_counter()
        a = [random.randint(0,  20000) for i in range(n)]
        a.sort()
        resault = 0
        for i in range(n):
            if a[i] > k and a[i] < k:
                resault = i
                break
            elif a[i] == k:
                resault = i-1
                break
            elif len(a) <= 2: break
        print(resault)
        toc = time.perf_counter()
        print(f'Вычисление заняло: {toc - tic:0.4f} секунд')
    def test1():
        n = int(input('Число n: '))
        k = int(input('Число k: '))
        tic = time.perf_counter()
        a = [random.randint(0,  20000) for i in range(n)]
        a.sort()
        resault = 0
        while True:
            center = len(a) // 2
            if len(a) <= 2: break
            elif a[center] > k and a[center+1] < k:
                resault = a[center]
                break
            elif a[center] == k:
                resault = center - 1
                break
            elif a[center] < k: a = a[0: center]
            else: a = a[center: len(a)]
        print(resault)
        toc = time.perf_counter()
        print(f'Вычисление заняло: {toc - tic:0.4f} секунд')
    test0()
    test1()
main()
