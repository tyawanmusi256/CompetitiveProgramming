n=int(input())
s=[input()for _ in range(n)]
x,y=input().split()
if s[int(x)-1]==y:
    print("Yes")
else:
    print("No")