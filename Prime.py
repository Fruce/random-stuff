def prime(n,a):
    if a%n == 0:
        print('not prime')
    elif n == 2:
        print('prime')
    else:
        prime(n-1,a)
a = int(input("enter a number: "))
prime(a-1,a)
