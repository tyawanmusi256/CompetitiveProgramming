s=list(input())
n=len(s)
k=int(input())
r=0
c=0
ans=0
for l in range(n):
    while c<=k and r<n:
        if s[r]==".":
            c+=1
        r+=1
    ans=max(ans,r-l-(1 if c>k else 0))
    # print(l,r)
    if s[l]==".":
        c-=1
print(ans)