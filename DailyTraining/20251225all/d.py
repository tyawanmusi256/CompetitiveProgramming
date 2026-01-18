n,q=map(int,input().split())
l=1
r=2
ans=0
for _ in range(q):
    h,t=input().split()
    t=int(t)
    if h=="R":
        if r<l:
            able=list(range(l-n+1,l))
        else:
            able=list(range(l+1,l+n))
        for i in able:
            if i%n==t%n:
                ans+=abs(r-i)
                r=i
                break
    else:
        if l<r:
            able=list(range(r-n+1,r))
        else:
            able=list(range(r+1,r+n))
        for i in able:
            if i%n==t%n:
                ans+=abs(l-i)
                l=i
                break
print(ans)
