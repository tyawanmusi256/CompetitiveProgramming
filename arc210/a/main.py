n,q=map(int,input().split())
a=[0]*n
b=[0]*(n-1)
for _ in range(q):
    i,x=map(int,input().split())
    i-=1
    a[i]+=x
    if i!=n-1:
        b[i]=max(b[i],a[i]-a[i+1])
    if i!=0:
        b[i-1]=max(b[i-1],a[i-1]-a[i])
ans=[1]
for i in b:
    ans.append(ans[-1]+i+1)
print(sum(ans))