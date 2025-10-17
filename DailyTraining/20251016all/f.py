n,m=map(int,input().split())
a=list(map(int,input().split()))
x=sum(a[:m])
ans=tmp=sum((i+1)*a[i] for i in range(m))
for i in range(m,n):
    tmp-=x
    x+=a[i]-a[i-m]
    tmp+=m*a[i]
    ans=max(ans,tmp)
print(ans)