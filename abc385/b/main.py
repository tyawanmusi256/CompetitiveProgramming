h,w,x,y=map(int, input().split())
x-=1
y-=1
s=[list(input())for _ in range(h)]
t=input()
ans=0
for i in t:
    if i=="U":
        if s[x-1][y]=="#":
            continue
        if s[x-1][y]=="@":
            ans+=1
            s[x-1][y]="."
        x-=1
    if i=="D":
        if s[x+1][y]=="#":
            continue
        if s[x+1][y]=="@":
            ans+=1
            s[x+1][y]="."
        x+=1
    if i=="L":
        if s[x][y-1]=="#":
            continue
        if s[x][y-1]=="@":
            ans+=1
            s[x][y-1]="."
        y-=1
    if i=="R":
        if s[x][y+1]=="#":
            continue
        if s[x][y+1]=="@":
            ans+=1
            s[x][y+1]="."
        y+=1
print(x+1,y+1,ans)