n,m=map(int,input().split())
a=[0]*n
b=[0]*n
ans=0
rc=[list(map(int,input().split())) for _ in range(m)]
for r,c in rc[::-1]:
    r-=1
    c-=1
    if a[r]==0 and b[c]==0:
        ans+=1
    a[r]=1
    b[c]=1
print(ans)