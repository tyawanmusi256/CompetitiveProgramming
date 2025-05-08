n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[i//k for i in a if i%k==0]
print(*ans)