def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def prime_factorization(n):
    factors = {}
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    if n > 1:
        factors[n] = 1
    return factors

def f(n,c):
    x=n
    while 1:
        y=x
        count=0
        while y!=0:
            count+=y//n
            y//=n
            if count>=c:
                return x
        x+=n
        

k=int(input())
a=prime_factorization(k)
ans=0
for i in a:
    ans=max(ans,f(i,a[i]))
print(ans)