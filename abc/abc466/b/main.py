n,m=map(int,input().split())
x=[-1]*m
for i in range(n):
    c,s=map(int,input().split())
    x[c-1]=max(x[c-1],s)
print(*x)