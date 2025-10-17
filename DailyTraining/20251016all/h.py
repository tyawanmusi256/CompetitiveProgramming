n,m,k=map(int,input().split())
a=list(map(int,input().split()))

if m==k:
    ans=[sum(a[:m])]
    for i in range(n-m):
        ans.append(ans[-1]-a[i]+a[i+m])
    print(*ans)
    exit()

from sortedcontainers import SortedList
s=SortedList(a[:m])
ans=sum(s[:k])
anss=[ans]
for i in range(n-m):
    x=a[i]
    y=a[i+m]


    if x<=s[k-1]:
        ans-=x
        ans+=s[k]
    s.remove(x)
    
    if y<=s[k-1]:
        ans+=y
        ans-=s[k-1]
    s.add(y)

    anss.append(ans)
print(*anss)