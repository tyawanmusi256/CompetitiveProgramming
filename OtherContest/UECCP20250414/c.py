from bisect import bisect_left as bl, bisect_right as br
n=int(input())
a=list(map(int,input().split()))
b=[0]
for i in range(1,n):
    b.append(b[i-1])
    if i%2==0:
        b[i]+=a[i]-a[i-1]
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    ans=0
    ll=bl(a,l)
    rr=br(a,r)-1
    ans+=b[rr]-b[ll] 
    if ll%2==0:
        ans+=a[ll]-l
    if rr%2:
        ans+=r-a[rr]
    print(ans)