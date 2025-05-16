n,m,q=map(int,input().split())
allok=set()
ok=set()
for _ in range(q):
    i=list(map(int,input().split()))
    if i[0]==1:
        x,y=i[1],i[2]
        ok.add((x,y))
    elif i[0]==2:
        x=i[1]
        allok.add(x)
    else:
        x,y=i[1],i[2]
        if x in allok or (x,y) in ok:
            print("Yes")
        else:
            print("No")

