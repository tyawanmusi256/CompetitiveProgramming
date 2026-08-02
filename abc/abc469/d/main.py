n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]
ans=set()
tmp=ab[0][0]
s=set(list(range(1,n+1)))
for i in range(m):
    if not tmp in ab[i]:
        s&=set(ab[i])
for i in s:
    if tmp!=i:
        ans.add((min(tmp,i),max(tmp,i)))
tmp=ab[0][1]
s=set(list(range(1,n+1)))
for i in range(m):
    if not tmp in ab[i]:
        s&=set(ab[i])
for i in s:
    if tmp!=i:
        ans.add((min(tmp,i),max(tmp,i)))
print(len(ans))