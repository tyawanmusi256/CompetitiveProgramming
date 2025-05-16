from sortedcontainers import SortedSet, SortedList, SortedDict
h,w,q=map(int,input().split())
row=[SortedSet() for _ in range(h)]
col=[SortedSet() for _ in range(w)]
for i in range(h):
    for j in range(w):
        row[i].add(j)
        col[j].add(i)
for _ in range(q):
    r,c=map(int,input().split())
    r-=1
    c-=1
    if c in row[r]:
        row[r].discard(c)
        col[c].discard(r)
        continue
    j=row[r].bisect_left(c)
    if j<len(row[r]):
        e=row[r][j]
        row[r].discard(e)
        col[e].discard(r)
    if j>0:
        e=row[r][j-1]
        row[r].discard(e)
        col[e].discard(r)
    
    i=col[c].bisect_left(r)
    if i<len(col[c]):
        e=col[c][i]
        col[c].discard(e)
        row[e].discard(c)
    if i>0:
        e=col[c][i-1]
        col[c].discard(e)
        row[e].discard(c)

print(sum(len(r) for r in row))

