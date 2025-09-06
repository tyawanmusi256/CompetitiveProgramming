n,m=map(int,input().split())
dis=[[1]*n for _ in range(n)]
for i in range(m):
    a=list(map(int,input().split()))
    for j in range(1,n):
        dis[a[j-1]-1][a[j]-1]=0
        dis[a[j]-1][a[j-1]-1]=0
ans=0
for i in range(n):
    dis[i][i]=0
    for j in range(n):
        if dis[i][j]==1:
            ans+=1
print(ans//2)