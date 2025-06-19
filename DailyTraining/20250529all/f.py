n,k=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
ans=0
for i in a:
    if ans==i:
        ans+=1
        k-=1
    elif ans>i:
        continue
    else:
        break
    if k==0:
        break
print(ans)