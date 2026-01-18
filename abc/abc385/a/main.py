a,b,c=map(int,input().split())
if a==b==c or max(a,b,c)*2==a+b+c:print("Yes")
else:print("No")
