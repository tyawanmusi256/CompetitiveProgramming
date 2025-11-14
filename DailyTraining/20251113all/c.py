s=input()
from collections import Counter
cnt=Counter(s)
a=[]
for x in cnt:
    a.append((-cnt[x],x))
a.sort()
print(a[0][1])