n=int(input())
a=list(map(int,input().split()))
b=[]
d={}
for i in range(n):
    if a[i] in d:
        b.append(d[a[i]])
        d[a[i]]=i+1
    else:
        b.append(-1)
        d[a[i]]=i+1
print(*b)