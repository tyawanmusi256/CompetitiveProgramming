n=int(input())
a=list(map(int,input().split()))
x=[0]*4
p=0
for i in range(n):
    x[0]+=1
    for j in range(3,-1,-1):
        if j+a[i] < 4:
            x[j+a[i]]+=x[j]
            x[j]=0
        else:
            p+=x[j]
            x[j]=0
print(p)
        