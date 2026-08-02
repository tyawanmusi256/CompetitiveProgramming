n=int(input())
import itertools
p=list(map(int,input().split()))
q=list(map(int,input().split()))
ans=0
for i in itertools.permutations(p):
    if list(i)>=q:
        break
    ans+=1
print(ans)