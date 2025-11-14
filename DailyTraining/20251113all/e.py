n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0,0]for _ in range(n)]
dp[0]=[1,1]
for i in range(1,n):
    if dp[i-1][0]==1:
        if abs(a[i]-a[i-1])<=k:
            dp[i][0]=1
        if abs(b[i]-a[i-1])<=k:
            dp[i][1]=1
    if dp[i-1][1]==1:
        if abs(a[i]-b[i-1])<=k:
            dp[i][0]=1
        if abs(b[i]-b[i-1])<=k:
            dp[i][1]=1
if dp[-1][0]==1 or dp[-1][1]==1:
    print("Yes")
else:
    print("No")