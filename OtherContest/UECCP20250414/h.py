n,x,m=map(int,input().split())
a=[x]
count=[0]*m
count[x]=1
while 1 and len(a)<n:
    x=(x*x)%m
    if count[x]:
        i=a.index(x)
        l=len(a)-i
        ans=sum(a)
        n-=len(a)
        ans+=sum(a[i:])*(n//l)
        n%=l
        ans+=sum(a[i:i+n])
        print(ans)
        exit()
    a.append(x)
    count[x]=1
print(sum(a))