h,w=map(int,input().split())
s=[list(input())for _ in range(h)]
b=[]
for i in range(h):
    for j in range(w):
        if not(s[i][j]=="." or s[i][j]=="#"):
            b.append((i,j,int(s[i][j])))
for x,y,n in b:
    for i in range(h):
        for j in range(w):
            if abs(x-i)+abs(y-j)<=n:
                s[i][j]="."
for i in range(h):
    print("".join(s[i]))