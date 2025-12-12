import random, time
def main():
    def test0():
        print('test0')

        n = int(input('Число n: '))
        k = int(input('Число k: '))

        tic = time.perf_counter()

        a = [random.randint(0, 20000) for i in range(n)]
        a.sort()
        resault = 0 if a[0] >= k else n+1
        print(a)

        for i in range(n-1):
            if a[i-1] <= k < a[i]: resault = i; break
            elif a[i] == k: resault = i-1; break

        print(resault)

        toc = time.perf_counter()
        print(f'Вычисление заняло: {toc - tic:0.4f} секунд\n')

    def test1():
        print('test1')

        n = int(input('Число n: '))
        k = int(input('Число k: '))

        tic = time.perf_counter()

        b = [0, n-1]

        a = [random.randint(0, 20000) for i in range(n)]
        a.sort()
        resault = 0 if a[0] >= k else n+1
        print(a)

        while b[0] <= b[1]:
            center = (b[0] + b[1]) // 2
            if center < n-1 and a[center-1] <= k < a[center]:
                resault = center; break
            elif a[center] < k: b[0] = center + 1
            else: b[1] = center - 1

        print(resault)

        toc = time.perf_counter()
        print(f'Вычисление заняло: {toc - tic:0.4f} секунд\n')

    def test2():
        print('test2')

        n = int(input('Число n: '))
        k = int(input('Число k: '))

        tic = time.perf_counter()

        a = [random.randint(0, 20000) for i in range(n)]
        a.sort()
        resault = 0 if a[0] >= k else n+1
        print(a)

        def rec(a, k, n, i=0):
            if i >= n-1 or len(a) <= 2: return 0
            elif a[i-1] <= k < a[i]: return i
            elif a[i] == k: return i
            return rec(a, k, n, i+1)

        try:
            resault = rec(a, k, n)
            print(resault)

        except RecursionError: print('Превышен лимит рекурсии')

        toc = time.perf_counter()
        print(f'Вычисление заняло: {toc - tic:0.4f} секунд\n')

    def super_hyper_tester3000():
        print('super_hyper_tester3000');n=int(input('Число n: '));k=int(input('Число k: '));tic=time.perf_counter();a=[]
        for i in range(n):a.append(random.randint(0,20000))
        for i in range(n):
          for j in range(0,n-i-1):
            if a[j]>a[j+1]:bugcup=a[j];a[j]=a[j+1];a[j+1]=bugcup
        if a[0]>=k:resault=len(a)+1
        else:resault=0
        print(a);ababababa=-1
        for i in range(len(a)):
          if a[i]==k:ababababa=i;print(ababababa);break;
        if ababababa!=-1:pass
        else:
          a.append(k);n = n+1
          for i in range(n):
            for j in range(0,n-i-1):
              if a[j]>a[j+1]:bugcup=a[j];a[j]=a[j+1];a[j+1]=bugcup
        while True:
          c=random.randint(0,n-1);
          if a[c]==k:print(c);break
        toc=time.perf_counter()
        print('Вычисление заняло:'+' '+str(round(toc-tic,4))+' '+'секунд')

    test0()
    test1()
    test2()
    super_hyper_tester3000()
main()
