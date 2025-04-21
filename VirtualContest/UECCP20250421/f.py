n=int(input())
x,y=map(int,input().split())
inf=301
dp=[[[inf]*301 for _ in range(301)] for _ in range(n+1)]
dp[0][0][0]=0
ans=inf
for i in range(1,n+1):
    a,b=map(int,input().split())
    for j in range(301):
        for k in range(301):
            dp[i][j][k]=min(dp[i-1][j][k],dp[i][j][k])
            dp[i][min(j+a,300)][min(k+b,300)]=min(dp[i-1][j][k]+1,dp[i][min(j+a,300)][min(k+b,300)])
            if x<=j and y<=k:
                ans=min(ans,dp[i][j][k])
print(ans if ans!=inf else -1)