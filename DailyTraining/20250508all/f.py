n=int(input())
a=list(map(int,input().split()))
ans=sum(i+1==a[i] for i in range(n))
ans=ans*(ans-1)//2
x=0
for i in range(n):
    if i+1!=a[i] and a[a[i]-1]==i+1:
        x+=1
print(ans+x//2)