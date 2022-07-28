def fibo(n,a=0,b=1):
    if a == 0:
        print(0)
    if n == 1:
        return
    else:
        sum = a+b
        print(sum)
        fibo(n-1,sum,a)
n = int(input('enter a num: '))
fibo(n)
