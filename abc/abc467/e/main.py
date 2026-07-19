#難しくない？
#c[i]=(b[i]-a[i]-a[i+1])%mとして、d[i]+d[i+1]=c[i]となるようなdを作る
#d[1]=c[0]-d[0], d[2]=c[1]-d[1]=c[1]-c[0]+d[0], d[3]=c[2]-d[2]=c[2]-c[1]+c[0]-d[0]

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[(b[i]-a[i]-a[i+1])%m for i in range(n-1)]
d=[0]*n
for i in range(n-1):
    d[i+1]=(c[i]-d[i])%m

from collections import defaultdict
events=defaultdict(int)
for i in range(n):
    if i&1:
        #d[0]をあとd[i]+1だけ増やすとd[i]が1->->0->m-1と到達してしまう
        events[d[i]+1]+=m
    else:
        #d[0]をあとm-d[i]だけ増やすとd[i]がm-1->0と一周する
        events[m-d[i]]-=m

tmp=sum(d)
ans=tmp
keys=[0]+sorted(events.keys())
for i in range(1,len(keys)):
    if keys[i]<m:
        if n&1:
            tmp+=keys[i]-keys[i-1]
        tmp+=events[keys[i]]
        ans=min(ans,tmp)
print(ans)