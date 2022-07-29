def is_prime(n):
    if n == 2 or n == 3 or n==5:
        return True
    if int(str(n)[-1])%2 == 0 or str(n)[0] == '-' or str(n)[-1] == '5' or n==1:
        return False #if divisible by 2 or 5

    sum,temp = 0,n
    while (temp != 0):      
        sum += (temp % 10)
        temp = temp//10
    if sum%3 == 0:
        return False #if divisible by 3

    if isinstance(n**0.5, int) is True:
        return False #if it's square root is integer

    for i in range(7,n):
        if n%i == 0:
            return False #if its a factor of 2 prime numbers
    else:
        return True #if prime
        
print(is_prime(-5))
