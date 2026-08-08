from itertools import permutations
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
ans=0
for i in permutations(range(1,n+1)):
    if p<list(i)<q:
        ans+=1
print(ans)