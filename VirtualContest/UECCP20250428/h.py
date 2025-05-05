k=int(input())
n=50
a=[k//50+n-1]*n
for i in range(k%50):
    a[i]+=50
    for j in range(n):
        if i!=j:a[j]-=1
print(n)
print(*a)