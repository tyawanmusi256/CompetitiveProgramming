n=int(input())
a=list(map(int,input().split()))
sump=1
mod=998244353
invn=pow(n,mod-2,mod)
ans=0
for i in range(n):
    p=sump*invn%mod
    ans=(ans+a[i]*p)%mod
    sump=(sump+p)%mod
print(ans)