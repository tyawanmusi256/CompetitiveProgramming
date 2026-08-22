h,w,k=map(int,input().split())
danger_h=set()
danger_w=set()
s = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            danger_h.add(i)
            danger_w.add(j)
visited = [[-1]*w for _ in range(h)]
stack = []
for i in range(h):
    for j in range(w):
        if (not i in danger_h) and (not j in danger_w):
            stack.append((i,j))
            visited[i][j] = 0
for i,j in stack:
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = i+di,j+dj
        if 0<=ni<h and 0<=nj<w and visited[ni][nj]==-1 and s[ni][nj]==".":
            visited[ni][nj] = visited[i][j]+1
            stack.append((ni,nj))
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j]=="." and visited[i][j]!=-1 and visited[i][j]<=k:
            ans += 1
print(ans)
