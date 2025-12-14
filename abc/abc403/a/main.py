n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(0,n,2):
    ans+=a[i]
print(ans)