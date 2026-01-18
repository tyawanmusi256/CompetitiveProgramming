n,k=map(int, input().split())
mod=10**9
a=[0]*(n+1)
for i in range(n+1):
    if i<k:
        a[i]=i+1
    elif i==k:
        a[i]=k*2
    else:
        a[i]=2*a[i-1]-a[i-k-1]
    a[i]%=mod
print((a[-1]-a[-2]+mod)%mod)