n=int(input())
p=[0]+list(map(int,input().split()))
ans=0
x=n-1
while x!=0:
    x=p[x]-1
    ans+=1
print(ans)