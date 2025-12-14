def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]

prime=sieve_of_eratosthenes(10**6)
n=len(prime)
x=[]
for i in prime:
    j=i*i
    while j<=10**12:
        x.append((j,i))
        j*=i*i
x.sort()
y=[]
for i in range(n-1):
    for j in range(i+1,n):
        if x[i][1]==x[j][1]:
            continue
        if x[i][0]*x[j][0]>10**12:
            break
        y.append(x[i][0]*x[j][0])
y.sort()
from bisect import bisect_right
for i in range(int(input())):
    a=int(input())
    print(y[bisect_right(y,a)-1])
