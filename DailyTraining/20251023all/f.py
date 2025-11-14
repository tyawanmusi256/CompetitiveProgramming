n=int(input())
a=[1]*(2*n+2)
print(1)
t=int(input())
c=1
a[1]=0
for i in range(2,2*n+2):
    a[t]=0
    if a[i]==0:continue
    print(i)
    c+=1
    if c==n+1:break
    t=int(input())
    a[i]=0

