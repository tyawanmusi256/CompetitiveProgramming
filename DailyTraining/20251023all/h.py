n=int(input())
c=list(map(int,input().split()))[::-1]
mi=min(c)
x=9-c.index(mi)
m=n//mi
mii=min(i for i in range(9) if c[i]<=mi+(n-mi*m))
y=9-mii
if x>=y:
    ans=str(x)*m
else:
    dif=c[mii]-mi
    can=(n-mi*m)//dif
    ans=str(y)*can+str(x)*(m-can)
print(ans)