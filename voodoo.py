#extremly fast program to count to number of proper fractions possible given the denominator
def primeDivs(N):
    p = 2
    while N>=p*p:
        print(p)
        if N%p == 0:   yield p
        while N%p==0:  N //= p
        p += 1 + (p&1)
    if N>1 : yield N

def proper_fractions(N):
    if N<2: return 0
    else:
        tot  = N
        for p in primeDivs(N):
            tot -= tot//p
        return tot

print(proper_fractions(25))
