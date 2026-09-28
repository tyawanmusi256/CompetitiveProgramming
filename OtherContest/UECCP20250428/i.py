import sys
input = lambda:sys.stdin.readline().rstrip()
import numpy as np
n=int(input())
xy=[list(map(int,input().split()))for _ in range(n)]
op=[np.array([[1,0,0],[0,1,0],[0,0,1]])]
for _ in range(int(input())):
    query=list(map(int,input().split()))
    if query[0]==1:
        op.append(np.array([[0,1,0],[-1,0,0],[0,0,1]]) @ op[-1])
    if query[0]==2:
        op.append(np.array([[0,-1,0],[1,0,0],[0,0,1]]) @ op[-1])
    if query[0]==3:
        p=query[1]
        op.append(np.array([[-1,0,2*p],[0,1,0],[0,0,1]]) @ op[-1])
    if query[0]==4:
        p=query[1]
        op.append(np.array([[1,0,0],[0,-1,2*p],[0,0,1]]) @ op[-1])
for _ in range(int(input())):
    a,b=map(int,input().split())
    x,y=xy[b-1]
    print(op[a])
    print(op[a][0,0]*x + op[a][0,1]*y + op[a][0,2], op[a][1,0]*x + op[a][1,1]*y + op[a][1,2])