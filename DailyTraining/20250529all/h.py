n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
x=list(map(int,input().split()))
m=[[10**18]*(n+1)for _ in range(n)]
for i in range(n):
    for j in range(i,-1,-1):
        m[i][j]=min(m[i][j+1],c[j])
dp=[[10**18]*(n+1) for _ in range(n+1)]
dp[0][0]=0
s=set(x)
for i in range(n):
    for j in range(n):
        if i-j<0:break
        dp[i+1][j+1]=min(dp[i+1][j+1],dp[i][j]+a[i]+m[i][i-j])
        if i+1 not in s:
            dp[i+1][j]=min(dp[i+1][j],dp[i][j])
print(min(dp[-1]))