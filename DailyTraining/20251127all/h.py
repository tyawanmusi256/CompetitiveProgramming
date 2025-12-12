n,m=map(int,input().split())
edge=[[]for _ in range(n)]
deg=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    deg[b-1]+=1
q=-1
ans=[node for node in range(n) if deg[node]==0]
if len(ans)!=1:
    print("No")
    exit()
q=ans[0]
while q!=-1:
    node=q
    q=-1
    for to in edge[node]:
        deg[to]-=1
        if deg[to]==0:
            if q!=-1:
                print("No")
                exit()
            q=to
            ans.append(to)
a=[0]*n
for i in range(n):
    a[ans[i]]=i+1
print("Yes")
print(*a)