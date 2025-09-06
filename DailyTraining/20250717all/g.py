from bisect import bisect_left
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
l=[0]*(n+1)
r=[0]*(n+1)
for i in range(n):
    l[i+1]=l[i]+a[i]
for i in range(n-1,-1,-1):
    r[i]=r[i+1]+a[i]
for _ in range(q):
    x=int(input())
    if x<a[0]:
        print(l[n]-x*n)
        continue
    if x>a[-1]:
        print(x*n-r[0])
        continue
    i=bisect_left(a,x)
    ll=x*i-l[i]
    rr=r[i+1]-x*(n-i-1)
    ans=ll+rr+abs(x-a[i])
    print(ans)