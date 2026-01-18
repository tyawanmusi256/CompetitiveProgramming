prime_various=[0]*(10**6+2)
for i in range(2,10**6+2):
    if prime_various[i]==0:
        for j in range(i,10**6+2,i):
            prime_various[j]+=1
q=int(input())
for _ in range(q):
    a=int(input())
    x=int(a**0.5)+1
    while x>0:
        if prime_various[x]==2 and x*x<=a:
            print(x*x)
            break
        x-=1
