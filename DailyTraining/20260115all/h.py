n,m=map(int,input().split())
city=[list(map(int,input().split()))for _ in range(n)]
tr=[list(map(int,input().split()))for _ in range(m)]

#dp[bit][i]: bitで表される都市群を訪れ、最後にiにいるときの最小コスト
goal_mask=(1<<n)-1
dp=[[10**18]*(n+m)for _ in range(1<<(n+m))]
ans=10**18
for i in range(n):
    x,y=city[i]
    dp[1<<i][i]=(x**2 + y**2)**0.5
    if n==1:
        ans=min(ans,dp[1<<i][i]+(x**2 + y**2)**0.5)
for i in range(m):
    x,y=tr[i]
    dp[1<<(n+i)][n+i]=(x**2 + y**2)**0.5
for bit in range(1<<(n+m)):
    c=1
    for i in range(n,n+m):
        if bit&(1<<i):
            c<<=1
    for i in range(n+m):
        if not(bit&(1<<i)):
            continue
        for j in range(n+m):
            if bit&(1<<j):
                continue
            x1,y1=city[i]if i<n else tr[i-n]
            x2,y2=city[j]if j<n else tr[j-n]
            cost=(((x1 - x2)**2 + (y1 - y2)**2)**0.5)/c
            dp[bit|(1<<j)][j]=min(dp[bit|(1<<j)][j],dp[bit][i]+cost)
            if (bit|(1<<j))&goal_mask==goal_mask:
                if j<n:
                    ans=min(ans,dp[bit|(1<<j)][j]+(((x2**2 + y2**2)**0.5)/c))
                else:
                    ans=min(ans,dp[bit|(1<<j)][j]+(((x2**2 + y2**2)**0.5)/(c<<1)))
print(ans)
    