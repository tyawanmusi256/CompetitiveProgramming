h,w=map(int,input().split())
s=[list(input())for _ in range(h)]
visited=[[0]*w for _ in range(h)]
stack=[]
for i in range(h):
    for j in range(w):
        if s[i][j]=="E":
            visited[i][j]=1
            stack.append((i,j))
dx,dy=[1,-1,0,0],[0,0,1,-1]
for i,j in stack:
    for k in range(4):
        x,y=i+dx[k],j+dy[k]
        if 0<=x<h and 0<=y<w and s[x][y]!="#" and visited[x][y]==0:
            visited[x][y]=1
            stack.append((x,y))
            if k==0:
                s[x][y]="^"
            elif k==1:
                s[x][y]="v"
            elif k==2:
                s[x][y]="<"
            else:
                s[x][y]=">"
for i in s:
    print("".join(i))