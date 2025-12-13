dij=[(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
xa,ya,xb,yb=map(int,input().split())
s=set()
for di,dj in dij:
    s.add((xa+di,ya+dj))
for di,dj in dij:
    if (xb+di,yb+dj) in s:
        print("Yes")
        exit()
print("No")