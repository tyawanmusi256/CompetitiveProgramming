n=int(input())
h=list(map(int, input().split()))
ans=1
for d in range(1,n):
    for i in range(n):
        tmp=h[i]
        s=0
        for j in range(i,n,d):
            if tmp==h[j]:s+=1
            else:break
        ans=max(ans,s)
print(ans)