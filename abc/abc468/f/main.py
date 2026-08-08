#LISをとる
#yは常に最大値を取る、更新できるなら更新する
from bisect import bisect_left
n=int(input())
p=list(map(int,input().split()))
y=0
q=[]
ans=0
for i in range(n):
    if p[i]>y:
        ans+=1
        y=p[i]
    else:
        q.append(p[i])
dp=[n+1]*len(q)
for i in q:
    dp[bisect_left(dp,i)]=i
ans+=bisect_left(dp,n+1)
print(ans)