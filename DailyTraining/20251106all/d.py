q=int(input())
a=[]
for _ in range(q):
    i,x=map(int,input().split())
    if i==1:
        a.append(x)
    else:
        print(a[-x])