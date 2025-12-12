n,c=map(int,input().split())
a=list(map(int,input().split()))
a[c-1]+=1
s=sum(a)
x=a[c-1]
a.sort()
mod=998244353
dp=[0]*n
# dp_i = 靴下iを持っている状態からスタートする期待値
#dp_i=1+sum_{j<i}(a[j]dp[i]/s)+sum_{j>i}(a[j]dp[j]/s)
#dp_i*(1-sum_{j<i}(a[j]/s))=1+sum_{j>i}(a[j]dp[j]/s)

# dp[n-1]=s*pow(a[n-1],mod-2,mod)%mod
# b=[0]
# for i in a:
#     b.append(b[-1]+i)
# for i in range(len(b)):
#     b[i]=b[i]*pow(s,mod-2,mod)%mod
# tmp=0
# for i in range(n-2,-1,-1):
#     tmp+=a[i+1]*dp[i+1]%mod
#     tmp%=mod
#     dp[i]=(1+tmp*pow(s,mod-2,mod))*pow((mod+1-b[i]*pow(s,mod-2,mod)%mod),mod-2,mod)%mod

dp[n-1]=s/a[n-1]
b=[0]
for i in a:
    b.append(b[-1]+i)
for i in range(len(b)):
    b[i]=b[i]/s
tmp=0
for i in range(n-2,-1,-1):
    tmp+=a[i+1]*dp[i+1]
    dp[i]=(1+tmp/s)/(1-b[i]/s)
print(dp[a.index(x)])
print(dp)