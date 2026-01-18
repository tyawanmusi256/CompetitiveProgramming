n,h,w=map(int,input().split())
tiles=[tuple(map(int,input().split()))for _ in range(n)]
import itertools
for perm in itertools.permutations(tiles):
    grid=[[0]*w for _ in range(h)]
    ind=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0:
                if ind>=n:
                    break
                th,tw=perm[ind]
                for x in range(i,i+th):
                    for y in range(j,j+tw):
                        if x>=h or y>=w:
                            grid[0][0]=-10**9
                            break
                        if grid[x][y]==1:
                            grid[x][y]=-10**9
                        else:
                            grid[x][y]=1
                ind+=1
    if sum(sum(i)for i in grid)==h*w:
        print("Yes")
        break
print("No")