n=int(input())-1
a=[]
while n:
    a.append(n%5)
    n//=5
ans=0
for i in range(len(a)):
    ans+=2*a[i]*(10**i)
print(ans)