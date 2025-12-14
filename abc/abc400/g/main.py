import sys
input = sys.stdin.readline
from copy import deepcopy
inf=10**18

def solve():
    n,m=map(int, input().split())
    dp=[[-inf]*8 for _ in range(3)]
    dp[0][0]=0
    xyz=[list(map(int, input().split())) for _ in range(n)]
    xyz.sort(key=lambda x: max(x), reverse=True)
    for i in range(2*m):
        x,y,z=xyz[i]
        ndp=deepcopy(dp)
        dp=[[-inf]*8 for _ in range(3)]
        for j in range(3):
            for k in range(8):
                if j!=0:
                    dp[j][k]=max(dp[j][k],ndp[j-1][k])
                dp[j][k]=max(dp[j][k],ndp[j][k^1]+x)
                dp[j][k]=max(dp[j][k],ndp[j][k^2]+y)
                dp[j][k]=max(dp[j][k],ndp[j][k^4]+z)
    for i in range(2*m,n):
        x,y,z=xyz[i]
        ndp=deepcopy(dp)
        dp=[[-inf]*8 for _ in range(3)]
        dp[0][0]=0
        for j in range(3):
            for k in range(8):
                dp[j][k]=max(dp[j][k],ndp[j][k])
                if j!=2:
                    dp[j][k]=max(dp[j][k],ndp[j+1][k^1]+x)
                    dp[j][k]=max(dp[j][k],ndp[j+1][k^2]+y)
                    dp[j][k]=max(dp[j][k],ndp[j+1][k^4]+z)
    print(dp[0][0])

for _ in range(int(input())):
    solve()