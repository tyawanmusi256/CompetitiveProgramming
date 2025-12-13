n=int(input())
s=input()
from collections import deque
q=deque()
q.append(n)
for i in range(n-1,-1,-1):
    if s[i]=="L":
        q.append(i)
    else:
        q.appendleft(i)
print(*q)