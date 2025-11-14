from heapq import heappop, heappush
n=int(input())
h=[]
for _ in range(n):
    s,c=map(int,input().split())
    heappush(h,(s,c))
ans=0
while len(h)>1:
    s1,c1=heappop(h)
    s2,c2=heappop(h)
    if s1==s2:
        heappush(h,(s1,c1+c2))
    else:
        heappush(h,(s2,c2))
        if c1>1:
            heappush(h,(s1*2,c1//2))
        ans+=c1%2
ans+=heappop(h)[1].bit_count()
print(ans)