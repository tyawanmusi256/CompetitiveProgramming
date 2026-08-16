# [1,6],[2,3],[4,5]がある

n=int(input())
st=[list(map(int,input().split()))for _ in range(n)]
st.sort()
d=[0]*(2*n+2)
for i in range(n):
    d[st[i][0]]+=1
    d[st[i][1]+1]-=1
for i in range(1,2*n+2):
    d[i]+=d[i-1]
    if d[i]>=3:
        exit(print(0))
mod=998244353
ans=1
i=0
tmp=-1
while i<n:
    if tmp<st[i][0]:
        ans*=2
        ans%=mod
        tmp=st[i][1]
    else:
        tmp=max(tmp,st[i][1])
    i+=1
print(ans)
