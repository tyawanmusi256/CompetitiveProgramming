n,k,x=map(int,input().split())
a=list(map(int,input().split()))
ans=a[:k]+[x]+a[k:]
print(*ans)