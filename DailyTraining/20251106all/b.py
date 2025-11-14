n,l,r=map(int,input().split())
a=list(range(1,l))+list(range(l,r+1))[::-1]+list(range(r+1,n+1))
print(*a)