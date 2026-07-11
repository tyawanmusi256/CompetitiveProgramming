mod = 998244353

def solve(n):
    s=input()
    dp=[0]*(n+5)
    dp_p=[0]*(n+5)
    dp[1]=1
    t=1
    soloC=0
    ans=0
    for c in s:
        if c=="I":
            t+=1
            for i in range(t,1,-1):
                dp[i]+=dp[i-1]
                dp[i]%=mod
        elif c=="P":
            for i in range(1,t+1):
                dp[i]+=dp_p[i]
                dp[i]%=mod
        elif c=="C":
            soloC+=1
            ans+=dp[1]
            ans%=mod
            for i in range(1,t+1):
                dp_p[i]+=dp[i+1]
                dp_p[i]%=mod
    print((ans-soloC)%mod)

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)