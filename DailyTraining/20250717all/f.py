n=int(input())
a=list(map(int,input().split()))
from collections import Counter
c=Counter(a)
a=list(set(a))
a.sort(reverse=True)
ans=[0]*n
for i in range(len(a)):
    ans[i]=c[a[i]]
print(*ans)