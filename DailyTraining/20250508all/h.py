n,m=map(int,input().split())
p=list(map(int,input().split()))
def check(x,m):
    y=0
    for i in range(n):
        k=int((x/p[i]+1)/2)
        y+=k*k*p[i]
        if y>m:
            return False
    return True
ok,ng=0,m+1
while ok+1<ng:
    mid=(ok+ng)//2
    if check(mid,m):
        ok=mid
    else:
        ng=mid
x=ok
ans=0
y=0
cnt=0
for i in range(n):
    k=int((x/p[i]+1)/2)
    ans+=k
    y+=k*k*p[i]
    if (2*k+1)*p[i]==x+1:
        cnt+=1
ans+=min((m-y)//(x+1),cnt)
print(ans)