n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[0]
for i in a:b.append(b[-1]+i)
ans=0
j=0
for i in range(n):
    if j!=n:
        while b[j+1]-b[i]<k:
            j+=1
            if j==n:break
    ans+=j-i
print(n*(n+1)//2-ans)