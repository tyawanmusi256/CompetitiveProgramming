x,y=map(int,input().split())
for i in range(8):
    new=int(str(x+y)[::-1])
    x,y=y,new
print(y)