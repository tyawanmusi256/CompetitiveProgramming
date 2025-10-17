n=int(input())
a=list(map(int,input().split()))
from collections import Counter
c=Counter(a)
s=list(set(a))
s.sort(reverse=True)
for i in range(n):
    if i>=len(s):
        print(0)
    else:
        print(c[s[i]])