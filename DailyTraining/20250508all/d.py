n=int(input())
a=list(map(int,input().split()))
x=[0,360]
t=0
for i in a:
    t+=i
    t%=360
    x.append(t)
x.sort()
print(max(x[i+1]-x[i] for i in range(len(x)-1)))