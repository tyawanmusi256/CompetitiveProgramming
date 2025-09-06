import sys
input = sys.stdin.readline
mod=998244353
n,m,k=map(int,input().split())
ng1=[]
ng2=[]
for _ in range(m):
    a,b=map(int,input().split())
    ng1.append(a-1)
    ng2.append(b-1)
dp=[0]*n
dp[0]=1
t=1
for _ in range(k):
    ndp=[t-i for i in dp]
    tt=t*(n-1)
    ng11=ng1
    ng22=ng2
    dpl=dp
    for i in range(m):
        a=ng11[i]
        b=ng22[i]
        ndp[b]-=dpl[a]
        ndp[a]-=dpl[b]
        tt-=dpl[a]+dpl[b]
    t=tt%mod
    dp=ndp
print(dp[0]%mod)