h,w=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(h)]
p=list(map(int,input().split()))
for i in range(h):
    for j in range(w):
        a[i][j]-=p[i+j]
dp=[[10**18]*(w+1)for _ in range(h+1)]
dp[h-1][w-1]=max(0,-a[h-1][w-1])
for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if i==h-1 and j==w-1:
            continue
        dp[i][j]=max(0,min(dp[i+1][j],dp[i][j+1])-a[i][j])
print(dp[0][0])