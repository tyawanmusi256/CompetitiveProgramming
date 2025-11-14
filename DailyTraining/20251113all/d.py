n=int(input())
qr=[]
for _ in range(n):
    q,r=map(int,input().split())
    qr.append((q,r))
for _ in range(int(input())):
    t,d=map(int,input().split())
    t-=1
    q,r=qr[t]
    dd=d%q
    x=(r-dd)%q
    print(d+x)
    