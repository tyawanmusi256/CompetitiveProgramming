n,k=map(int,input().split())
k=n-k
a=list(map(int,input().split()))
a.sort()
ans=10**9
for i in range(n):
    if i+k-1==n:
        break
    ans=min(ans,a[i+k-1]-a[i])
print(ans)