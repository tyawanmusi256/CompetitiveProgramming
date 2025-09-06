h,w,n=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
#座標圧縮
x_coords = sorted(set(a for a, b in ab))
y_coords = sorted(set(b for a, b in ab))
x_map = {x: i for i, x in enumerate(x_coords)}
y_map = {y: i for i, y in enumerate(y_coords)}
for a,b in ab:
    print(x_map[a]+1, y_map[b]+1)