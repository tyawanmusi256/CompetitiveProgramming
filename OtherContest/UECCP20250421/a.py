def prime_factor(n):
    ass=[]
    for i in range(2,int(n**0.5)+1):
        while n%i==0:ass.append(i);n//=i
    if n!=1:ass.append(n)
    return ass

n=int(input())
p=prime_factor(n)
from collections import Counter
c=Counter(p)
ans=0
for i in c:
    m=c[i]
    for j in range(1,10**20):
        if j>m:break
        ans+=1
        m-=j
print(ans)