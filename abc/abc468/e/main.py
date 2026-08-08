# 1/1 * 111111111
# 1/2 * 122222221
# 1/3 * 123333321
# 1/4 * 1234444321
# 1/5 * 1234554321
# 1/6 * 1234554321
# 1/7 * 1234444321
# 1/8 * 1233333321
# 1/9 * 1222222221
# 1/10 * 1111111111

mod=998244353
n=int(input())
a=list(map(int,input().split()))
for i in range(n//2):
    a[i]+=a[n-1-i]
b=[0]
for i in range(1,n+1):
    b.append((b[i-1]+pow(i,mod-2,mod))%mod)
ans=0
tmp=b[n]
for i in range(1,(n+1)//2+1):
    ans+=(a[i-1]*tmp)%mod
    tmp+=b[n-i]-b[i]
    ans%=mod
    tmp%=mod
print(ans)