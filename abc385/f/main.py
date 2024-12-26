n=int(input())
x=[]
h=[]
for _ in range(n):
    xx,hh=map(int, input().split())
    x.append(xx)
    h.append(hh)
flag=True
for i in range(n-1):
    if h[i]*x[i+1]>=x[i]*h[i+1]:
        flag=False
        break
if flag:
    print(-1)
    exit()
print(max((h[i]*x[i+1]-h[i+1]*x[i])/(x[i+1]-x[i])for i in range(n-1)))