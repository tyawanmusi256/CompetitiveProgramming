map_7x7 = [
[0, 47, 11, 10, 5, 28, 7],
[23, 9, 22, 24, 48, 14, 30],
[12, 25, 29, 38, 37, 19, 40],
[32, 26, 31, 6, 27, 41, 33],
[43, 18, 16, 45, 4, 20, 36],
[34, 8, 42, 3, 17, 1, 35],
[2, 15, 21, 44, 46, 13, 39]
]

map_5x5 = [
    [20, 16, 1, 17, 12],
[13, 10, 22, 2, 11],
[6, 18, 7, 19, 24],
[3, 21, 8, 15, 9],
[4, 5, 0, 23, 14]
]


n = 363
x = n**2-1
if n%4==1:
    grid=[[j^x for j in i]for i in map_5x5]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            assert grid[i][j]<=x
else:
    grid=[[j^x for j in i]for i in map_7x7]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            assert grid[i][j]<=x