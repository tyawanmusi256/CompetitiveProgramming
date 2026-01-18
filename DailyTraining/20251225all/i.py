n=int(input())
a=list(map(int,input().split()))
#dp[S]:=集合Sの要素で構成される1122数列ができるa[:r]の最小のr
idx=[[]for _ in range(20)]
for i,v in enumerate(a):
    idx[v-1].append(i)
dp=[10**9]*(1<<20)
dp[0]=0
from bisect import bisect_left
ans=0
for s in range(1<<20):
    r=dp[s]
    if r==10**9:
        continue
    ans=max(ans,bin(s).count("1"))
    for bit in range(20):
        if s>>bit&1:
            continue
        i=bisect_left(idx[bit],r)
        # print(bin(s),idx[bit],r,i)
        if i==len(idx[bit]) or i+1==len(idx[bit]):
            continue
        dp[s|1<<bit]=min(dp[s|1<<bit],idx[bit][i+1])
print(ans*2)

