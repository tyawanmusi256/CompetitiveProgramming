n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=sum(a)*(n-1)
from bisect import bisect_left
for i in range(n-1):
    j=bisect_left(a,10**8-a[i])
    ans-=10**8*(n-max(i+1,j))
print(ans)