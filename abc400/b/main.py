n,m=map(int,input().split())
if n==1:
    exit(print(m+1))
ans=0
for i in range(m+1):
    ans+=n**i
    if ans>10**9:
        exit(print("inf"))
print(ans)