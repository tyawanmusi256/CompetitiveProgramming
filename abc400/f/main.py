n=int(input())
c=list(map(int,input().split()))
x=list(map(int,input().split()))
c+=c
dp=[[10**13]*(2*n) for _ in range(2*n)]
for i in range(2*n):
    dp[i][i]=1+x[c[i]-1]
    for j in range(i+1,2*n):
        dp[j][i]=0
for l in range(1,n+1):
    for i in range(2*n):
        j=i+l
        if j>=2*n:
            break
        for k in range(i,j):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
            if c[k]==c[j]:
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j-1]+j-k)
            if c[k]==c[i] and k!=i:
                dp[i][j]=min(dp[i][j],dp[i+1][k-1]+dp[k][j]+k-i)
ans=10**13
for i in range(n):
    ans=min(ans,dp[i][i+n-1])
print(ans)