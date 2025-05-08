n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for i in range(m):
    u,v,a,b=map(int,input().split())
    edge[u-1].append((v-1,a,b))
ok=0
ng=10**4+1
inf=10**18
mid=(ok+ng)/2
for _ in range(50):
    mid=(ok+ng)/2
    dp=[-inf]*n
    dp[0]=0
    for i in range(n):
        for j,a,b in edge[i]:
            dp[j]=max(dp[j],dp[i]+a-mid*b)
    if dp[n-1]>=0:
        ok=mid
    else:
        ng=mid
print(ok)