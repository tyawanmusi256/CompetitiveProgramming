n,d=map(int,input().split())
x=list(map(int,input().split()))
y=[(x[i],i)for i in range(n)]
y.sort()
ans=[]
for i in range(n):
    t=0
    if i!=0:
        t+=y[i][0]-y[i-1][0]>=d
    else:
        t+=1
    if i!=n-1:
        t+=y[i+1][0]-y[i][0]>=d
    else:
        t+=1
    if t==2:
        ans.append(y[i][1]+1)
print(len(ans))
print(*sorted(ans))