a,b=map(int,input().split())
x=a//b
if abs(x-a/b)<abs(x+1-a/b):
    print(x)
else:
    print(x+1)