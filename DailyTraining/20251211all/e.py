h1,w1=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h1)]
h2,w2=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(h2)]
from itertools import combinations
for rows in combinations(range(h1),h2):
    for cols in combinations(range(w1),w2):
        c=[[a[r][c] for c in cols] for r in rows]
        if c==b:
            print("Yes")
            exit()
print("No")