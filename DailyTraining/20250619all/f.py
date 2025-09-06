n,m=map(int,input().split())
ka=[list(map(int,input().split()))for _ in range(m)]
b=list(map(int,input().split()))
dic={}
for i in range(n):
    dic[b[i]]=i
ans=[0]*n
for i in range(m):
    k=ka[i][0]
    idx=max(dic[ka[i][j]] for j in range(1,k+1))
    ans[idx]+=1
for i in range(1,n):ans[i]+=ans[i-1]
print(*ans)