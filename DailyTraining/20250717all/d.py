n=int(input())
grid=[[0]*100 for _ in range(100)]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    for i in range(a,b):
        for j in range(c,d):
            grid[i][j]=1
print(sum(sum(row) for row in grid))