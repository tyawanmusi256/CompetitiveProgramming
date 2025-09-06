n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=k*(k+1)//2
s=set()
for i in a:
    if not 1<=i<=k:
        continue
    if i in s:
        continue
    s.add(i)
    ans-=i
print(ans)