#a,b,cを降順としてf(i,j,k)>=f(ii,jj,kk) i<=ii, j<=jj, k<=kk は明らか
n,kk=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort(reverse=1)
b.sort(reverse=1)
c.sort(reverse=1)
f=lambda i,j,k:a[i]*b[j]+b[j]*c[k]+c[k]*a[i]
from heapq import heappop,heappush
s=set()
h=[]
s.add((0,0,0))
heappush(h,(-f(0,0,0),0,0,0))
for _ in range(kk):
    cc,i,j,k=heappop(h)
    cc*=-1
    if not (i+1,j,k) in s and max(i+1,j,k)<n:
        s.add((i+1,j,k))
        heappush(h,(-f(i+1,j,k),i+1,j,k))
    if not (i,j+1,k) in s and max(i,j+1,k)<n:
        s.add((i,j+1,k))
        heappush(h,(-f(i,j+1,k),i,j+1,k))
    if not (i,j,k+1) in s and max(i,j,k+1)<n:
        s.add((i,j,k+1))
        heappush(h,(-f(i,j,k+1),i,j,k+1))
print(cc)