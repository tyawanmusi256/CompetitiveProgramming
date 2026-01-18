n,d=map(int,input().split())
a=list(map(int,input().split()))
c=[0]*1000001
for i in a:
    c[i]+=1
if d==0:
    print(sum(max(i-1,0) for i in c))
    exit()
ans=0
for i in range(d):
    b=[]
    for j in range(i,1000001,d):
        b.append(c[j])
    b=[0]+b+[0]
    m=len(b)
    dp=[[0]*m for _ in range(2)]
    for j in range(1,m):
        dp[0][j]=dp[1][j-1]
        dp[1][j]=min(dp[1][j-1]+b[j],dp[0][j-1]+b[j])
    ans+=min(dp[0][m-1],dp[1][m-1])
print(ans)