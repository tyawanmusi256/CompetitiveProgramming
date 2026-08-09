n=int(input())
c=list(map(int,input().split()))
from collections import Counter
d=Counter(c)
print(n-max(d.values()))