n,s=map(int,input().split())
a=list(map(int,input().split()))
from collections import Counter
c=Counter(a)
ans=0
for i in a:
    if s-i in c:
        ans+=c[s-i]
    if i*2==s:
        ans-=1
print(ans//2)