s=list(input())
if len(s)==2:
    if int("".join(s))%8==0 or int("".join(s[::-1]))%8==0:print("Yes")
    else:print("No")
    exit()
if len(s)==1:
    if s[0]=="8":print("Yes")
    else:print("No")
    exit()
from collections import defaultdict,Counter
d=defaultdict(int)
for i in s:d[i]+=1
for i in range(0,1000,8):
    f=Counter(list(str(i).zfill(3)))
    flag=True
    for j in f:
        if f[j]>d[j]:flag=False
    if flag:
        print("Yes")
        exit()
print("No")