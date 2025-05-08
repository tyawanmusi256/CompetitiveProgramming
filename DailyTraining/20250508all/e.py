h,w,d=map(int,input().split())
g=[list(input())for _ in range(h)]
visited=[[0]*w for _ in range(h)]
queue=[]
for i in range(h):
    for j in range(w):
        if g[i][j]=="H":
            visited[i][j]=1
            queue.append((i,j))
for x,y in queue:
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx,ny=x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and visited[nx][ny]==0 and g[nx][ny]==".":
            visited[nx][ny]=visited[x][y]+1
            queue.append((nx,ny))
ans=0
for i in range(h):
    for j in range(w):
        if 0<visited[i][j]<=d+1:
            ans+=1
print(ans)