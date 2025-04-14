n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    for x in a:
        if i-x>=0:
            dp[i]=max(dp[i],i-dp[i-x])
print(dp[n])