n=int(input())
x=[-1000000001]+list(map(int,input().split()))+[1000000001]
p=[0]+list(map(int,input().split()))+[0]
n+=2
for i in range(1,n):
    p[i]+=p[i-1]

from bisect import bisect_left as bl, bisect_right as br
for _ in range(int(input())):
    l,r=map(int,input().split())
    l=bl(x,l)
    r=br(x,r)-1
    print(p[r]-p[l-1])