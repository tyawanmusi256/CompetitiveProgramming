from sortedcontainers import SortedList
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
if m==k:
    ans=sum(a[:m])
    anss=[ans]
    for i in range(m,n):
        ans+=a[i]
        ans-=a[i-m]
        anss.append(ans)
    print(*anss)
    exit()
first=a[:m]
first.sort()
mi=SortedList(first[:k])
ma=SortedList(first[k:])
ans=sum(mi)
anss=[ans]
for i in range(m,n):
    j=a[i-m]
    if j in mi:
        mi.remove(j)
        tmp=ma.pop(0)
        mi.add(tmp)
        ans+=tmp
        ans-=j
    else:
        ma.remove(j)
    x=a[i]
    if x < mi[-1]:
        mi.add(x)
        tmp=mi.pop(-1)
        ma.add(tmp)
        ans+=x
        ans-=tmp
    else:
        ma.add(x)
    anss.append(ans)
print(*anss)