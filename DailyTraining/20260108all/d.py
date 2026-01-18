n=int(input())
a=list(map(int,input().split()))
ans=0
b=[0]
for i in a[::-1]:
    b.append(b[-1]+i)
b=b[1:]
print(n-sum(1 for i in range(n) if b[i]<4))