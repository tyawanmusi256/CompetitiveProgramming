n=int(input())
a=list(map(int,list(input())))
b=list(map(int,list(input())))
c=list(map(int,list(input())))
ans=10**9
for i in range(n):
    for j in range(n):
        for k in range(n):
            if not a[i]==b[j]==c[k]:
                continue
            if i==j==k:
                ans=min(ans,i+n+n)
            elif i==j:
                ans=min(ans,i+n)
            elif j==k:
                ans=min(ans,j+n)
            elif k==i:
                ans=min(ans,k+n)
            else:
                ans=min(ans,max(i,j,k))
print(ans if ans!=10**9 else -1)