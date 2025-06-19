import sys
sys.setrecursionlimit(10**6)

n,x=map(int,input().split())
l=[]
a=[]
for i in range(n):
    la=list(map(int,input().split()))
    l.append(la[0])
    a.append(la[1:])

def dfs(y, visited):
    ans=0
    if visited==n-1:
        return y==1
    for i in range(l[visited+1]):
        j = a[visited+1][i]
        if y%j==0:
            ans += dfs(y//j, visited+1)
    return ans
print(dfs(x, -1))