n=int(input())
d=dict()
for _ in range(n):
    a,c=map(int,input().split())
    if c not in d:
        d[c]=a
    else:
        d[c]=min(d[c],a)
ans=0
for i in d:
    ans=max(ans,d[i])
print(ans)