n,q=map(int,input().split())
p=list(map(int,input().split()))
pq=[[0]*n,[0]*n]
for i in range(n):
    pq[0][i]=p[i]-1
    pq[1][p[i]-1]=i
z=0
for _ in range(q):
    query=input().split()
    if query[0]=="1":
        x,y=map(int,query[1:])
        if z==0:
            pq[1][pq[0][x-1]],pq[1][pq[0][y-1]]=pq[1][pq[0][y-1]],pq[1][pq[0][x-1]]
            pq[0][x-1],pq[0][y-1]=pq[0][y-1],pq[0][x-1]
        else:
            pq[0][pq[1][x-1]],pq[0][pq[1][y-1]]=pq[0][pq[1][y-1]],pq[0][pq[1][x-1]]
            pq[1][x-1],pq[1][y-1]=pq[1][y-1],pq[1][x-1]
    else:
        z^=1
print(*(i+1 for i in pq[z]))