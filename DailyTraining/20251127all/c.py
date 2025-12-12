xa,ya=map(int,input().split())
xb,yb=map(int,input().split())
xc,yc=map(int,input().split())
ab=(xa-xb)**2+(ya-yb)**2
ac=(xa-xc)**2+(ya-yc)**2
bc=(xb-xc)**2+(yb-yc)**2
if max(ab,ac,bc)*2==ab+ac+bc:
    print("Yes")
else:
    print("No")