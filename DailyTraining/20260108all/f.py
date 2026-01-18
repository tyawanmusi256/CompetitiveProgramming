n,r=map(int,input().split())
l=list(map(int,input().split()))
ans=0
if r>=1:
    closed=0
    opened=0
    anss=0
    for i in range(r-1,-1,-1):
        if l[i]==0:
            anss=max(anss,1+closed*2+opened)
            opened+=1
        else:
            closed+=1
    ans+=anss
if r<n:
    closed=0
    opened=0
    anss=0
    for i in range(r,n):
        if l[i]==0:
            anss=max(anss,1+closed*2+opened)
            opened+=1
        else:
            closed+=1
    ans+=anss
print(ans)