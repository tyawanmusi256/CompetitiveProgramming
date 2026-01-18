def solve():
    n,w=map(int, input().split())
    bag=[[0]for _ in range(61)]
    for i in range(n):
        x,y=map(int, input().split())
        bag[x].append(y)
    ans=0
    for i in range(60):
        bag[i].sort(reverse=True)
        if w>>i&1:
            ans+=bag[i][0]
            for j in range(1, len(bag[i])-1,2):
                bag[i+1].append(bag[i][j]+bag[i][j+1])
        else:
            for j in range(0, len(bag[i])-1, 2):
                bag[i+1].append(bag[i][j]+bag[i][j+1])
    return ans

for _ in range(int(input())):
    print(solve())