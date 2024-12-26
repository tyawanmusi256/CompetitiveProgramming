from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from bisect import bisect_left
n,m,sx,sy=map(int, input().split())
xx=defaultdict(SortedSet)
yy=defaultdict(SortedSet)
xy=[]
for i in range(n):
    x,y=map(int, input().split())
    xx[x].add(y)
    yy[y].add(x)
    xy.append((x,y))

ans=0
for _ in range(m):
    d,c=input().split()
    c=int(c)
    if d=="U":
        if sx in xx:
            for y in xx[sx].irange(sy,sy+c):
                ans+=1
                yy[y].discard(sx)
                xx[sx].discard(y)
        sy+=c
    if d=="D":
        if sx in xx:
            for y in xx[sx].irange(sy-c,sy):
                ans+=1
                yy[y].discard(sx)
                xx[sx].discard(y)
        sy-=c
    if d=="L":
        if sy in yy:
            for x in yy[sy].irange(sx-c,sx):
                ans+=1
                xx[x].discard(sy)
                yy[sy].discard(x)
        sx-=c
    if d=="R":
        if sy in yy:
            for x in yy[sy].irange(sx,sx+c):
                ans+=1
                xx[x].discard(sy)
                yy[sy].discard(x)
        sx+=c
print(sx,sy,ans)