n,p=map(int,input().split())
prime=[]
for i in range(2,int(p**0.5)+1):
    if p%i==0:
        while p%i==0:
            prime.append(i)
            p//=i
    if p==1:break
if p!=1:prime.append(p)
from collections import Counter
c=Counter(prime)
ans=1
for i in c:
    while c[i]>=n:
        ans*=i
        c[i]-=n
print(ans)