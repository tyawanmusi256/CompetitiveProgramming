from more_itertools import distinct_permutations
n,k=map(int, input().split())
s=input()
ans=0
for t in distinct_permutations(s):
    flag=True
    for i in range(len(t)-k+1):
        t1=t[i:i+k]
        if t1==t1[::-1]:
            flag=False
            break
    if flag:
        ans+=1
print(ans)
