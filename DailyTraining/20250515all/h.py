n=int(input())
a=list(map(int,input().split()))
ok=1
ng=10**9+1
inf=10**9+1
while ng-ok>0.001:
    mid=(ok+ng)/2
    dp=[[-inf]*2 for _ in range(n)]
    dp[0]=[a[0]-mid,-inf]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1])+a[i]-mid
        if i==1:
            dp[i][0]=max(dp[i][0],a[i]-mid)
        dp[i][1]=dp[i-1][0]
    if max(dp[n-1])>=0:
        ok=mid
    else:
        ng=mid
print(ok)

ok=1
ng=10**9+1
while ng-ok>1:
    mid=(ok+ng)//2
    f=lambda x: (x>=mid)*2-1
    dp=[[0]*2 for _ in range(n)]
    dp[0][0]=f(a[0])
    for i in range(1,n):
        dp[i][0]=max(dp[i-1])+f(a[i])
        if i==1:
            dp[i][0]=max(dp[i][0],f(a[i]))
        dp[i][1]=dp[i-1][0]
    if max(dp[n-1])>0:
        ok=mid
    else:
        ng=mid
print(ok)