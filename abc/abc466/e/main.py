#a|bb|a|b|aa
#2*k+1個の区間に分かれる
n,k=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(2*k+1) for _ in range(n+1)]
dp[0][0]=ab[0][0]
dp[0][1]=ab[0][1]
for i in range(1,n):
    for j in range(2*k+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+ab[i][0]
            continue
        if j&1:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+ab[i][1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+ab[i][0]
print(max(dp[n-1]))