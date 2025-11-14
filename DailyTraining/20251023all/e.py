n,k=map(int,input().split())
a=list(map(int,input().split()))
s=set(a)
a=sorted(s)
if a[:k]==list(range(0,k)):
    print(k)
else:
    for i in range(k):
        if len(a)==i:
            print(i)
            break
        if a[i]!=i:
            print(i)
            break